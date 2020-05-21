# -*- coding: utf-8 -*-
"""
Created on Thu May 21 05:46:09 2020

@author: rodiyansyah
"""


import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv('titanic.csv')

print(titanic['Name'].str.lower())