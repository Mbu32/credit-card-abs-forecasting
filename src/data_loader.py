import os
from fredapi import Fred
import pandas as pd

api_key = os.getenv('FRED_API_KEY')
fred = Fred(api_key=api_key)


DRCC = fred.get_series_all_releases('DRCCLACBS') # Credit Card Delinquency rate (all commercial banks)
COR = fred.get_series_all_releases('CORCCACBS') #Credit card charge-off rate
TERM = fred.get_series_all_releases('TERMCBCCALLNS') # Terms on Credit Card plans



os.makedirs('./data',exist_ok=True)
DRCC.to_csv('./data/DRCCLACBS.csv')
COR.to_csv('./data/CORCCACBS.csv')
TERM.to_csv('./data/TERMCBCCALLNS.csv')
