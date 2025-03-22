import pandas as pd
import numpy as np

import matplotlib.pyplot  as pl
import seaborn as sbn

data = pd.read_csv("la_jobs.csv",index_col=0)
data["EXPERIENCE_LENGTH"] = data["EXPERIENCE_LENGTH"].replace("-", 0).astype(float)
data["EDUCATION_YEARS"] = data["EDUCATION_YEARS"].replace("-", 0).astype(float)

#print(data["EXPERIENCE_LENGTH"],data["EDUCATION_YEARS"])

x = data[data["EXPERIENCE_LENGTH"] > data["EDUCATION_YEARS"]]

print (x.head())