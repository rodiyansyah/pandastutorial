# -*- coding: utf-8 -*-
"""
Created on Wed May 20 10:50:13 2020

@author: rodiyansyah
"""


import pandas as pd

titanic = pd.read_csv('titanic.csv')


adult_names = titanic.loc[titanic['Age']>35, ['Name','Age']]

print(adult_names)