import pandas as pd
import numpy as np

import matplotlib.pyplot  as pl
import seaborn as sbn
data = pd.read_csv("la_jobs.csv",index_col=0)
data['OPEN_DATE']=data['OPEN_DATE']

data['OPEN_DATE'] = pd.to_datetime(data['OPEN_DATE'], format='%m/%d/%Y', errors='coerce')

date_counts = data['OPEN_DATE'].value_counts()
most_common_date = date_counts.idxmax()
print(most_common_date)