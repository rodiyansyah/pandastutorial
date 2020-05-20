# -*- coding: utf-8 -*-
"""
Created on Wed May 20 08:54:03 2020

@author: rodiyansyah
"""


import pandas as pd

titanic = pd.read_csv('titanic.csv')

# print(titanic.head())

#ambil seluruh kolom Age
print(titanic['Age'].head())

print('type titanic[\'age\']: ',type(titanic['Age']))

print('shape titanic[\'age\']: ',titanic['Age'].shape)

age_sex = titanic[['Age', 'Sex']]

print(age_sex.head())

print('type titanic[\'age\',\'sex\'] : ',type(age_sex))

print('shape titanic[\'age\',\'sex\'] : ',age_sex.shape)

print('==========================')
above35 = titanic[titanic['Age']>35]
print('diatas 35')
print(above35)

class23 = titanic[titanic['Pclass'].isin([2,3])]
print('class 2 dan 3')
print(class23)


age_no_na = titanic[titanic['Age'].notna()]
print('ada data umurnya')
print(age_no_na)


