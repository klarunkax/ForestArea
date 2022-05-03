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
total_CLC_Forest = pandas.DataFrame(CLC_Forest)
CLC_1990 = CLC_Forest.loc[:,CLC_Forest.columns.str.startswith('1990')]
total_CLC_Forest['1990'] = CLC_1990.sum(axis=1)
CLC_2000 = CLC_Forest.loc[:,CLC_Forest.columns.str.startswith('2000')]
total_CLC_Forest['2000'] = CLC_2000.sum(axis=1)
print(total_CLC_Forest.to_string())
CLC_2006 = CLC_Forest.loc[:,CLC_Forest.columns.str.startswith('2006')]
total_CLC_Forest['2006'] = CLC_2006.sum(axis=1)
CLC_2012 = CLC_Forest.loc[:,CLC_Forest.columns.str.startswith('2012')]
total_CLC_Forest['2012'] = CLC_2012.sum(axis=1)
CLC_2018 = CLC_Forest.loc[:,CLC_Forest.columns.str.startswith('2018')]
total_CLC_Forest['2018'] = CLC_2018.sum(axis=1)
#delete forest categories and keep only totals for each year
total_CLC_Forest = total_CLC_Forest[['GRID_CODE', 'EEA39', 'EU27', '2000', '2006', '2012', '2018']]
#print(total_CLC_Forest.to_string())

#delete the country if it has NA for any of the years
#total_CLC_Forest_EEA39 = total_CLC_Forest.dropna(axis=0, how='any', subset=['1990', '2000', '2006', '2012', '2018'])


#
# # B.)create TOTAL FOREST for EU27
# #total_CLC_Forest_EU27 = total_CLC_Forest.dropna(axis=0, how='any', subset=['1990', '2000', '2006', '2012', '2018'])
total_CLC_Forest_EU27 = total_CLC_Forest[total_CLC_Forest["EU27"] == 1]
print(total_CLC_Forest_EU27.to_string())
total_CLC_Forest_EU27.loc['CLC_EU27'] = total_CLC_Forest_EU27.sum(numeric_only=True, axis=0)/1000000 #mil. hectares
print(total_CLC_Forest_EU27.to_string())
CLC_EU27 = total_CLC_Forest_EU27.loc["CLC_EU27"]
CLC_EU27 = CLC_EU27.iloc[3:]
print(CLC_EU27)

# # 2.)sum up categories to create CORE FOREST (all except TWS)
#CLC_Forest = CLC_Forest.drop(columns="1992") # PROBLEM!
total_core_CLC = pandas.DataFrame(CLC_Forest)
core_CLC_Forest = CLC_Forest.loc[:, ~CLC_Forest.columns.str.endswith('TWS')]

#print(CLC_Forest.to_string())

# CLC_1990 = core_CLC_Forest.loc[:,core_CLC_Forest.columns.str.startswith('1990')]
# total_core_CLC['1990'] = CLC_1990.sum(axis=1)
#print(CLC_1992)
CLC_2000 = core_CLC_Forest.loc[:,core_CLC_Forest.columns.str.startswith('2000')]
total_core_CLC['2000'] = CLC_2000.sum(axis=1)
#print(CLC_2000)
CLC_2006 = core_CLC_Forest.loc[:,core_CLC_Forest.columns.str.startswith('2006')]
total_core_CLC['2006'] = CLC_2006.sum(axis=1)
CLC_2012 = core_CLC_Forest.loc[:,core_CLC_Forest.columns.str.startswith('2012')]
total_core_CLC['2012'] = CLC_2012.sum(axis=1)
CLC_2018 = core_CLC_Forest.loc[:,core_CLC_Forest.columns.str.startswith('2018')]
total_core_CLC['2018'] = CLC_2018.sum(axis=1)

# #delete forest categories and keep only totals for each year
total_core_CLC = total_core_CLC[['GRID_CODE', 'EEA39', 'EU27', '2000', '2006', '2012', '2018']]


# B.)create CORE FOREST for EU27
total_core_CLC_EU27 = total_core_CLC.dropna(axis=0, how='any', subset=['2000', '2006', '2012', '2018'])
total_core_CLC_EU27 = total_core_CLC_EU27[total_core_CLC_EU27["EU27"] == 1]
total_core_CLC_EU27.loc['CLC_core_EU27'] = total_core_CLC_EU27.sum(numeric_only=True, axis=0)/1000000 #mil. hectares
#print(total_core_CLC_EU27.to_string())
CLC_core_EU27 = total_core_CLC_EU27.loc["CLC_core_EU27"]
CLC_core_EU27 = CLC_core_EU27.iloc[3:]
print(CLC_core_EU27)

 #3.)TWS = NON CORE FOREST
#print(CLC_Forest.to_string())

total_NONcore_CLC = pandas.DataFrame(CLC_Forest)
NONcore_CLC_Forest = CLC_Forest[['GRID_CODE', 'EEA39', '2000TWS', '2006TWS', '2012TWS', '2018TWS']]

# CLC_1990 = NONcore_CLC_Forest.loc[:,NONcore_CLC_Forest.columns.str.startswith('1990')]
# total_NONcore_CLC['1990'] = CLC_1990.sum(axis=1)
CLC_2000 = NONcore_CLC_Forest.loc[:,NONcore_CLC_Forest.columns.str.startswith('2000')]
total_NONcore_CLC['2000'] = CLC_2000.sum(axis=1)
CLC_2006 = NONcore_CLC_Forest.loc[:,NONcore_CLC_Forest.columns.str.startswith('2006')]
total_NONcore_CLC['2006'] = CLC_2006.sum(axis=1)
CLC_2012 = NONcore_CLC_Forest.loc[:,NONcore_CLC_Forest.columns.str.startswith('2012')]
total_NONcore_CLC['2012'] = CLC_2012.sum(axis=1)
CLC_2018 = NONcore_CLC_Forest.loc[:,NONcore_CLC_Forest.columns.str.startswith('2018')]
total_NONcore_CLC['2018'] = CLC_2018.sum(axis=1)

#delete forest categories and keep only totals for each year
total_NONcore_CLC = total_NONcore_CLC[['GRID_CODE', 'EEA39', 'EU27', '2000', '2006', '2012', '2018']]
#print(total_NONcore_CLC.to_string())


# B.)create NON-CORE FOREST for EU27
total_NONcore_CLC_EU27 = total_NONcore_CLC.dropna(axis=0, how='any', subset=['2000', '2006', '2012', '2018'])
total_NONcore_CLC_EU27 = total_NONcore_CLC_EU27[total_NONcore_CLC_EU27["EU27"] == 1]
total_NONcore_CLC_EU27.loc['CLC_NONcore_EU27'] = total_NONcore_CLC_EU27.sum(numeric_only=True, axis=0)/1000000 #mil. hectares
#print(total_core_CLC_EU27.to_string())
CLC_NONcore_EU27 = total_NONcore_CLC_EU27.loc["CLC_NONcore_EU27"]
CLC_NONcore_EU27 = CLC_NONcore_EU27.iloc[3:]
print(CLC_NONcore_EU27)

# 4.) Change data
#A) CLC_EU27
CLC_EU27 = pandas.DataFrame(CLC_EU27)
CLC_EU27_t = CLC_EU27.T
#CLC_NONcore_EU27_t["1990-2000"] = CLC_NONcore_EU27_t["2000"] - CLC_NONcore_EU27_t["1990"]
CLC_EU27_t["2000-2006"] = CLC_EU27_t["2006"] - CLC_EU27_t["2000"]
CLC_EU27_t["2006-2012"] = CLC_EU27_t["2012"] - CLC_EU27_t["2006"]
CLC_EU27_t["2012-2018"] = CLC_EU27_t["2018"] - CLC_EU27_t["2012"]
CLC_EU27_t = CLC_EU27_t[['2000-2006', '2006-2012', '2012-2018']]
CLC_EU27_change = CLC_EU27_t.T
print(CLC_EU27_change)

# D.) CLC_core_EU27
CLC_core_EU27 = pandas.DataFrame(CLC_core_EU27)
CLC_core_EU27_t = CLC_core_EU27.T
CLC_core_EU27_t["2000-2006"] = CLC_core_EU27_t["2006"] - CLC_core_EU27_t["2000"]
CLC_core_EU27_t["2006-2012"] = CLC_core_EU27_t["2012"] - CLC_core_EU27_t["2006"]
CLC_core_EU27_t["2012-2018"] = CLC_core_EU27_t["2018"] - CLC_core_EU27_t["2012"]

CLC_core_EU27_t = CLC_core_EU27_t[['2000-2006', '2006-2012', '2012-2018']]
CLC_core_EU27_change = CLC_core_EU27_t.T

print(CLC_core_EU27_change)


# F.) CLC_NONcore_EU27
CLC_NONcore_EU27 = pandas.DataFrame(CLC_NONcore_EU27)
CLC_NONcore_EU27_t = CLC_NONcore_EU27.T
CLC_NONcore_EU27_t["2000-2006"] = CLC_NONcore_EU27_t["2006"] - CLC_NONcore_EU27_t["2000"]
CLC_NONcore_EU27_t["2006-2012"] = CLC_NONcore_EU27_t["2012"] - CLC_NONcore_EU27_t["2006"]
CLC_NONcore_EU27_t["2012-2018"] = CLC_NONcore_EU27_t["2018"] - CLC_NONcore_EU27_t["2012"]

CLC_NONcore_EU27_t = CLC_NONcore_EU27_t[['2000-2006', '2006-2012', '2012-2018']]
CLC_NONcore_EU27_change = CLC_NONcore_EU27_t.T
print(CLC_NONcore_EU27_change)
#
# sum_CLC_EU27 = pandas.concat([CLC_EU27, CLC_core_EU27, CLC_NONcore_EU27], axis=1, join="inner")
# sum_CLC_EU27.to_csv('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/sum_tables/sum_CLC_EU27.csv')
# print(sum_CLC_EU27)
#
# change_CLC_EU27 = pandas.concat([CLC_EU27_change, CLC_core_EU27_change, CLC_NONcore_EU27_change], axis=1, join="inner")
# change_CLC_EU27.to_csv('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/sum_tables/change_CLC_EU27.csv')
# print(change_CLC_EU27)
# # # 6.) plot charts

# CLC_EU27.plot.bar(
# ylabel="milion hectares", xlabel="year", title="CLC total forest area in EU27", legend=None)
# plt.ylim(bottom=0, top=180)
# plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/CLC_EU27.png')
# plt.show()
# #
# 
# CLC_core_EU27.plot.bar(
# ylabel="milion hectares", xlabel="year", title="CLC core forest area in EU27", legend=None)
# plt.ylim(bottom=0, top=180)
# plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/CLC_core_EU27.png')
# plt.show()
# # #
# 
# CLC_NONcore_EU27.plot.bar(
# ylabel="milion hectares", xlabel="years", title="CLC non-core forest area in EU27", legend=None)
# plt.ylim(bottom=0, top=180)
# plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/CLC_NONcore_EU27.png')
# plt.show()
# # #
# # # #
# 
# 
# CLC_EU27_change.plot.bar(
# ylabel="milion hectares", xlabel="Years", title="CLC change in total forest area in EU27", legend=None)
# plt.ylim(bottom=-3, top=3.5)
# plt.xticks(rotation='horizontal')
# plt.axhline(y=0, color='r', linestyle='-')
# plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/CLC_EU27_change.png')
# plt.show()
# 
# 
# CLC_core_EU27_change.plot.bar(
# ylabel="milion hectares", xlabel="years", title="CLC change in core forest area in EU27", legend=None)
# plt.ylim(bottom=-3, top=3.5)
# plt.xticks(rotation='horizontal')
# plt.axhline(y=0, color='r', linestyle='-')
# plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/CLC_core_EU27_change.png')
# plt.show()
# 
# 
# CLC_NONcore_EU27_change.plot.bar(
# ylabel="milion hectares", xlabel="years", title="CLC change in non-core forest area in EU27", legend=None)
# plt.ylim(bottom=-3, top=3.5)
# plt.xticks(rotation='horizontal')
# plt.axhline(y=0, color='r', linestyle='-')
# plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/CLC_NONcore_EU27_change.png')
# plt.show()