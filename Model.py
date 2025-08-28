import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Import your loader
from DataLoader import load_data


def train_and_evaluate(file_path, stock_name="Stock", epochs=20, batch_size=32):
    # Load preprocessed data
    x_train, y_train, x_test, y_test, scaler = load_data(file_path)

    # Build model
    model = Sequential()
    model.add(LSTM(100, return_sequences=True, input_shape=(x_train.shape[1], x_train.shape[2])))
    model.add(Dropout(0.2))
    model.add(LSTM(100, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mean_squared_error')
    model.summary()

    # Train
    history = model.fit(
        x_train, y_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_data=(x_test, y_test)
    )

    # Predict
    predicted = model.predict(x_test)

    # Reconstruct shape for inverse scaling
    pred_close_scaled = np.zeros((predicted.shape[0], 2))  # 2 = features (Close+Sentiment)
    pred_close_scaled[:, 0] = predicted[:, 0]
    predicted_prices = scaler.inverse_transform(pred_close_scaled)[:, 0]

    actual_close_scaled = np.zeros((y_test.shape[0], 2))
    actual_close_scaled[:, 0] = y_test
    actual_prices = scaler.inverse_transform(actual_close_scaled)[:, 0]

    # Metrics
    rmse = np.sqrt(mean_squared_error(actual_prices, predicted_prices))
    mae = mean_absolute_error(actual_prices, predicted_prices)
    r2 = r2_score(actual_prices, predicted_prices)
    mape = np.mean(np.abs((actual_prices - predicted_prices) / actual_prices)) * 100
    accuracy = 100 - mape

    print(f"RMSE: {rmse:.2f}")
    print(f"MAE: {mae:.2f}")
    print(f"R² Score: {r2:.2f}")
    print(f"Model Accuracy: {accuracy:.2f}%")

    # Plot
    plt.figure(figsize=(12, 6))
    plt.plot(actual_prices, color='blue', label='Actual Prices')
    plt.plot(predicted_prices, color='red', label='Predicted Prices')
    plt.title(f"{stock_name} Stock Prediction with Sentiment")
    plt.xlabel("Days")
    plt.ylabel("Price")
    plt.legend()
    plt.show()
