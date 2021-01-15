from time import time
from pandas.io.parsers import read_csv
import streamlit as st
import pandas as pd
import numpy as np
import time
import csv

dt = 'dt'
lat = 'LandAverageTemperature'
lat2 = 'landaveragetemperature'

st.title("Global Temperature Change from 1750-2015")

climate_url = ('GlobalTemperatures.csv')




@st.cache
def load_data_climate():
    data = pd.read_csv(climate_url, usecols=[dt, lat])
    data.dropna(inplace=True)
    
    return data

temp_data = load_data_climate()
 


if st.checkbox('Show raw data for historic global temperature'):
    st.write(temp_data)











