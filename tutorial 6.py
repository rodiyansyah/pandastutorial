# -*- coding: utf-8 -*-
"""
Created on Wed May 20 16:54:16 2020

@author: rodiyansyah
"""


import pandas as pd

air_quality= pd.read_csv('air_quality_no2.csv', index_col=0, parse_dates=True)

#menambah kolom london meter cubic
air_quality['london_mgC'] = air_quality['station_london'] * 1882

#menambah kolom rasio paris/antwerp
air_quality['ratioParisAntWerp'] = air_quality['station_paris'] / air_quality['station_antwerp']

#mengganti nama kolom
air_quality_renamed = air_quality.rename(
    columns={'station_antwerp':'satu',
             'station_paris':'dua',
             'station_london':'tiga'})

print(air_quality.head())

print(air_quality_renamed.head())

print(air_quality_renamed.info())