# -*- coding: utf-8 -*-
"""
Created on Wed May 20 08:27:11 2020

@author: rodiyansyah
"""

import pandas as pd

df = pd.DataFrame({
    "name": ["sandi","fajar","rodiyansyah"],
    "age":[23,43,22],
    "sex":["male", "male","male"]}
    )
print(df)

#Each column in a DataFrame is a series
print(df['age'])

#create a Series from scratch
SeriesAge = pd.Series([33,52,34], name ="usia")

print(SeriesAge)

print("max on df: ",df["age"].max())

print("max on SeriesAge: ",SeriesAge.max())

print(df.describe())