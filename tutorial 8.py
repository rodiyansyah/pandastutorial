# -*- coding: utf-8 -*-
"""
Created on Wed May 20 19:50:04 2020

@author: rodiyansyah
"""

import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option("max_rows", None)

titanic = pd.read_csv('titanic.csv')
air_quality = pd.read_csv('air_quality_long.csv')


#print(air_quality.head())

#sort titanic by Age
#print(titanic.sort_values(by="Age").head())

#sort by class and age descending order
#print(titanic.sort_values(by=['Pclass','Age'], ascending=False).head())

#filter for no2 only
no2 = air_quality[air_quality['parameter']=='no2']

#use measurements (head) for each location (groupby)
no2_subset = no2.sort_index().groupby(['location']).head(2)

print(no2_subset.pivot(columns='location', values='value'))
