# LSTM-Based Stock Price Prediction on Indian Markets

This repository implements a deep learning pipeline to forecast stock prices of major Indian companies using **Long Short-Term Memory (LSTM)** networks.  
The model integrates **historical stock prices** with **sentiment features** to improve predictive accuracy.  

📈 Reported performance: **~98.2% accuracy** (MAPE-based) on an 80/20 train-test split.

---

## 🔑 Key Features
- **End-to-End Workflow**: data scraping → cleaning → preprocessing → model training → evaluation  
- **Hybrid Input**: combines numerical market data with sentiment scores  
- **Deep Learning Model**: LSTM architecture optimized for time series forecasting  
- **Evaluation Metrics**: RMSE, MAE, MAPE, and accuracy percentage  
- **Visualization**: plots predicted vs actual stock price trends  

---

## 📂 Project Structure
├── scraper.py # Data collection script
├── Cleaner.py # Cleans raw stock data into structured CSVs
├── DataLoader.py # Loads and preprocesses time-series sequences
├── Model.py # Defines, trains, and evaluates the LSTM model
├── data_cleaned/ # Repository of cleaned CSV files
└── README.md

yaml
Copy code

---

## ⚙️ Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/Kevalexe/LTSM-model-on-Indian-Markets.git
cd LTSM-model-on-Indian-Markets
pip install -r requirements.txt
Dependencies:

pandas, numpy, scikit-learn

tensorflow / keras

matplotlib

vaderSentiment

🚀 Usage
Scrape stock data

bash
Copy code
python scraper.py
Clean raw data

bash
Copy code
python Cleaner.py
Run model training & evaluation

bash
Copy code
python Model.py
Outputs:

Evaluation metrics (RMSE, MAE, MAPE, Accuracy)

Visualization: predicted vs actual closing prices

📊 Results
Accuracy: ~98.2% (based on MAPE)

Dataset: 15 leading Indian companies

Visualization: Actual vs Predicted stock trends show strong overlap

🔮 Future Improvements
Automate sentiment scraping from financial news/Twitter feeds

Add a Streamlit / Tkinter UI to allow users to select companies and visualize forecasts interactively

Compare against alternative architectures (GRU, BiLSTM, Transformer-based models)

Extend to multi-stock portfolio forecasting

👤 Author
Keval Mistry
Student, LDCE Ahmedabad
