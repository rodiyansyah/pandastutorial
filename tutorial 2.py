# -*- coding: utf-8 -*-
"""
Created on Wed May 20 08:27:42 2020

@author: rodiyansyah
"""


import pandas as pd

titanic = pd.read_csv('titanic.csv')

print(titanic.head(8))
print(titanic.dtypes)

#transfer to excel
# titanic.to_excel('data.xlsx', sheet_name='penumpang', index=False)


print('titanic Info')
print(titanic.info())