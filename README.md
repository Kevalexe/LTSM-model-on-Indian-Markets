# LSTM Model on Indian Stock Markets 🇮🇳📈

A Python project implementing a Long Short-Term Memory (LSTM) neural network to predict next-day closing prices of Indian stocks (NSE/BSE) using historical stock prices and sentiment analysis from news headlines.

## Table of Contents
- [Description](#description)  
- [Features](#features)  
- [Folder Structure](#folder-structure)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
  - [Running the App](#running-the-app)  
- [Metrics](#metrics)  
- [Planned Work](#planned-work)  
- [Author](#author)  

## Description
This project leverages an LSTM neural network to analyze and predict trends in Indian stock markets. Using historical stock price data and sentiment analysis from news headlines, the model forecasts short-term price movements. The project is modular and designed for future expansions such as real-time market data, advanced visualizations, and multiple stock pipelines.

## Features
- LSTM-based prediction for next-day closing prices  
- Data preprocessing, scaling, and sequence creation  
- Sentiment analysis integration using VADER  
- CLI interface to select which stock to train  
- Computes evaluation metrics: RMSE, MAE, R² Score, MAPE, and Accuracy (%)  
- Visualizes predicted vs actual prices using matplotlib  
- Modular structure for easy extensions and future improvements  

## Folder Structure

├── CLI.py # Command-line interface to choose stock CSV
├── DataLoader.py # Data preprocessing: scaling, sequences, sentiment
├── Model.py # LSTM model, training, evaluation, plotting
├── data_cleaned/ # Folder containing cleaned stock CSVs
├── README.md # Project documentation
└── requirements.txt # Required Python packages



## Getting Started

### Prerequisites
- Python ≥ 3.8  
- Libraries: `numpy`, `pandas`, `tensorflow`, `keras`, `matplotlib`, `scikit-learn`, `vaderSentiment`  
- Jupyter Notebook (optional, for experimentation)  

### Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/Kevalexe/LTSM-model-on-Indian-Markets.git
cd LTSM-model-on-Indian-Markets
Running the App
Place your cleaned stock CSV files inside the data_cleaned/ folder. Each CSV must have at least a Close column.
```
Run the CLI:



python CLI.py
Select the stock you want to train (enter the number). The model will train, evaluate, and display a plot of predicted vs actual prices.

Example output:


📂 Available stock datasets:
1. RELIANCE.csv
2. TCS.csv
3. INFY.csv

👉 Enter the number of the stock you want to train on: 1
📈 Training model for RELIANCE...
Model Accuracy: 92.45%
Metrics
RMSE: Root Mean Squared Error

MAE: Mean Absolute Error

R² Score: Coefficient of determination

MAPE: Mean Absolute Percentage Error

Accuracy (%): 100 - MAPE

Planned Work
Replace sample headlines with real-time news data

Add GUI interface for stock selection and interactive visualization

Save trained models for faster inference

Expand dataset to all NSE/BSE listed stocks

Author
Keval – Student & aspiring Quant/AI enthusiast
GitHub: Kevalexe
