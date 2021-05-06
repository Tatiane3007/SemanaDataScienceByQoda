# https://dashboard.ngrok.com/signup
!pip install streamlit
!pip install pyngrok==4.1.1
!pip install yfinance

%%writefile app.py
import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Google!

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-3-25')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)


# https://dashboard.ngrok.com/signup
!ngrok authtoken 1s1klPmg7kDGgx1ZUuNmlM0Twgh_3o3Vy99MeToXTTjsAjqEP
!streamlit run app.py &>/dev/null&
from pyngrok import ngrok
# Setup a tunnel to the streamlit port 8501
public_url = ngrok.connect(port='8501')
public_url


#desligar tunel
!pgrep streamlit
!kill 149
!kill 264
ngrok.kill()
