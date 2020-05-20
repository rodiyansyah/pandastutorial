# -*- coding: utf-8 -*-
"""
Created on Wed May 20 19:50:04 2020

@author: rodiyansyah
"""


import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option("max_rows", None)

titanic = pd.read_csv('air_quality_no2.csv')


print(titanic)