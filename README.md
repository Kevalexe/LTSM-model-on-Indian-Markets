# LSTM Model on Indian Markets

Predicting stock prices of India’s top 15 companies using LSTM neural networks, combining historical closing prices with sentiment features.  
Achieved ~98.2% accuracy on an 80/20 train-test split.

---

## Features
- End-to-end pipeline: scraping → cleaning → preprocessing → model training → prediction  
- Uses **closing prices + sentiment** as features  
- LSTM model built with **TensorFlow/Keras**  
- Evaluation metrics: RMSE, MAE, MAPE, Accuracy  
- Visualization of predicted vs actual prices  

---

## Project Structure
├── scraper.py # Scrapes stock data
├── Cleaner.py # Cleans raw CSVs
├── DataLoader.py # Loads & preprocesses data
├── Model.py # LSTM model, training, evaluation
├── data_cleaned/ # Cleaned CSV files

yaml
Copy code

---

## Installation
```bash
git clone https://github.com/Kevalexe/LTSM-model-on-Indian-Markets.git
cd LTSM-model-on-Indian-Markets
pip install -r requirements.txt
(requirements: pandas, numpy, scikit-learn, tensorflow, matplotlib, vaderSentiment)

Usage
Scrape stock data:

bash
Copy code
python scraper.py
Clean scraped data:

bash
Copy code
python Cleaner.py
Train & evaluate model:

bash
Copy code
python Model.py
Outputs:

RMSE, MAE, MAPE, Accuracy

Plot of actual vs predicted prices

Results
Reported accuracy: ~98.2% (based on MAPE)

Works on 15 Indian companies’ stock data

Future Work
Automate sentiment scraping from news/Twitter

Add interactive UI (Streamlit / Tkinter) for live predictions

Explore GRU / BiLSTM for performance comparison

Author
Keval – Student, LDCE Ahmedabad

yaml
Copy code

---

Want me to also generate a **`requirements.txt`** for you so users can install 
