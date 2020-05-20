# -*- coding: utf-8 -*-
"""
Created on Wed May 20 08:54:03 2020

@author: rodiyansyah
"""


import pandas as pd

titanic = pd.read_csv('titanic.csv')

# print(titanic.head())

#ambil seluruh kolom Age

print(titanic['Age'])