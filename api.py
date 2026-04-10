import os
from fredapi import Fred
import pandas as pd

api_key = os.getenv('FRED_API_KEY')
fred = Fred(api_key=api_key)


fred.search('gdp')