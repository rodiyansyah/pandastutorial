# -*- coding: utf-8 -*-
"""
Created on Wed May 20 15:47:10 2020

@author: rodiyansyah
"""


import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv('air_quality_no2.csv', index_col=0, parse_dates=True)
# print(air_quality.head())

#all data in 1 plot
#air_quality.plot()

#only data paris
#air_quality['station_paris'].plot()

#diagram titik-titik
#air_quality.plot.scatter(x='station_london', y='station_paris', alpha=0.4)

#plot box
#air_quality.plot.box()

# axs = air_quality.plot.area(figsize=(12,4), subplots=True)

fig, axs = plt.subplots(figsize=(12,4))
air_quality.plot.area(ax=axs)
axs.set_ylabel("NO2 consentration")
fig.savefig('dodol.png')