import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def load_data(file_path, sequence_length=60):
    # Load CSV
    df = pd.read_csv(file_path)
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    df = df.dropna(subset=['Close']).reset_index(drop=True)

    # Example sentiment generation (replace with real news if available)
    headlines = [
        "Reliance posts record quarterly profit",
        "Reliance faces regulatory hurdles in new project",
    ] * (len(df)//2 + 1)
    headlines = headlines[:len(df)]

    analyzer = SentimentIntensityAnalyzer()
    df['Sentiment'] = [analyzer.polarity_scores(h)['compound'] for h in headlines]

    # Features: Close + Sentiment
    features = ['Close', 'Sentiment']
    data = df[features]

    # Scale
    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_data = scaler.fit_transform(data)

    # Create sequences
    x, y = [], []
    for i in range(sequence_length, len(scaled_data)):
        x.append(scaled_data[i-sequence_length:i])
        y.append(scaled_data[i, 0])  # predicting Close only

    x, y = np.array(x), np.array(y)

    # Train-test split
    split = int(0.8 * len(x))
    x_train, x_test = x[:split], x[split:]
    y_train, y_test = y[:split], y[split:]


    return  x_train, y_train, x_test, y_test, scaler
