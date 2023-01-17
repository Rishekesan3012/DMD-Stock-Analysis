import streamlit as st
from stockmarketprediction import readSymbol
from stockmarketprediction import dmd_analysis
from stockmarketprediction import dmd_pred

# from stockmarketprediction import dmd_pred
# from stockmarketprediction import dmd_pred_plot

st.title("Stock Price Prediction")

stock_exchange = ["nse50_sym", "nse100_SYM"]    
index = st.selectbox("Select a Stock Exchange", stock_exchange)

symbol, matx = readSymbol(index)
sym = st.selectbox("Choose a Symbol", symbol)

# input_3 = st.date_input("Enter a date:")
col1, col2 = st.columns(2)
from_date = col1.date_input("From:")
to_date = col2.date_input("To:")

training = st.number_input("Training Set (in days)",step=1,min_value=0)

pred_options = ["Next 5 days", "Next 10 days"]
predict = st.selectbox("Predict for",pred_options)

if st.button("Predict"):
   dmd_analysis(9,training,5)
   dmd_pred(25,12,sym)
