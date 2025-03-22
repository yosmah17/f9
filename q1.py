import pandas as pd
import numpy as np

import matplotlib.pyplot  as pl
import seaborn as sbn

data = pd.read_csv("la_jobs.csv",index_col=0)
data["EXPERIENCE_LENGTH"].replace("-",0,inplace=True)
data["EXPERIENCE_LENGTH"] = data["EXPERIENCE_LENGTH"]

print(data["EXPERIENCE_LENGTH"])

x = data[data["EXPERIENCE_LENGTH"]== 0]

print (x)