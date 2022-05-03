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


#1.) sum up all the forest catergories together by years = TOTAL FOREST
total_ESA_Forest = pandas.DataFrame(ESA_Forest)
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
total_ESA_Forest['2020'] = ESA_2020.sum(axis=1)
#delete forest categories and keep only totals for each year
total_ESA_Forest = total_ESA_Forest[['GRID_CODE', 'EEA39', 'EU27', '1992', '2000', '2005', '2006', '2010', '2012', '2015', '2018', '2020']]


#delete the country if it has NA for any of the years
total_ESA_Forest_EEA39 = total_ESA_Forest.dropna(axis=0, how='any', subset=['1992', '2000', '2005', '2006', '2010', '2012', '2015', '2018', '2020'])
# A)create total forest for EEA39
total_ESA_Forest_EEA39.loc['ESA_EEA39'] = total_ESA_Forest_EEA39.sum(numeric_only=True, axis=0)/1000000 #mil. hectares
ESA_EEA39 = total_ESA_Forest_EEA39.loc["ESA_EEA39"]
ESA_EEA39 = ESA_EEA39.iloc[3:]
#print(ESA_EEA39)

# B.)create TOTAL FOREST for EU27
total_ESA_Forest_EU27 = total_ESA_Forest.dropna(axis=0, how='any', subset=['1992', '2000', '2005', '2006', '2010', '2012', '2015', '2018', '2020'])
total_ESA_Forest_EU27 = total_ESA_Forest_EU27[total_ESA_Forest_EU27["EU27"] == 1]
print(total_ESA_Forest_EU27.to_string())
total_ESA_Forest_EU27.loc['ESA_EU27'] = total_ESA_Forest_EU27.sum(numeric_only=True, axis=0)/1000000 #mil. hectares
ESA_EU27 = total_ESA_Forest_EU27.loc["ESA_EU27"]
ESA_EU27 = ESA_EU27.iloc[3:]
#print(ESA_EU27)
# # 2.)sum up categories to create CORE FOREST (all except 100 a 110)
ESA_Forest = ESA_Forest.drop(columns="1992") # PROBLEM!
total_core_ESA = pandas.DataFrame(ESA_Forest)
core_ESA_Forest = ESA_Forest.loc[:, ~ESA_Forest.columns.str.endswith('_100')]
core_ESA_Forest = core_ESA_Forest.loc[:, ~core_ESA_Forest.columns.str.endswith('_110')]
#print(ESA_Forest.to_string())
#
ESA_1992 = core_ESA_Forest.loc[:,core_ESA_Forest.columns.str.startswith('1992')]
total_core_ESA['1992'] = ESA_1992.sum(axis=1)
#print(ESA_1992)
ESA_2000 = core_ESA_Forest.loc[:,core_ESA_Forest.columns.str.startswith('2000')]
total_core_ESA['2000'] = ESA_2000.sum(axis=1)
#print(ESA_2000)
ESA_2005 = core_ESA_Forest.loc[:,core_ESA_Forest.columns.str.startswith('2005')]
total_core_ESA['2005'] = ESA_2005.sum(axis=1)
ESA_2006 = core_ESA_Forest.loc[:,core_ESA_Forest.columns.str.startswith('2006')]
total_core_ESA['2006'] = ESA_2006.sum(axis=1)
ESA_2010 = core_ESA_Forest.loc[:,core_ESA_Forest.columns.str.startswith('2010')]
total_core_ESA['2010'] = ESA_2010.sum(axis=1)
ESA_2012 = core_ESA_Forest.loc[:,core_ESA_Forest.columns.str.startswith('2012')]
total_core_ESA['2012'] = ESA_2012.sum(axis=1)
ESA_2015 = core_ESA_Forest.loc[:,core_ESA_Forest.columns.str.startswith('2015')]
total_core_ESA['2015'] = ESA_2015.sum(axis=1)
ESA_2018 = core_ESA_Forest.loc[:,core_ESA_Forest.columns.str.startswith('2018')]
total_core_ESA['2018'] = ESA_2018.sum(axis=1)
ESA_2020 = core_ESA_Forest.loc[:,core_ESA_Forest.columns.str.startswith('2020')]
total_core_ESA['2020'] = ESA_2020.sum(axis=1)

# #delete forest categories and keep only totals for each year
total_core_ESA = total_core_ESA[['GRID_CODE', 'EEA39', 'EU27', '1992', '2000', '2005', '2006', '2010', '2012','2015', '2018', '2020']]
#print(total_core_ESA.to_string())
# # A)create CORE forest for EEA39
total_core_ESA_EEA39 = total_core_ESA.dropna(axis=0, how='any', subset=['1992', '2000', '2005', '2006', '2010', '2012','2015', '2018', '2020'])
total_core_ESA_EEA39.loc['ESA_core_EEA39'] = total_core_ESA_EEA39.sum(numeric_only=True, axis=0)/1000000 #mil. hectares
#print(total_core_ESA_EEA39.to_string())

ESA_core_EEA39 = total_core_ESA_EEA39.loc["ESA_core_EEA39"]
ESA_core_EEA39 = ESA_core_EEA39.iloc[3:]
#print(ESA_core_EEA39)

# B.)create CORE FOREST for EU27
total_core_ESA_EU27 = total_core_ESA.dropna(axis=0, how='any', subset=['1992', '2000', '2005', '2006', '2010', '2012', '2015', '2018', '2020'])
total_core_ESA_EU27 = total_core_ESA_EU27[total_core_ESA_EU27["EU27"] == 1]
total_core_ESA_EU27.loc['ESA_core_EU27'] = total_core_ESA_EU27.sum(numeric_only=True, axis=0)/1000000 #mil. hectares
#print(total_core_ESA_EU27.to_string())
ESA_core_EU27 = total_core_ESA_EU27.loc["ESA_core_EU27"]
ESA_core_EU27 = ESA_core_EU27.iloc[3:]
#print(ESA_core_EU27)

# 3.)sum up categories 100 a 110 to create NON CORE FOREST
#print(ESA_Forest.to_string())

total_NONcore_ESA = pandas.DataFrame(ESA_Forest)
NONcore_ESA_Forest = ESA_Forest[['GRID_CODE', 'EEA39', 'EU27', '1992_100', '1992_110', '2000_100', '2000_110', '2005_100', '2005_110', '2006_100', '2006_110', '2010_100', '2010_110', '2012_100', '2012_110', '2015_100', '2015_110', '2018_100', '2018_110', '2020_100', '2020_110']]

ESA_1992 = NONcore_ESA_Forest.loc[:,NONcore_ESA_Forest.columns.str.startswith('1992')]
total_NONcore_ESA['1992'] = ESA_1992.sum(axis=1)
ESA_2000 = NONcore_ESA_Forest.loc[:,NONcore_ESA_Forest.columns.str.startswith('2000')]
total_NONcore_ESA['2000'] = ESA_2000.sum(axis=1)
ESA_2005 = NONcore_ESA_Forest.loc[:,NONcore_ESA_Forest.columns.str.startswith('2005')]
total_NONcore_ESA['2005'] = ESA_2005.sum(axis=1)
ESA_2006 = NONcore_ESA_Forest.loc[:,NONcore_ESA_Forest.columns.str.startswith('2006')]
total_NONcore_ESA['2006'] = ESA_2006.sum(axis=1)
ESA_2010 = NONcore_ESA_Forest.loc[:,NONcore_ESA_Forest.columns.str.startswith('2010')]
total_NONcore_ESA['2010'] = ESA_2010.sum(axis=1)
ESA_2012 = NONcore_ESA_Forest.loc[:,NONcore_ESA_Forest.columns.str.startswith('2012')]
total_NONcore_ESA['2012'] = ESA_2012.sum(axis=1)
ESA_2015 = NONcore_ESA_Forest.loc[:,NONcore_ESA_Forest.columns.str.startswith('2015')]
total_NONcore_ESA['2015'] = ESA_2015.sum(axis=1)
ESA_2018 = NONcore_ESA_Forest.loc[:,NONcore_ESA_Forest.columns.str.startswith('2018')]
total_NONcore_ESA['2018'] = ESA_2018.sum(axis=1)
ESA_2020 = NONcore_ESA_Forest.loc[:,NONcore_ESA_Forest.columns.str.startswith('2020')]
total_NONcore_ESA['2020'] = ESA_2018.sum(axis=1)

#delete forest categories and keep only totals for each year
total_NONcore_ESA = total_NONcore_ESA[['GRID_CODE', 'EEA39', 'EU27', '1992', '2000', '2005', '2006', '2010', '2012','2015' , '2018', '2020']]
#print(total_NONcore_ESA.to_string())

# A)create NON-CORE forest for EEA39
total_NONcore_ESA_EEA39 = total_NONcore_ESA.dropna(axis=0, how='any', subset=['1992', '2000', '2005', '2006', '2010', '2012', '2015', '2018', '2020'])
total_NONcore_ESA_EEA39.loc['ESA_NONcore_EEA39'] = total_NONcore_ESA_EEA39.sum(numeric_only=True, axis=0)/1000000 #mil. hectares
ESA_NONcore_EEA39 = total_NONcore_ESA_EEA39.loc["ESA_NONcore_EEA39"]
ESA_NONcore_EEA39 = ESA_NONcore_EEA39.iloc[3:]
#print(ESA_NONcore_EEA39)

# B.)create NON-CORE FOREST for EU27
total_NONcore_ESA_EU27 = total_NONcore_ESA.dropna(axis=0, how='any', subset=['1992', '2000', '2005', '2006', '2010', '2012', '2018', '2020'])
total_NONcore_ESA_EU27 = total_NONcore_ESA_EU27[total_NONcore_ESA_EU27["EU27"] == 1]
total_NONcore_ESA_EU27.loc['ESA_NONcore_EU27'] = total_NONcore_ESA_EU27.sum(numeric_only=True, axis=0)/1000000 #mil. hectares
#print(total_core_ESA_EU27.to_string())
ESA_NONcore_EU27 = total_NONcore_ESA_EU27.loc["ESA_NONcore_EU27"]
ESA_NONcore_EU27 = ESA_NONcore_EU27.iloc[3:]
#print(ESA_NONcore_EU27)

# 4.) Change data
#A) ESA_EU27 Total CHANGE
ESA_EU27 = pandas.DataFrame(ESA_EU27)
ESA__change_EU27_t = ESA_EU27.T
ESA__change_EU27_t["1992-2000"] = ESA__change_EU27_t["2000"] - ESA__change_EU27_t["1992"]
ESA__change_EU27_t["2000-2005"] = ESA__change_EU27_t["2005"] - ESA__change_EU27_t["2000"]
ESA__change_EU27_t["2005-2010"] = ESA__change_EU27_t["2010"] - ESA__change_EU27_t["2005"]
ESA__change_EU27_t["2010-2015"] = ESA__change_EU27_t["2015"] - ESA__change_EU27_t["2010"]
ESA__change_EU27_t["2015-2020"] = ESA__change_EU27_t["2020"] - ESA__change_EU27_t["2015"]
ESA__change_EU27_t = ESA__change_EU27_t[['1992-2000', '2000-2005', '2005-2010', '2010-2015', '2015-2020']]
ESA_EU27_change = ESA__change_EU27_t.T
# print(ESA_EU27_change)

# #  B)ESA_EEA39 total
# ESA_EEA39 = pandas.DataFrame(ESA_EEA39)
# ESA__change_EU27_t = ESA_EEA39.T
# ESA__change_EU27_t["1992-2000"] = ESA__change_EU27_t["2000"] - ESA__change_EU27_t["1992"]
# ESA__change_EU27_t["2000-2005"] = ESA__change_EU27_t["2005"] - ESA__change_EU27_t["2000"]
# ESA__change_EU27_t["2005-2010"] = ESA__change_EU27_t["2010"] - ESA__change_EU27_t["2005"]
# ESA__change_EU27_t["2010-2015"] = ESA__change_EU27_t["2015"] - ESA__change_EU27_t["2010"]
# ESA__change_EU27_t["2015-2020"] = ESA__change_EU27_t["2020"] - ESA__change_EU27_t["2015"]
# ESA__change_EU27_t = ESA__change_EU27_t[['1992-2000', '2000-2005', '2005-2010', '2010-2015', '2015-2020']]
# ESA_EEA39_change = ESA__change_EU27_t.T
# # print(ESA_EEA39_change)

# # C.) ESA_core_EEA39 total
# ESA_core_EEA39 = pandas.DataFrame(ESA_core_EEA39)
# ESA__change_EU27_t = ESA_core_EEA39.T
# ESA__change_EU27_t["1992-2000"] = ESA__change_EU27_t["2000"] - ESA__change_EU27_t["1992"]
# ESA__change_EU27_t["2000-2005"] = ESA__change_EU27_t["2005"] - ESA__change_EU27_t["2000"]
# ESA__change_EU27_t["2005-2010"] = ESA__change_EU27_t["2010"] - ESA__change_EU27_t["2005"]
# ESA__change_EU27_t["2010-2015"] = ESA__change_EU27_t["2015"] - ESA__change_EU27_t["2010"]
# ESA__change_EU27_t["2015-2020"] = ESA__change_EU27_t["2020"] - ESA__change_EU27_t["2015"]
# ESA__change_EU27_t = ESA__change_EU27_t[['1992-2000', '2000-2005', '2005-2010', '2010-2015', '2015-2020']]
# ESA_core_EEA39_change = ESA__change_EU27_t.T
# # print(ESA_core_EEA39_change)

# D.) ESA_core_EU27 ChANGE
ESA_core_EU27 = pandas.DataFrame(ESA_core_EU27)
ESA__change_EU27_t = ESA_core_EU27.T
ESA__change_EU27_t["1992-2000"] = ESA__change_EU27_t["2000"] - ESA__change_EU27_t["1992"]
ESA__change_EU27_t["2000-2005"] = ESA__change_EU27_t["2005"] - ESA__change_EU27_t["2000"]
ESA__change_EU27_t["2005-2010"] = ESA__change_EU27_t["2010"] - ESA__change_EU27_t["2005"]
ESA__change_EU27_t["2010-2015"] = ESA__change_EU27_t["2015"] - ESA__change_EU27_t["2010"]
ESA__change_EU27_t["2015-2020"] = ESA__change_EU27_t["2020"] - ESA__change_EU27_t["2015"]
ESA__change_EU27_t = ESA__change_EU27_t[['1992-2000', '2000-2005', '2005-2010', '2010-2015', '2015-2020']]
ESA_core_EU27_change = ESA__change_EU27_t.T

# print(ESA_core_EU27_change)

# # E.) ESA_NONcore_EEA39 CHANGE
# ESA_NONcore_EEA39 = pandas.DataFrame(ESA_NONcore_EEA39)
# ESA__change_EU27_t = ESA_NONcore_EEA39.T
# ESA__change_EU27_t["1992-2000"] = ESA__change_EU27_t["2000"] - ESA__change_EU27_t["1992"]
# ESA__change_EU27_t["2000-2005"] = ESA__change_EU27_t["2005"] - ESA__change_EU27_t["2000"]
# ESA__change_EU27_t["2005-2010"] = ESA__change_EU27_t["2010"] - ESA__change_EU27_t["2005"]
# ESA__change_EU27_t["2010-2015"] = ESA__change_EU27_t["2015"] - ESA__change_EU27_t["2010"]
# ESA__change_EU27_t["2015-2020"] = ESA__change_EU27_t["2020"] - ESA__change_EU27_t["2015"]
# ESA__change_EU27_t = ESA__change_EU27_t[['1992-2000', '2000-2005', '2005-2010', '2010-2015', '2015-2020']]
# ESA_NONcore_EEA39_change = ESA__change_EU27_t.T
# # print(ESA_NONcore_EEA39_change)

# F.) ESA_NONcore_EU27 CHANGE
ESA_NONcore_EU27 = pandas.DataFrame(ESA_NONcore_EU27)
ESA__change_EU27_t = ESA_NONcore_EU27.T
ESA__change_EU27_t["1992-2000"] = ESA__change_EU27_t["2000"] - ESA__change_EU27_t["1992"]
ESA__change_EU27_t["2000-2005"] = ESA__change_EU27_t["2005"] - ESA__change_EU27_t["2000"]
ESA__change_EU27_t["2005-2010"] = ESA__change_EU27_t["2010"] - ESA__change_EU27_t["2005"]
ESA__change_EU27_t["2010-2015"] = ESA__change_EU27_t["2015"] - ESA__change_EU27_t["2010"]
ESA__change_EU27_t["2015-2020"] = ESA__change_EU27_t["2020"] - ESA__change_EU27_t["2015"]
ESA__change_EU27_t = ESA__change_EU27_t[['1992-2000', '2000-2005', '2005-2010', '2010-2015', '2015-2020']]
ESA_NONcore_EU27_change = ESA__change_EU27_t.T
# print(ESA_NONcore_EU27_change)
#

# 5.) ready data
print(ESA_EEA39)
print(ESA_EU27)
print(ESA_core_EEA39)
print(ESA_core_EU27)
print(ESA_NONcore_EEA39)
print(ESA_NONcore_EU27)
print(ESA_EU27_change)
print(ESA_core_EU27_change)
print(ESA_NONcore_EU27_change)

sum_ESA_EU27 = pandas.concat([ESA_EU27, ESA_core_EU27, ESA_NONcore_EU27], axis=1, join="inner")
sum_ESA_EU27.to_csv('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/sum_tables/sum_ESA_EU27.csv')
print(sum_ESA_EU27)

change_ESA_EU27 = pandas.concat([ESA_EU27_change, ESA_core_EU27_change, ESA_NONcore_EU27_change], axis=1, join="inner")
change_ESA_EU27.to_csv('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/sum_tables/change_ESA_EU27.csv')
print(change_ESA_EU27)
#
# # # 6.) plot charts
# # ESA_EEA39.plot.bar(
# # ylabel="milion hectares", xlabel="year", title="ESA forest area 1992-2018 ")
# # plt.legend()
# # plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/ESA_EEA39.png')
# # plt.show()
# # #
#
ESA_EU27.plot.bar(
ylabel="milion hectares", xlabel="year", title="ESA total forest area in EU27", legend=None)
plt.ylim(bottom=0, top=180)
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/ESA_EU27.png')
plt.show()
#
# # ESA_core_EEA39.plot.bar(
# # ylabel="milion hectares", xlabel="year", title="ESA forest area 1992-2018")
# # plt.legend()
# # plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/ESA_core_EEA39.png')
# # plt.show()
# #
ESA_core_EU27.plot.bar(
ylabel="milion hectares", xlabel="year", title="ESA core forest area in EU27", legend=None)
plt.ylim(bottom=0, top=180)
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/ESA_core_EU27.png')
plt.show()
# #
# # ESA_NONcore_EEA39.plot.bar(
# # ylabel="milion hectares", xlabel="year", title="ESA forest area 1992-2018")
# # plt.legend()
# # plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/ESA_NONcore_EEA39.png')
# # plt.show()
# #
#
ESA_NONcore_EU27.plot.bar(
ylabel="milion hectares", xlabel="years", title="ESA non-core forest area in EU27", legend=None)
plt.ylim(bottom=0, top=180)
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/ESA_NONcore_EU27.png')
plt.show()
# #
# # #


ESA_EU27_change.plot.bar(
ylabel="milion hectares", xlabel="Years", title="ESA change in total forest area in EU27", legend=None)
plt.ylim(bottom=-3, top=3.5)
plt.xticks(rotation='horizontal')
plt.axhline(y=0, color='r', linestyle='-')
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/ESA_EU27_change.png')
plt.show()

# ESA_EEA39_change.plot.bar(
# ylabel="milion hectares", xlabel="year", title="ESA forest area change 1992-2018")
# plt.axhline(y=0, color='r', linestyle='-')
# plt.legend()
# plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/ESA_EEA39_change.png')
# plt.show()

# ESA_core_EEA39_change.plot.bar(
# ylabel="milion hectares", xlabel="year", title="ESA forest area change 1992-2018")
# plt.axhline(y=0, color='r', linestyle='-')
# plt.legend()
# plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/ESA_core_EEA39_change.png')
# plt.show()

ESA_core_EU27_change.plot.bar(
ylabel="milion hectares", xlabel="years", title="ESA change in core forest area in EU27", legend=None)
plt.ylim(bottom=-3, top=3.5)
plt.xticks(rotation='horizontal')
plt.axhline(y=0, color='r', linestyle='-')
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/ESA_core_EU27_change.png')
plt.show()

# ESA_NONcore_EEA39_change.plot.bar(
# ylabel="milion hectares", xlabel="year", title="ESA forest area change 1992-2018")
# plt.axhline(y=0, color='r', linestyle='-')
# plt.legend()
# plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/ESA_NONcore_EEA39_change.png')
# plt.show()

ESA_NONcore_EU27_change.plot.bar(
ylabel="milion hectares", xlabel="years", title="ESA change in non-core forest area in EU27", legend=None)
plt.ylim(bottom=-3, top=3.5)
plt.xticks(rotation='horizontal')
plt.axhline(y=0, color='r', linestyle='-')
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/ESA_NONcore_EU27_change.png')
plt.show()