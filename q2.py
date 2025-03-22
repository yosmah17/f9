import pandas as pd
import numpy as np

import matplotlib.pyplot  as pl
import seaborn as sbn

data = pd.read_csv("la_jobs.csv",index_col=0)
data["SCHOOL_TYPE"]


print(data["SCHOOL_TYPE"])

x = data[data["SCHOOL_TYPE"]!="-"]

print (x)