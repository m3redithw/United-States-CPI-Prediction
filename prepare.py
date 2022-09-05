# ignore warning
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd

# working with dates
from datetime import datetime

def get_data():
    '''
    This function returns the cleaned dataset
    '''
    df = pd.read_csv('cpi.csv')
    # Convert label date to datetime
    df['label'] = pd.to_datetime(df['label'], infer_datetime_format=True)
    # Convert year to datetime
    df['year'] =  pd.to_datetime(df['year']).dt.to_period('Y')
    # Rename period to month
    df = df.rename(columns={'period': 'month'})
    # Convert period to datetime
    df['month'] = df['month'].str.replace('M', '')
    
    return df