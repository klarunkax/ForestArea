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
MODIS_Forest = pandas.DataFrame(Modis_Forest)

#1.) sum up all the forest catergories together by years = TOTAL FOREST
total_MODIS_Forest = pandas.DataFrame(MODIS_Forest)
MODIS_2001 = MODIS_Forest.loc[:,MODIS_Forest.columns.str.startswith('2001')]
total_MODIS_Forest['2001'] = MODIS_2001.sum(axis=1)
MODIS_2005 = MODIS_Forest.loc[:,MODIS_Forest.columns.str.startswith('2005')]
total_MODIS_Forest['2005'] = MODIS_2005.sum(axis=1)
MODIS_2006 = MODIS_Forest.loc[:,MODIS_Forest.columns.str.startswith('2006')]
total_MODIS_Forest['2006'] = MODIS_2006.sum(axis=1)
MODIS_2010 = MODIS_Forest.loc[:,MODIS_Forest.columns.str.startswith('2010')]
total_MODIS_Forest['2010'] = MODIS_2010.sum(axis=1)
MODIS_2012 = MODIS_Forest.loc[:,MODIS_Forest.columns.str.startswith('2012')]
total_MODIS_Forest['2012'] = MODIS_2012.sum(axis=1)
MODIS_2015 = MODIS_Forest.loc[:,MODIS_Forest.columns.str.startswith('2015')]
total_MODIS_Forest['2015'] = MODIS_2015.sum(axis=1)
MODIS_2018 = MODIS_Forest.loc[:,MODIS_Forest.columns.str.startswith('2018')]
total_MODIS_Forest['2018'] = MODIS_2018.sum(axis=1)
MODIS_2020 = MODIS_Forest.loc[:,MODIS_Forest.columns.str.startswith('2020')]
total_MODIS_Forest['2020'] = MODIS_2020.sum(axis=1)
#delete forest categories and keep only totals for each year
total_MODIS_Forest = total_MODIS_Forest[['GRID_CODE', 'EEA39', 'EU27', '2001', '2005', '2006', '2010', '2012', '2015', '2018', '2020']]


#delete the country if it has NA for any of the years
# total_MODIS_Forest_EEA39 = total_MODIS_Forest.dropna(axis=0, how='any', subset=['2001', '2005', '2006', '2010', '2012', '2015', '2018', '2020'])
# # A)create total forest for EEA39
# total_MODIS_Forest_EEA39.loc['MODIS_EEA39'] = total_MODIS_Forest_EEA39.sum(numeric_only=True, axis=0)/1000000 #mil. hectares
# MODIS_EEA39 = total_MODIS_Forest_EEA39.loc["MODIS_EEA39"]
# MODIS_EEA39 = MODIS_EEA39.iloc[3:]
# #print(MODIS_EEA39)

# B.)create TOTAL FOREST for EU27
total_MODIS_Forest_EU27 = total_MODIS_Forest.dropna(axis=0, how='any', subset=['2001', '2005', '2006', '2010', '2012', '2015', '2018', '2020'])
total_MODIS_Forest_EU27 = total_MODIS_Forest_EU27[total_MODIS_Forest_EU27["EU27"] == 1]
#print(total_MODIS_Forest_EU27.to_string())
total_MODIS_Forest_EU27.loc['MODIS_EU27'] = total_MODIS_Forest_EU27.sum(numeric_only=True, axis=0)/1000000 #mil. hectares
MODIS_EU27 = total_MODIS_Forest_EU27.loc["MODIS_EU27"]
MODIS_EU27 = MODIS_EU27.iloc[3:]
#print(MODIS_EU27)

# # 2.)sum up categories to create CORE FOREST (all except 22)
total_core_MODIS = pandas.DataFrame(MODIS_Forest)
core_MODIS_Forest = MODIS_Forest.loc[:, ~MODIS_Forest.columns.str.endswith('_22')]
#print(MODIS_Forest.to_string())
core_MODIS_Forest = core_MODIS_Forest.drop(columns="2001") # PROBLEM!
MODIS_2001 = core_MODIS_Forest.loc[:,core_MODIS_Forest.columns.str.startswith('2001')]
total_core_MODIS['2001'] = MODIS_2001.sum(axis=1)
MODIS_2005 = core_MODIS_Forest.loc[:,core_MODIS_Forest.columns.str.startswith('2005')]
total_core_MODIS['2005'] = MODIS_2005.sum(axis=1)
MODIS_2006 = core_MODIS_Forest.loc[:,core_MODIS_Forest.columns.str.startswith('2006')]
total_core_MODIS['2006'] = MODIS_2006.sum(axis=1)
MODIS_2010 = core_MODIS_Forest.loc[:,core_MODIS_Forest.columns.str.startswith('2010')]
total_core_MODIS['2010'] = MODIS_2010.sum(axis=1)
MODIS_2012 = core_MODIS_Forest.loc[:,core_MODIS_Forest.columns.str.startswith('2012')]
total_core_MODIS['2012'] = MODIS_2012.sum(axis=1)
MODIS_2015 = core_MODIS_Forest.loc[:,core_MODIS_Forest.columns.str.startswith('2015')]
total_core_MODIS['2015'] = MODIS_2015.sum(axis=1)
MODIS_2018 = core_MODIS_Forest.loc[:,core_MODIS_Forest.columns.str.startswith('2018')]
total_core_MODIS['2018'] = MODIS_2018.sum(axis=1)
MODIS_2020 = core_MODIS_Forest.loc[:,core_MODIS_Forest.columns.str.startswith('2020')]
total_core_MODIS['2020'] = MODIS_2020.sum(axis=1)

# #delete forest categories and keep only totals for each year
total_core_MODIS = total_core_MODIS[['GRID_CODE', 'EEA39', 'EU27', '2001', '2005', '2006', '2010', '2012','2015', '2018', '2020']]
#print(total_core_MODIS.to_string())
# # # A)create CORE forest for EEA39
# total_core_MODIS_EEA39 = total_core_MODIS.dropna(axis=0, how='any', subset=['2001', '2005', '2006', '2010', '2012','2015', '2018', '2020'])
# total_core_MODIS_EEA39.loc['MODIS_core_EEA39'] = total_core_MODIS_EEA39.sum(numeric_only=True, axis=0)/1000000 #mil. hectares
# #print(total_core_MODIS_EEA39.to_string())
#
# MODIS_core_EEA39 = total_core_MODIS_EEA39.loc["MODIS_core_EEA39"]
# MODIS_core_EEA39 = MODIS_core_EEA39.iloc[3:]
# #print(MODIS_core_EEA39)

# B.)create CORE FOREST for EU27
total_core_MODIS_EU27 = total_core_MODIS.dropna(axis=0, how='any', subset=['2001', '2005', '2006', '2010', '2012', '2015', '2018', '2020'])
total_core_MODIS_EU27 = total_core_MODIS_EU27[total_core_MODIS_EU27["EU27"] == 1]
total_core_MODIS_EU27.loc['MODIS_core_EU27'] = total_core_MODIS_EU27.sum(numeric_only=True, axis=0)/1000000 #mil. hectares
#print(total_core_MODIS_EU27.to_string())
MODIS_core_EU27 = total_core_MODIS_EU27.loc["MODIS_core_EU27"]
MODIS_core_EU27 = MODIS_core_EU27.iloc[3:]
#print(MODIS_core_EU27)

# 3.)sum up categories 22 to create NON CORE FOREST
#print(MODIS_Forest.to_string())

total_NONcore_MODIS = pandas.DataFrame(MODIS_Forest)
NONcore_MODIS_Forest = MODIS_Forest[['GRID_CODE', 'EEA39', 'EU27', '2001_22', '2005_22', '2006_22', '2010_22', '2012_22', '2015_22', '2018_22', '2020_22']]

MODIS_2001 = NONcore_MODIS_Forest.loc[:,NONcore_MODIS_Forest.columns.str.startswith('2001')]
total_NONcore_MODIS['2001'] = MODIS_2001.sum(axis=1)
MODIS_2005 = NONcore_MODIS_Forest.loc[:,NONcore_MODIS_Forest.columns.str.startswith('2005')]
total_NONcore_MODIS['2005'] = MODIS_2005.sum(axis=1)
MODIS_2006 = NONcore_MODIS_Forest.loc[:,NONcore_MODIS_Forest.columns.str.startswith('2006')]
total_NONcore_MODIS['2006'] = MODIS_2006.sum(axis=1)
MODIS_2010 = NONcore_MODIS_Forest.loc[:,NONcore_MODIS_Forest.columns.str.startswith('2010')]
total_NONcore_MODIS['2010'] = MODIS_2010.sum(axis=1)
MODIS_2012 = NONcore_MODIS_Forest.loc[:,NONcore_MODIS_Forest.columns.str.startswith('2012')]
total_NONcore_MODIS['2012'] = MODIS_2012.sum(axis=1)
MODIS_2015 = NONcore_MODIS_Forest.loc[:,NONcore_MODIS_Forest.columns.str.startswith('2015')]
total_NONcore_MODIS['2015'] = MODIS_2015.sum(axis=1)
MODIS_2018 = NONcore_MODIS_Forest.loc[:,NONcore_MODIS_Forest.columns.str.startswith('2018')]
total_NONcore_MODIS['2018'] = MODIS_2018.sum(axis=1)
MODIS_2020 = NONcore_MODIS_Forest.loc[:,NONcore_MODIS_Forest.columns.str.startswith('2020')]
total_NONcore_MODIS['2020'] = MODIS_2020.sum(axis=1)

#delete forest categories and keep only totals for each year
total_NONcore_MODIS = total_NONcore_MODIS[['GRID_CODE', 'EEA39', 'EU27', '2001', '2005', '2006', '2010', '2012', '2015', '2018', '2020']]
#print(total_NONcore_MODIS.to_string())

# # A)create NON-CORE forest for EEA39
# total_NONcore_MODIS_EEA39 = total_NONcore_MODIS.dropna(axis=0, how='any', subset=['1992', '2000', '2005', '2006', '2010', '2012', '2015', '2018', '2020'])
# total_NONcore_MODIS_EEA39.loc['MODIS_NONcore_EEA39'] = total_NONcore_MODIS_EEA39.sum(numeric_only=True, axis=0)/1000000 #mil. hectares
# MODIS_NONcore_EEA39 = total_NONcore_MODIS_EEA39.loc["MODIS_NONcore_EEA39"]
# MODIS_NONcore_EEA39 = MODIS_NONcore_EEA39.iloc[3:]
# #print(MODIS_NONcore_EEA39)

# B.)create NON-CORE FOREST for EU27
total_NONcore_MODIS_EU27 = total_NONcore_MODIS.dropna(axis=0, how='any', subset=['2001', '2005', '2006', '2010', '2012', '2018', '2020'])
total_NONcore_MODIS_EU27 = total_NONcore_MODIS_EU27[total_NONcore_MODIS_EU27["EU27"] == 1]
total_NONcore_MODIS_EU27.loc['MODIS_NONcore_EU27'] = total_NONcore_MODIS_EU27.sum(numeric_only=True, axis=0)/1000000 #mil. hectares
#print(total_core_MODIS_EU27.to_string())
MODIS_NONcore_EU27 = total_NONcore_MODIS_EU27.loc["MODIS_NONcore_EU27"]
MODIS_NONcore_EU27 = MODIS_NONcore_EU27.iloc[3:]
#print(MODIS_NONcore_EU27)

# 4.) Change data
#A) MODIS_EU27 Total CHANGE
MODIS_EU27 = pandas.DataFrame(MODIS_EU27)
MODIS__change_EU27_t = MODIS_EU27.T
MODIS__change_EU27_t["2001-2005"] = MODIS__change_EU27_t["2005"] - MODIS__change_EU27_t["2001"]
MODIS__change_EU27_t["2005-2010"] = MODIS__change_EU27_t["2010"] - MODIS__change_EU27_t["2005"]
MODIS__change_EU27_t["2010-2015"] = MODIS__change_EU27_t["2015"] - MODIS__change_EU27_t["2010"]
MODIS__change_EU27_t["2015-2020"] = MODIS__change_EU27_t["2020"] - MODIS__change_EU27_t["2015"]
MODIS__change_EU27_t = MODIS__change_EU27_t[['2001-2005', '2005-2010', '2010-2015', '2015-2020']]
MODIS_EU27_change = MODIS__change_EU27_t.T
#print(MODIS_EU27_change)

# #  B)MODIS_EEA39 total
# MODIS_EEA39 = pandas.DataFrame(MODIS_EEA39)
# MODIS__change_EU27_t = MODIS_EEA39.T
# MODIS__change_EU27_t["1992-2000"] = MODIS__change_EU27_t["2000"] - MODIS__change_EU27_t["1992"]
# MODIS__change_EU27_t["2000-2005"] = MODIS__change_EU27_t["2005"] - MODIS__change_EU27_t["2000"]
# MODIS__change_EU27_t["2005-2010"] = MODIS__change_EU27_t["2010"] - MODIS__change_EU27_t["2005"]
# MODIS__change_EU27_t["2010-2015"] = MODIS__change_EU27_t["2015"] - MODIS__change_EU27_t["2010"]
# MODIS__change_EU27_t["2015-2020"] = MODIS__change_EU27_t["2020"] - MODIS__change_EU27_t["2015"]
# MODIS__change_EU27_t = MODIS__change_EU27_t[['1992-2000', '2000-2005', '2005-2010', '2010-2015', '2015-2020']]
# MODIS_EEA39_change = MODIS__change_EU27_t.T
# # print(MODIS_EEA39_change)

# # C.) MODIS_core_EEA39 total
# MODIS_core_EEA39 = pandas.DataFrame(MODIS_core_EEA39)
# MODIS__change_EU27_t = MODIS_core_EEA39.T
# MODIS__change_EU27_t["1992-2000"] = MODIS__change_EU27_t["2000"] - MODIS__change_EU27_t["1992"]
# MODIS__change_EU27_t["2000-2005"] = MODIS__change_EU27_t["2005"] - MODIS__change_EU27_t["2000"]
# MODIS__change_EU27_t["2005-2010"] = MODIS__change_EU27_t["2010"] - MODIS__change_EU27_t["2005"]
# MODIS__change_EU27_t["2010-2015"] = MODIS__change_EU27_t["2015"] - MODIS__change_EU27_t["2010"]
# MODIS__change_EU27_t["2015-2020"] = MODIS__change_EU27_t["2020"] - MODIS__change_EU27_t["2015"]
# MODIS__change_EU27_t = MODIS__change_EU27_t[['1992-2000', '2000-2005', '2005-2010', '2010-2015', '2015-2020']]
# MODIS_core_EEA39_change = MODIS__change_EU27_t.T
# # print(MODIS_core_EEA39_change)

# D.) MODIS_core_EU27 ChANGE
MODIS_core_EU27 = pandas.DataFrame(MODIS_core_EU27)
MODIS__change_EU27_t = MODIS_core_EU27.T
MODIS__change_EU27_t["2001-2005"] = MODIS__change_EU27_t["2005"] - MODIS__change_EU27_t["2001"]
MODIS__change_EU27_t["2005-2010"] = MODIS__change_EU27_t["2010"] - MODIS__change_EU27_t["2005"]
MODIS__change_EU27_t["2010-2015"] = MODIS__change_EU27_t["2015"] - MODIS__change_EU27_t["2010"]
MODIS__change_EU27_t["2015-2020"] = MODIS__change_EU27_t["2020"] - MODIS__change_EU27_t["2015"]
MODIS__change_EU27_t = MODIS__change_EU27_t[['2001-2005', '2005-2010', '2010-2015', '2015-2020']]
MODIS_core_EU27_change = MODIS__change_EU27_t.T
#print(MODIS_core_EU27_change)

# # E.) MODIS_NONcore_EEA39 CHANGE
# MODIS_NONcore_EEA39 = pandas.DataFrame(MODIS_NONcore_EEA39)
# MODIS__change_EU27_t = MODIS_NONcore_EEA39.T
# MODIS__change_EU27_t["1992-2000"] = MODIS__change_EU27_t["2000"] - MODIS__change_EU27_t["1992"]
# MODIS__change_EU27_t["2000-2005"] = MODIS__change_EU27_t["2005"] - MODIS__change_EU27_t["2000"]
# MODIS__change_EU27_t["2005-2010"] = MODIS__change_EU27_t["2010"] - MODIS__change_EU27_t["2005"]
# MODIS__change_EU27_t["2010-2015"] = MODIS__change_EU27_t["2015"] - MODIS__change_EU27_t["2010"]
# MODIS__change_EU27_t["2015-2020"] = MODIS__change_EU27_t["2020"] - MODIS__change_EU27_t["2015"]
# MODIS__change_EU27_t = MODIS__change_EU27_t[['1992-2000', '2000-2005', '2005-2010', '2010-2015', '2015-2020']]
# MODIS_NONcore_EEA39_change = MODIS__change_EU27_t.T
# # print(MODIS_NONcore_EEA39_change)

# F.) MODIS_NONcore_EU27 CHANGE
MODIS_NONcore_EU27 = pandas.DataFrame(MODIS_NONcore_EU27)
MODIS__change_EU27_t = MODIS_NONcore_EU27.T
MODIS__change_EU27_t["2001-2005"] = MODIS__change_EU27_t["2005"] - MODIS__change_EU27_t["2001"]
MODIS__change_EU27_t["2005-2010"] = MODIS__change_EU27_t["2010"] - MODIS__change_EU27_t["2005"]
MODIS__change_EU27_t["2010-2015"] = MODIS__change_EU27_t["2015"] - MODIS__change_EU27_t["2010"]
MODIS__change_EU27_t["2015-2020"] = MODIS__change_EU27_t["2020"] - MODIS__change_EU27_t["2015"]
MODIS__change_EU27_t = MODIS__change_EU27_t[['2001-2005', '2005-2010', '2010-2015', '2015-2020']]
MODIS_NONcore_EU27_change = MODIS__change_EU27_t.T
#print(MODIS_NONcore_EU27_change)
#

# 5.) ready data
# MODIS_EU27.index.name='Year'
# MODIS_EU27 = MODIS_EU27.reset_index(level=0)
# print(MODIS_EU27)
#
# MODIS_core_EU27.index.name='Year'
# MODIS_core_EU27 = MODIS_EU27.reset_index(level=0)
# print(MODIS_core_EU27)
#
# MODIS_NONcore_EU27.index.name='Year'
# MODIS_NONcore_EU27 = MODIS_NONcore_EU27.reset_index(level=0)
# print(MODIS_NONcore_EU27)
#
# MODIS_EU27_change.index.name='Year'
# MODIS_EU27_change = MODIS_EU27_change.reset_index(level=0)
# print(MODIS_EU27_change)
#
# MODIS_core_EU27_change.index.name='Year'
# MODIS_core_EU27_change = MODIS_core_EU27_change.reset_index(level=0)
# print(MODIS_core_EU27_change)
#
sum_MODIS_EU27 = pandas.concat([MODIS_EU27, MODIS_core_EU27, MODIS_NONcore_EU27], axis=1, join="inner")
sum_MODIS_EU27.to_csv('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/sum_tables/sum_MODIS_EU27.csv')
print(sum_MODIS_EU27)

change_MODIS_EU27 = pandas.concat([MODIS_EU27_change, MODIS_core_EU27_change, MODIS_NONcore_EU27_change], axis=1, join="inner")
change_MODIS_EU27.to_csv('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/sum_tables/change_MODIS_EU27.csv')
#print(change_MODIS_EU27)7_change = MODIS_NONcore_EU27_change.reset_index(level=0)
print(MODIS_NONcore_EU27_change)


# #
# # 6.) plot charts
# MODIS_EEA39.plot.bar(
# ylabel="milion hectares", xlabel="year", title="MODIS forest area 1992-2018 ")
# plt.legend()
# plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/MODIS_EEA39.png')
# plt.show()
# #

MODIS_EU27.plot.bar(
ylabel="milion hectares", xlabel="year", title="MODIS total forest area in EU27", legend=None)
plt.ylim(bottom=0, top=250)
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/MODIS_EU27_v2.png')
plt.show()
#
# # MODIS_core_EEA39.plot.bar(
# # ylabel="milion hectares", xlabel="year", title="MODIS forest area 1992-2018")
# # plt.legend()
# # plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/MODIS_core_EEA39.png')
# # plt.show()
# #
MODIS_core_EU27.plot.bar(
ylabel="milion hectares", xlabel="year", title="MODIS core forest area in EU27", legend=None)
plt.ylim(bottom=0, top=250)
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/MODIS_core_EU27_v2.png')
plt.show()
# #
# # MODIS_NONcore_EEA39.plot.bar(
# # ylabel="milion hectares", xlabel="year", title="MODIS forest area 1992-2018")
# # plt.legend()
# # plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/MODIS_NONcore_EEA39.png')
# # plt.show()
# #
#
MODIS_NONcore_EU27.plot.bar(
ylabel="milion hectares", xlabel="years", title="MODIS non-core forest area in EU27", legend=None)
plt.ylim(bottom=0, top=250)
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/MODIS_NONcore_EU27_v2.png')
plt.show()
# #
# # #


MODIS_EU27_change.plot.bar(
ylabel="milion hectares", xlabel="Years", title="MODIS change in total forest area in EU27", legend=None)
plt.ylim(bottom=-4, top=6)
plt.xticks(rotation='horizontal')
plt.axhline(y=0, color='r', linestyle='-')
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/MODIS_EU27_change_v2.png')
plt.show()

# MODIS_EEA39_change.plot.bar(
# ylabel="milion hectares", xlabel="year", title="MODIS forest area change 1992-2018")
# plt.axhline(y=0, color='r', linestyle='-')
# plt.legend()
# plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/MODIS_EEA39_change.png')
# plt.show()

# MODIS_core_EEA39_change.plot.bar(
# ylabel="milion hectares", xlabel="year", title="MODIS forest area change 1992-2018")
# plt.axhline(y=0, color='r', linestyle='-')
# plt.legend()
# plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/MODIS_core_EEA39_change.png')
# plt.show()

MODIS_core_EU27_change.plot.bar(
ylabel="milion hectares", xlabel="years", title="MODIS change in core forest area in EU27", legend=None)
plt.ylim(bottom=-4, top=6)
plt.xticks(rotation='horizontal')
plt.axhline(y=0, color='r', linestyle='-')
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/MODIS_core_EU27_change_v2.png')
plt.show()

# MODIS_NONcore_EEA39_change.plot.bar(
# ylabel="milion hectares", xlabel="year", title="MODIS forest area change 1992-2018")
# plt.axhline(y=0, color='r', linestyle='-')
# plt.legend()
# plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/MODIS_NONcore_EEA39_change.png')
# plt.show()

MODIS_NONcore_EU27_change.plot.bar(
ylabel="milion hectares", xlabel="years", title="MODIS change in non-core forest area in EU27", legend=None)
plt.ylim(bottom=-4, top=6)
plt.xticks(rotation='horizontal')
plt.axhline(y=0, color='r', linestyle='-')
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/MODIS_NONcore_EU27_change_v2.png')
plt.show()