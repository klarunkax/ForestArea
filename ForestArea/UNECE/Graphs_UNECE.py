import pandas
import os
import csv
import matplotlib.pyplot as plt
import numpy as np


os.chdir('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_tables')
#load the statistics
UNECE_Forest = pandas.read_csv('UNECE_forestArea v2.csv')
#put the stats into dataframes
UNECE_Forest = pandas.DataFrame(UNECE_Forest)
#delete Poland and Hungary where we miss OWL
UNECE_Forest.rename(columns={ UNECE_Forest.columns[0]: "country" }, inplace = True)
UNECE_Forest = UNECE_Forest[UNECE_Forest['country'] != 'Hungary']
UNECE_Forest = UNECE_Forest[UNECE_Forest['country'] != 'Poland']
UNECE_Forest = UNECE_Forest[UNECE_Forest['country'] != 'Malta']
UNECE_Forest = UNECE_Forest[UNECE_Forest["EU"] == 1]
print(UNECE_Forest.to_string())

#core forest
UNECE_core_EU25 = UNECE_Forest.iloc[:, 2:8]
UNECE_core_EU25 = UNECE_core_EU25.rename(columns={"Forest - 2020 ( 1000 ha )": "2020", "Forest - 2015 ( 1000 ha )": "2015", "Forest - 2010 ( 1000 ha )": "2010", "Forest - 2005 ( 1000 ha )": "2005", "Forest - 2000 ( 1000 ha )": "2000", "Forest - 1990 ( 1000 ha )": "1990"})
print(UNECE_core_EU25.to_string())
UNECE_core_EU25.loc['UNECE_core_EU25'] = UNECE_core_EU25.sum(numeric_only=True, axis=0)/1000 #mil. hectares
UNECE_core_EU25 = UNECE_core_EU25.loc["UNECE_core_EU25"]
UNECE_core_EU25 = UNECE_core_EU25.sort_index()
print(UNECE_core_EU25)

#TOTAL FOREST

UNECE_EU25 = UNECE_Forest.iloc[:, 14:20]
UNECE_EU25 = UNECE_EU25.rename(columns={"Total forest and OWL - 2020 ( 1000 ha )": "2020", "Total forest and OWL - 2015 ( 1000 ha )": "2015", "Total forest and OWL - 2010 ( 1000 ha )": "2010", "Total forest and OWL - 2005 ( 1000 ha )": "2005", "Total forest and OWL - 2000 ( 1000 ha )": "2000", "Total forest and OWL - 1990 ( 1000 ha )": "1990"})
print(UNECE_EU25.to_string())
UNECE_EU25.loc['UNECE_EU25'] = UNECE_EU25.sum(numeric_only=True, axis=0)/1000 #mil. hectares
UNECE_EU25 = UNECE_EU25.loc["UNECE_EU25"]
UNECE_EU25 = UNECE_EU25.sort_index()
print(UNECE_EU25)

#NON CORE FOREST

UNECE_NONcore_EU25 = UNECE_Forest.iloc[:, 8:14]
UNECE_NONcore_EU25 = UNECE_NONcore_EU25.rename(columns={"OWL - 2020 ( 1000 ha )": "2020", "OWL - 2015 ( 1000 ha )": "2015", "OWL - 2010 ( 1000 ha )": "2010", "OWL - 2005 ( 1000 ha )": "2005", "OWL - 2000 ( 1000 ha )": "2000", "OWL - 1990 ( 1000 ha )": "1990"})
print(UNECE_NONcore_EU25.to_string())
UNECE_NONcore_EU25.loc['UNECE_NONcore_EU25'] = UNECE_NONcore_EU25.sum(numeric_only=True, axis=0)/1000 #mil. hectares
UNECE_NONcore_EU25 = UNECE_NONcore_EU25.loc["UNECE_NONcore_EU25"]
UNECE_NONcore_EU25 = UNECE_NONcore_EU25.sort_index()
print(UNECE_NONcore_EU25)

#
# # 4.) Change data
# #A) UNECE_EU25 Total CHANGE
UNECE_EU25 = pandas.DataFrame(UNECE_EU25)
UNECE_change_EU25_t = UNECE_EU25.T
UNECE_change_EU25_t["1990-2000"] = UNECE_change_EU25_t["2000"] - UNECE_change_EU25_t["1990"]
UNECE_change_EU25_t["2000-2005"] = UNECE_change_EU25_t["2005"] - UNECE_change_EU25_t["2000"]
UNECE_change_EU25_t["2005-2010"] = UNECE_change_EU25_t["2010"] - UNECE_change_EU25_t["2005"]
UNECE_change_EU25_t["2010-2015"] = UNECE_change_EU25_t["2015"] - UNECE_change_EU25_t["2010"]
UNECE_change_EU25_t["2015-2020"] = UNECE_change_EU25_t["2020"] - UNECE_change_EU25_t["2015"]
UNECE_change_EU25_t = UNECE_change_EU25_t[['1990-2000', '2000-2005', '2005-2010', '2010-2015', '2015-2020']]
UNECE_EU25_change = UNECE_change_EU25_t.T
print(UNECE_EU25_change)

#
# # D.) UNECE_core_EU25 ChANGE
UNECE_core_EU25 = pandas.DataFrame(UNECE_core_EU25)
UNECE_change_EU25_t = UNECE_core_EU25.T
UNECE_change_EU25_t["1990-2000"] = UNECE_change_EU25_t["2000"] - UNECE_change_EU25_t["1990"]
UNECE_change_EU25_t["2000-2005"] = UNECE_change_EU25_t["2005"] - UNECE_change_EU25_t["2000"]
UNECE_change_EU25_t["2005-2010"] = UNECE_change_EU25_t["2010"] - UNECE_change_EU25_t["2005"]
UNECE_change_EU25_t["2010-2015"] = UNECE_change_EU25_t["2015"] - UNECE_change_EU25_t["2010"]
UNECE_change_EU25_t["2015-2020"] = UNECE_change_EU25_t["2020"] - UNECE_change_EU25_t["2015"]
UNECE_change_EU25_t = UNECE_change_EU25_t[['1990-2000', '2000-2005', '2005-2010', '2010-2015', '2015-2020']]
UNECE_core_EU25_change = UNECE_change_EU25_t.T
print(UNECE_core_EU25_change)
#
#
#
# # F.) UNECE_NONcore_EU25 CHANGE
UNECE_NONcore_EU25 = pandas.DataFrame(UNECE_NONcore_EU25)
UNECE_change_EU25_t = UNECE_NONcore_EU25.T
UNECE_change_EU25_t["1990-2000"] = UNECE_change_EU25_t["2000"] - UNECE_change_EU25_t["1990"]
UNECE_change_EU25_t["2000-2005"] = UNECE_change_EU25_t["2005"] - UNECE_change_EU25_t["2000"]
UNECE_change_EU25_t["2005-2010"] = UNECE_change_EU25_t["2010"] - UNECE_change_EU25_t["2005"]
UNECE_change_EU25_t["2010-2015"] = UNECE_change_EU25_t["2015"] - UNECE_change_EU25_t["2010"]
UNECE_change_EU25_t["2015-2020"] = UNECE_change_EU25_t["2020"] - UNECE_change_EU25_t["2015"]
UNECE_change_EU25_t = UNECE_change_EU25_t[['1990-2000', '2000-2005', '2005-2010', '2010-2015', '2015-2020']]
UNECE_NONcore_EU25_change = UNECE_change_EU25_t.T
print(UNECE_NONcore_EU25_change)
# #
# # 5.) ready data
#
sum_UNECE_EU25 = pandas.concat([UNECE_EU25, UNECE_core_EU25, UNECE_NONcore_EU25], axis=1, join="inner")
sum_UNECE_EU25.to_csv('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/sum_tables/sum_UNECE_EU25.csv')
print(sum_UNECE_EU25)
#
change_UNECE_EU25 = pandas.concat([UNECE_EU25_change, UNECE_core_EU25_change, UNECE_NONcore_EU25_change], axis=1, join="inner")
change_UNECE_EU25.to_csv('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/sum_tables/change_UNECE_EU25.csv')
# #print(change_UNECE_EU25)7_change = UNECE_NONcore_EU25_change.reset_index(level=0)

#
#
# # #
# # # 6.) plot charts
#
UNECE_EU25.plot.bar(
ylabel="milion hectares", xlabel="year", title="UNECE Forest+Other wooded land in EU25", legend=None)
plt.ylim(bottom=0, top=180)
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/UNECE_EU25.png')
plt.show()
#

UNECE_core_EU25.plot.bar(
ylabel="milion hectares", xlabel="year", title="UNECE Forest in EU25", legend=None)
plt.ylim(bottom=0, top=180)
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/UNECE_core_EU25.png')
plt.show()
# #

UNECE_NONcore_EU25.plot.bar(
ylabel="milion hectares", xlabel="years", title="Other wooded land in EU25", legend=None)
plt.ylim(bottom=0, top=180)
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/UNECE_NONcore_EU25.png')
plt.show()
# #
# # #


UNECE_EU25_change.plot.bar(
ylabel="milion hectares", xlabel="Years", title="UNECE change in Forest + Other wooded land in EU25", legend=None)
plt.ylim(bottom=-4, top=7)
plt.xticks(rotation='horizontal')
plt.axhline(y=0, color='r', linestyle='-')
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/UNECE_EU25_change.png')
plt.show()

UNECE_core_EU25_change.plot.bar(
ylabel="milion hectares", xlabel="years", title="UNECE change in Forest in EU25", legend=None)
plt.ylim(bottom=-4, top=7)
plt.xticks(rotation='horizontal')
plt.axhline(y=0, color='r', linestyle='-')
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/UNECE_core_EU25_change.png')
plt.show()

UNECE_NONcore_EU25_change.plot.bar(
ylabel="milion hectares", xlabel="years", title="UNECE change in Other wooded land in EU25", legend=None)
plt.ylim(bottom=-4, top=7)
plt.xticks(rotation='horizontal')
plt.axhline(y=0, color='r', linestyle='-')
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/UNECE_NONcore_EU25_change.png')
plt.show()