import streamlit at st
import pathlib as path
import pandas as pd
import numpy as np
import os
import sys
import time


# Set the title of the dashboard
st.title("My First Streamlit Dashboard")

# Create a sidebar with a slider
st.sidebar.header("Settings")
slider_value = st.sidebar.slider("Select a value", 1, 100, 50)

# Generate some data based on the slider value
data = pd.DataFrame({
    'x': np.arange(1, slider_value + 1),
    'y': np.random.randn(slider_value).cumsum()
})

# Display the line chart
st.line_chart(data)

# Display the slider value
st.write("Slider value:", slider_value)





