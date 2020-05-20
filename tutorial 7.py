# -*- coding: utf-8 -*-
"""
Created on Wed May 20 17:05:33 2020

@author: rodiyansyah
"""

import pandas as pd

titanic = pd.read_csv('titanic.csv')

print(titanic.head())


print('Avg Age: ', titanic['Age'].mean())

print('Median Age and Fare')
print(titanic[['Age', 'Fare']].median())

print('describe Age and Fare')
print(titanic[['Age', 'Fare']].describe())

print(titanic.agg({ 'Age':['min', 'max', 'median', 'skew'],
                   'Fare':['min', 'max', 'median', 'mean']
    }))


agg_group_by_cat = titanic[['Sex','Age']].groupby('Sex').mean()
print(agg_group_by_cat)