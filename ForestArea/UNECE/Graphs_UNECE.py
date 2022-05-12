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
UNECE_Forest = UNECE_Forest[UNECE_Forest['country'] != 'Malta']
UNECE_Forest = UNECE_Forest[UNECE_Forest["EU"] == 1]
print(UNECE_Forest.to_string())

#core forest
UNECE_EU27_Forest = UNECE_Forest.iloc[:, 2:8]
UNECE_EU27_Forest = UNECE_EU27_Forest.rename(columns={"Forest - 2020 ( 1000 ha )": "2020", "Forest - 2015 ( 1000 ha )": "2015", "Forest - 2010 ( 1000 ha )": "2010", "Forest - 2005 ( 1000 ha )": "2005", "Forest - 2000 ( 1000 ha )": "2000", "Forest - 1990 ( 1000 ha )": "1990"})
print(UNECE_EU27_Forest.to_string())
UNECE_EU27_Forest.loc['UNECE_EU27_Forest'] = UNECE_EU27_Forest.sum(numeric_only=True, axis=0)/1000 #mil. hectares
UNECE_EU27_Forest = UNECE_EU27_Forest.loc["UNECE_EU27_Forest"]
UNECE_EU27_Forest = UNECE_EU27_Forest.sort_index()
print(UNECE_EU27_Forest)

#TOTAL FOREST

UNECE_EU27_ForestAndOWL = UNECE_Forest.iloc[:, 14:20]
UNECE_EU27_ForestAndOWL = UNECE_EU27_ForestAndOWL.rename(columns={"Total forest and OWL - 2020 ( 1000 ha )": "2020", "Total forest and OWL - 2015 ( 1000 ha )": "2015", "Total forest and OWL - 2010 ( 1000 ha )": "2010", "Total forest and OWL - 2005 ( 1000 ha )": "2005", "Total forest and OWL - 2000 ( 1000 ha )": "2000", "Total forest and OWL - 1990 ( 1000 ha )": "1990"})
print(UNECE_EU27_ForestAndOWL.to_string())
UNECE_EU27_ForestAndOWL.loc['UNECE_EU27_ForestAndOWL'] = UNECE_EU27_ForestAndOWL.sum(numeric_only=True, axis=0)/1000 #mil. hectares
UNECE_EU27_ForestAndOWL = UNECE_EU27_ForestAndOWL.loc["UNECE_EU27_ForestAndOWL"]
UNECE_EU27_ForestAndOWL = UNECE_EU27_ForestAndOWL.sort_index()
print(UNECE_EU27_ForestAndOWL)

#NON CORE FOREST

UNECE_EU27_OWL = UNECE_Forest.iloc[:, 8:14]
UNECE_EU27_OWL = UNECE_EU27_OWL.rename(columns={"OWL - 2020 ( 1000 ha )": "2020", "OWL - 2015 ( 1000 ha )": "2015", "OWL - 2010 ( 1000 ha )": "2010", "OWL - 2005 ( 1000 ha )": "2005", "OWL - 2000 ( 1000 ha )": "2000", "OWL - 1990 ( 1000 ha )": "1990"})
print(UNECE_EU27_OWL.to_string())
UNECE_EU27_OWL.loc['UNECE_EU27_OWL'] = UNECE_EU27_OWL.sum(numeric_only=True, axis=0)/1000 #mil. hectares
UNECE_EU27_OWL = UNECE_EU27_OWL.loc["UNECE_EU27_OWL"]
UNECE_EU27_OWL = UNECE_EU27_OWL.sort_index()
print(UNECE_EU27_OWL)

#
# # 4.) Change data
# #A) UNECE_EU27_ForestAndOWL Total CHANGE
UNECE_EU27_ForestAndOWL = pandas.DataFrame(UNECE_EU27_ForestAndOWL)
UNECE_change_EU27_t = UNECE_EU27_ForestAndOWL.T
UNECE_change_EU27_t["1990-2000"] = UNECE_change_EU27_t["2000"] - UNECE_change_EU27_t["1990"]
UNECE_change_EU27_t["2000-2005"] = UNECE_change_EU27_t["2005"] - UNECE_change_EU27_t["2000"]
UNECE_change_EU27_t["2005-2010"] = UNECE_change_EU27_t["2010"] - UNECE_change_EU27_t["2005"]
UNECE_change_EU27_t["2010-2015"] = UNECE_change_EU27_t["2015"] - UNECE_change_EU27_t["2010"]
UNECE_change_EU27_t["2015-2020"] = UNECE_change_EU27_t["2020"] - UNECE_change_EU27_t["2015"]
UNECE_change_EU27_t = UNECE_change_EU27_t[['1990-2000', '2000-2005', '2005-2010', '2010-2015', '2015-2020']]
UNECE_EU27_ForestAndOWL_change = UNECE_change_EU27_t.T
print(UNECE_EU27_ForestAndOWL_change)

#
# # D.) UNECE_EU27_Forest ChANGE
UNECE_EU27_Forest = pandas.DataFrame(UNECE_EU27_Forest)
UNECE_change_EU27_t = UNECE_EU27_Forest.T
UNECE_change_EU27_t["1990-2000"] = UNECE_change_EU27_t["2000"] - UNECE_change_EU27_t["1990"]
UNECE_change_EU27_t["2000-2005"] = UNECE_change_EU27_t["2005"] - UNECE_change_EU27_t["2000"]
UNECE_change_EU27_t["2005-2010"] = UNECE_change_EU27_t["2010"] - UNECE_change_EU27_t["2005"]
UNECE_change_EU27_t["2010-2015"] = UNECE_change_EU27_t["2015"] - UNECE_change_EU27_t["2010"]
UNECE_change_EU27_t["2015-2020"] = UNECE_change_EU27_t["2020"] - UNECE_change_EU27_t["2015"]
UNECE_change_EU27_t = UNECE_change_EU27_t[['1990-2000', '2000-2005', '2005-2010', '2010-2015', '2015-2020']]
UNECE_EU27_Forest_change = UNECE_change_EU27_t.T
print(UNECE_EU27_Forest_change)
#
#
#
# # F.) UNECE_EU27_OWL CHANGE
UNECE_EU27_OWL = pandas.DataFrame(UNECE_EU27_OWL)
UNECE_change_EU27_t = UNECE_EU27_OWL.T
UNECE_change_EU27_t["1990-2000"] = UNECE_change_EU27_t["2000"] - UNECE_change_EU27_t["1990"]
UNECE_change_EU27_t["2000-2005"] = UNECE_change_EU27_t["2005"] - UNECE_change_EU27_t["2000"]
UNECE_change_EU27_t["2005-2010"] = UNECE_change_EU27_t["2010"] - UNECE_change_EU27_t["2005"]
UNECE_change_EU27_t["2010-2015"] = UNECE_change_EU27_t["2015"] - UNECE_change_EU27_t["2010"]
UNECE_change_EU27_t["2015-2020"] = UNECE_change_EU27_t["2020"] - UNECE_change_EU27_t["2015"]
UNECE_change_EU27_t = UNECE_change_EU27_t[['1990-2000', '2000-2005', '2005-2010', '2010-2015', '2015-2020']]
UNECE_EU27_OWL_change = UNECE_change_EU27_t.T
print(UNECE_EU27_OWL_change)
# #
# # 5.) ready data
#
sum_UNECE_EU27_ForestAndOWL = pandas.concat([UNECE_EU27_ForestAndOWL, UNECE_EU27_Forest, UNECE_EU27_OWL], axis=1, join="inner")
sum_UNECE_EU27_ForestAndOWL.to_csv('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/sum_tables/sum_UNECE_EU27.csv')
print(sum_UNECE_EU27_ForestAndOWL)
#
change_UNECE_EU27_ForestAndOWL = pandas.concat([UNECE_EU27_ForestAndOWL_change, UNECE_EU27_Forest_change, UNECE_EU27_OWL_change], axis=1, join="inner")
change_UNECE_EU27_ForestAndOWL.to_csv('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/sum_tables/change_UNECE_EU27.csv')
# #print(change_UNECE_EU27_ForestAndOWL)7_change = UNECE_EU27_OWL_change.reset_index(level=0)

#
#
# # #
# # # 6.) plot charts
#
UNECE_EU27_ForestAndOWL.plot.bar(
ylabel="milion hectares", xlabel="year", title="UNECE Forest+Other wooded land in EU27", legend=None)
plt.ylim(bottom=0, top=200)
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/UNECE_EU27_ForestAndOWL.png')
plt.show()
#

UNECE_EU27_Forest.plot.bar(
ylabel="milion hectares", xlabel="year", title="UNECE Forest in EU27", legend=None)
plt.ylim(bottom=0, top=200)
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/UNECE_EU27_Forest.png')
plt.show()
# #

UNECE_EU27_OWL.plot.bar(
ylabel="milion hectares", xlabel="years", title="Other wooded land in EU27", legend=None)
plt.ylim(bottom=0, top=200)
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/UNECE_EU27_OWL.png')
plt.show()
# #
# # #


UNECE_EU27_ForestAndOWL_change.plot.bar(
ylabel="milion hectares", xlabel="Years", title="UNECE change in Forest + Other wooded land in EU27", legend=None)
plt.ylim(bottom=-4, top=7)
plt.xticks(rotation='horizontal')
plt.axhline(y=0, color='r', linestyle='-')
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/UNECE_EU27_ForestAndOWL_change.png')
plt.show()

UNECE_EU27_Forest_change.plot.bar(
ylabel="milion hectares", xlabel="years", title="UNECE change in Forest in EU27", legend=None)
plt.ylim(bottom=-4, top=7)
plt.xticks(rotation='horizontal')
plt.axhline(y=0, color='r', linestyle='-')
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/UNECE_EU27_Forest_change.png')
plt.show()

UNECE_EU27_OWL_change.plot.bar(
ylabel="milion hectares", xlabel="years", title="UNECE change in Other wooded land in EU27", legend=None)
plt.ylim(bottom=-4, top=7)
plt.xticks(rotation='horizontal')
plt.axhline(y=0, color='r', linestyle='-')
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/UNECE_EU27_OWL_change.png')
plt.show()