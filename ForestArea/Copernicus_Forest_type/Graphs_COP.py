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

#1.) sum up all the forest catergories together by years = TOTAL FOREST
total_COP_Forest = pandas.DataFrame(COP_Forest)
COP_2012 = COP_Forest.loc[:,COP_Forest.columns.str.startswith('2012')]
total_COP_Forest['2012'] = COP_2012.sum(axis=1)
COP_2015 = COP_Forest.loc[:,COP_Forest.columns.str.startswith('2015')]
total_COP_Forest['2015'] = COP_2015.sum(axis=1)
COP_2018 = COP_Forest.loc[:,COP_Forest.columns.str.startswith('2018')]
total_COP_Forest['2018'] = COP_2018.sum(axis=1)
#delete forest categories and keep only totals for each year
total_COP_Forest = total_COP_Forest[['GRID_CODE', 'EEA39', 'EU27', '2012', '2015', '2018']]

# #delete the country if it has NA for any of the years
# total_COP_Forest_EEA39 = total_COP_Forest.dropna(axis=0, how='any', subset=['1992', '2000', '2005', '2006', '2010', '2012', '2015', '2018', '2020'])
# # A)create total forest for EEA39
# total_COP_Forest_EEA39.loc['COP_EEA39'] = total_COP_Forest_EEA39.sum(numeric_only=True, axis=0)/1000000 #mil. hectares
# COP_EEA39 = total_COP_Forest_EEA39.loc["COP_EEA39"]
# COP_EEA39 = COP_EEA39.iloc[3:]
# #print(COP_EEA39)

# B.)create TOTAL FOREST for EU27
total_COP_Forest_EU27 = total_COP_Forest.dropna(axis=0, how='any', subset=['2012', '2015', '2018'])
total_COP_Forest_EU27 = total_COP_Forest_EU27[total_COP_Forest_EU27["EU27"] == 1]
print(total_COP_Forest_EU27.to_string())
total_COP_Forest_EU27.loc['COP_EU27'] = total_COP_Forest_EU27.sum(numeric_only=True, axis=0)/1000000 #mil. hectares
COP_EU27 = total_COP_Forest_EU27.loc["COP_EU27"]
COP_EU27 = COP_EU27.iloc[3:]
print(COP_EU27)


# 4.) Change data
#A) COP_EU27 Total CHANGE
COP_EU27 = pandas.DataFrame(COP_EU27)
COP__change_EU27_t = COP_EU27.T
COP__change_EU27_t["2012-2015"] = COP__change_EU27_t["2015"] - COP__change_EU27_t["2012"]
COP__change_EU27_t["2015-2018"] = COP__change_EU27_t["2018"] - COP__change_EU27_t["2015"]
COP__change_EU27_t = COP__change_EU27_t[['2012-2015', '2015-2018']]
COP_EU27_change = COP__change_EU27_t.T
print(COP_EU27_change)


COP_EU27.to_csv('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/sum_tables/sum_COP_EU27.csv')

COP_EU27_change.to_csv('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/sum_tables/change_COP_EU27.csv')

# # # # 6.) plot charts
# # # COP_EEA39.plot.bar(
# # # ylabel="milion hectares", xlabel="year", title="COP forest area 1992-2018 ")
# # # plt.legend()
# # # plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/COP_EEA39.png')
# # # plt.show()
# # # #
# #
# COP_EU27.plot.bar(
# ylabel="milion hectares", xlabel="year", title="COP total forest area in EU27", legend=None)
# plt.ylim(bottom=0, top=180)
# plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/COP_EU27.png')
# plt.show()
# #
# # #
#
# COP_EU27_change.plot.bar(
# ylabel="milion hectares", xlabel="Years", title="COP change in total forest area in EU27", legend=None)
# plt.ylim(bottom=-3, top=8)
# plt.xticks(rotation='horizontal')
# plt.axhline(y=0, color='r', linestyle='-')
# plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/COP_EU27_change.png')
# plt.show()
