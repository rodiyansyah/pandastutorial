# -*- coding: utf-8 -*-
"""
Created on Wed May 20 10:50:13 2020

@author: rodiyansyah
"""


import pandas as pd

titanic = pd.read_csv('titanic.csv')


adult_names = titanic.loc[titanic['Age']>35, ['Name','Age']]
print("Nama Age Passenger > 35 YO")
print(adult_names)

data = titanic.iloc[9:25, 2:5]
print("data row 10 hingga 25 kolom 3 sd 5")
print(data)

#merubah kolom 3 dari baris 0 sebanyak 3 dengan "dodol"
titanic.iloc[0:3, 3] = "dodol"

print(titanic.head())