LSTM Model for Indian Market Stock Prediction

Predicting stock prices of India’s top 15 companies using LSTM neural networks, with sentiment features, clean data pipelines, and a modular architecture. Achieved ~98.2% accuracy on an 80/20 train-test split.

Table of Contents

Project Overview

Features

Project Structure

Installation & Setup

How to Run

Results & Accuracy

Future Enhancements

About

Project Overview

This project aims to forecast next-day closing stock prices for India's top 15 companies using a Long Short-Term Memory (LSTM) network. The workflow includes:

Scraping stock data via scraper.py

Cleaning and normalizing data through Cleaner.py

Preprocessing features (Close price + sentiment) and preparing sequences using DataLoader.py

Training and evaluating the LSTM model with Model.py

Visualization of predictions and evaluation metrics using matplotlib

Features

End-to-end stock prediction pipeline

Data scraping → cleaning → sequence generation → model → prediction

Multi-feature input: Combines historical closing prices and sentiment scores for improved forecasting.

Model evaluation: Uses RMSE, MAE, MAPE metrics, with visualizations of predicted vs. actual prices.

High reported accuracy: Around 98.2% accuracy over an 80/20 train-test split, according to MAPE-based calculation.

Project Structure
LTSM-model-on-Indian-Markets/
│
├── scraper.py         # Downloads historical stock data for 15 companies
├── Cleaner.py         # Cleans raw CSVs—removes NaNs, keeps numeric columns
├── DataLoader.py      # Loads cleaned data, adds sentiment, scales, prepares sequences
├── Model.py           # Builds, trains, evaluates, and plots the LSTM model
├── data_cleaned/      # Cleaned CSV files for each company
└── results/           # (Optional) Graphs and metrics for each stock

Installation & Setup

Clone the repo:

git clone https://github.com/Kevalexe/LTSM-model-on-Indian-Markets.git
cd LTSM-model-on-Indian-Markets


Install Python dependencies:

pip install pandas numpy scikit-learn tensorflow matplotlib vaderSentiment


Ensure you have a stable internet connection for scraping.

How to Run

Scrape stock data:

python scraper.py


Clean raw data:

python Cleaner.py


Load and preprocess:
This is handled internally when running the model.

Train and evaluate:

python Model.py


Once complete, the script outputs:

RMSE, MAE, MAPE, Approx. Accuracy (%)

A plot of actual vs. predicted closing prices

Results & Accuracy

Evaluation metrics are printed at the end of the model run. Based on your output logic:

MAPE (Mean Absolute Percentage Error) is computed, and Accuracy (%) = 100 – MAPE

The model currently reports approximately 98.2% accuracy on the 80/20 train-test split.

Future Enhancements

Automate sentiment scraping from financial news or Twitter.

Add interactive UI using Streamlit or desktop app for live predictions.

Train and compare models across multiple stocks in batch pipelines.

Introduce hyperparameter tuning, dropout adjustments, or alternative architectures like GRU or BiLSTM.

About

Created by Keval, this project showcases:

Full-stack data engineering and machine learning proficiency

Integration of sentiment analysis into time series forecasting

Strong modular Python code organization

Clear documentation and visual results

Feel free to explore, improve, or reach out for collaboration!

Let me know if you want enhancements to this README or help automating docs like plots or metrics inclusion!
