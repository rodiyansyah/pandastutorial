# -*- coding: utf-8 -*-
"""
Created on Thu May 21 05:22:16 2020

@author: rodiyansyah
"""


import pandas as pd

air_quality_no2 = pd.read_csv('air_quality_no2_long.csv', parse_dates=True)

air_quality_no2 = air_quality_no2[['date.utc', 'location', 'parameter', 'value']]

#print(air_quality_no2.head())

air_quality_pm25 = pd.read_csv('air_quality_pm25_long.csv',  parse_dates=True)

air_quality_pm25 = air_quality_pm25[['date.utc', 'location', 'parameter', 'value']]

#print(air_quality_pm25.head())
stations_coord = pd.read_csv("air_quality_stations.csv")
air_quality_parameters = pd.read_csv("air_quality_parameters.csv")

#gabung pm25 dan no2
air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)
#urut by tanggal
air_quality = air_quality.sort_values('date.utc')
#gabung dengan koordinat
air_quality = pd.merge(air_quality, stations_coord, how='left', on='location')
#gabung dengan parameter
air_quality = pd.merge(air_quality, air_quality_parameters, how='left', 
                       left_on='parameter', right_on='id')





print(air_quality.head())