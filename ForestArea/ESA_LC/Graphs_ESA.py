import pandas
import os
import csv
import matplotlib.pyplot as plt
import numpy as np


os.chdir('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_tables')
#load the statistics
CLC_Forest = pandas.read_csv('CLC_Forest_v2.csv')
COP_Forest = pandas.read_csv('COP_Forest_v01.csv')
ESA_Forest = pandas.read_csv('ESA_Forest_v2.csv')
Modis_Forest = pandas.read_csv('modis_forest_v1.csv')

#put the stats into dataframes
CLC_Forest = pandas.DataFrame(CLC_Forest)
COP_Forest = pandas.DataFrame(COP_Forest)
ESA_Forest = pandas.DataFrame(ESA_Forest)
Modis_Forest = pandas.DataFrame(Modis_Forest)

#delete categories 30, 40, 170
ESA_Forest = ESA_Forest.loc[:, ~ESA_Forest.columns.str.endswith('_30')]
ESA_Forest = ESA_Forest.loc[:, ~ESA_Forest.columns.str.endswith('_40')]
ESA_Forest = ESA_Forest.loc[:, ~ESA_Forest.columns.str.endswith('_170')]

#sum up all the forest catergories together by years = TOTAL FOREST
total_ESA_Forest = pandas.DataFrame(ESA_Forest)
#print(list(ESA_Forest.columns))
ESA_1992 = ESA_Forest.loc[:,ESA_Forest.columns.str.startswith('1992')]
total_ESA_Forest['1992'] = ESA_1992.sum(axis=1)
ESA_2000 = ESA_Forest.loc[:,ESA_Forest.columns.str.startswith('2000')]
total_ESA_Forest['2000'] = ESA_2000.sum(axis=1)
ESA_2005 = ESA_Forest.loc[:,ESA_Forest.columns.str.startswith('2005')]
total_ESA_Forest['2005'] = ESA_2005.sum(axis=1)
ESA_2006 = ESA_Forest.loc[:,ESA_Forest.columns.str.startswith('2006')]
total_ESA_Forest['2006'] = ESA_2006.sum(axis=1)
ESA_2010 = ESA_Forest.loc[:,ESA_Forest.columns.str.startswith('2010')]
total_ESA_Forest['2010'] = ESA_2010.sum(axis=1)
ESA_2012 = ESA_Forest.loc[:,ESA_Forest.columns.str.startswith('2012')]
total_ESA_Forest['2012'] = ESA_2012.sum(axis=1)
ESA_2015 = ESA_Forest.loc[:,ESA_Forest.columns.str.startswith('2015')]
total_ESA_Forest['2015'] = ESA_2015.sum(axis=1)
ESA_2018 = ESA_Forest.loc[:,ESA_Forest.columns.str.startswith('2018')]
total_ESA_Forest['2018'] = ESA_2018.sum(axis=1)
ESA_2020 = ESA_Forest.loc[:,ESA_Forest.columns.str.startswith('2020')]
total_ESA_Forest['2020'] = ESA_2018.sum(axis=1)

#delete forest categories and keep only totals for each year
total_ESA_Forest = total_ESA_Forest[['GRID_CODE', 'EEA39', 'EU27', '1992', '2000', '2005', '2006', '2010', '2012', '2018', '2020']]
print(total_ESA_Forest.to_string())

#delete the country if it has NA for any of the years
total_ESA_Forest_EEA39 = total_ESA_Forest.dropna(axis=0, how='any', subset=['1992', '2000', '2005', '2006', '2010', '2012', '2018', '2020'])
# 1.)create total forest for EEA39
total_ESA_Forest_EEA39.loc['CLC_EEA39'] = total_ESA_Forest_EEA39.sum(numeric_only=True, axis=0)/1000000 #mil. hectares
ESA_EEA39 = total_ESA_Forest_EEA39.loc["CLC_EEA39"]
ESA_EEA39 = ESA_EEA39.iloc[3:]
print(ESA_EEA39)

# 2.)create TOTAL FOREST for EU27
total_ESA_Forest_EU27 = total_ESA_Forest.dropna(axis=0, how='any', subset=['1992', '2000', '2005', '2006', '2010', '2012', '2018', '2020'])
total_ESA_Forest_EU27 = total_ESA_Forest_EU27[total_ESA_Forest_EU27["EU27"] == 1]
total_ESA_Forest_EU27.loc['CLC_EU27'] = total_ESA_Forest_EU27.sum(numeric_only=True, axis=0)/1000000 #mil. hectares
ESA_EU27 = total_ESA_Forest_EU27.loc["CLC_EU27"]
ESA_EU27 = ESA_EU27.iloc[3:]
print(ESA_EU27)
#

# CLC_EEA39.plot(
# ylabel="milion hectares", xlabel="year", title="CLC forest area in EEA39 1990-2018 ")
# plt.legend()
# plt.show()
#
# CLC_EU27.plot(
# ylabel="milion hectares", xlabel="year", title="CLC forest area 1990-2018")
# plt.legend()
# plt.show()
#
# CLC_EU24.plot(
# ylabel="milion hectares", xlabel="year", title="CLC forest area 1990-2018")
#
# plt.legend()
# plt.show()

