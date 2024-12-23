import streamlit at st
import pathlib as path
import pandas as pd
import numpy as np
import os
import sys
import time


# Set the title of the dashboard
st.title('Real-Time Cryptocurrency Prices')
st.subheader('Data from CoinDesk API')

# Function to get crypto prices
def get_crypto_price(crypto):
    url = f"https://min-api.cryptocompare.com/data/price?fsym={crypto}&tsyms=USD"
    response = requests.get(url)
    data = response.json()
    return data['USD']

# Create a sidebar with a slider
st.sidebar.header("Settings")
slider_value = st.sidebar.slider("Select a value", 1, 100, 50)

placeholder = st.empty()

while True:
    data = fetch_data()
    btc_price = data['bpi']['USD']['rate']
    timestamp = data['time']['updated']

    with placeholder.container():
        st.write(f"**Bitcoin Price (USD):** ${btc_price}")
        st.write(f"**Last Updated:** {timestamp}")

    time.sleep(60)  # Update every 60 seconds

# Generate some data based on the slider value
data = pd.DataFrame({
    'x': np.arange(1, slider_value + 1),
    'y': np.random.randn(slider_value).cumsum()
})


# Display the line chart
st.line_chart(data)

# Display the slider value
st.write("Slider value:", slider_value)








