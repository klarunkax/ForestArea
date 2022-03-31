import pandas
import os
import csv
import matplotlib.pyplot as plt
import numpy as np


os.chdir('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_tables')

CLC_Forest = pandas.read_csv('CLC_Forest_v2.csv')
COP_Forest = pandas.read_csv('COP_Forest_v01.csv')
ESA_Forest = pandas.read_csv('ESA_Forest_v2.csv')
Modis_Forest = pandas.read_csv('modis_forest_v1.csv')


CLC_Forest = pandas.DataFrame(CLC_Forest)
COP_Forest = pandas.DataFrame(COP_Forest)
ESA_Forest = pandas.DataFrame(ESA_Forest)
Modis_Forest = pandas.DataFrame(Modis_Forest)


# CLC = pandas.DataFrame(columns = ['1990', '2000', '2006', '2012', '2018'])
CLC_Forest['1990'] = CLC_Forest['1990BLF'] + CLC_Forest['1990CF'] + CLC_Forest['1990MF'] + CLC_Forest['1990TWS']
CLC_Forest['2000'] = CLC_Forest['2000BLF'] + CLC_Forest['2000CF'] + CLC_Forest['2000MF'] + CLC_Forest['2000TWS']
CLC_Forest['2006'] = CLC_Forest['2006BLF'] + CLC_Forest['2006CF'] + CLC_Forest['2006MF'] + CLC_Forest['2006TWS']
CLC_Forest['2012'] = CLC_Forest['2012BLF'] + CLC_Forest['2012CF'] + CLC_Forest['2012MF'] + CLC_Forest['2012TWS']
CLC_Forest['2018'] = CLC_Forest['2018BLF'] + CLC_Forest['2018CF'] + CLC_Forest['2018MF'] + CLC_Forest['2018TWS']
CLC_Forest = CLC_Forest.drop(columns=['1990BLF', '1990CF', '1990MF', '1990TWS', '1990F',
                             '2000BLF', '2000CF', '2000MF', '2000TWS', '2000F',
                             '2006BLF', '2006CF', '2006MF', '2006TWS', '2006F',
                             '2012BLF', '2012CF', '2012MF', '2012TWS', '2012F',
                             '2018BLF', '2018CF', '2018MF', '2018TWS', '2018F'])

CLC_Forest.loc['CLC_EEA39'] = CLC_Forest.sum(numeric_only=True, axis=0)
CLC_EEA39 = CLC_Forest
CLC_EEA39 = CLC_EEA39[CLC_EEA39["EEA39"] == 39]
CLC_EEA39 = CLC_EEA39.drop(CLC_EEA39.columns[[0, 1, 2, 3, 4, 5, 6]], axis = 1)

CLC_EU27 = CLC_Forest[CLC_Forest["EU27"] == 1]
CLC_EU27.loc['CLC_EU27'] = CLC_EU27.sum(numeric_only=True, axis=0)
CLC_EU27 = CLC_EU27[CLC_EU27["EU27"] == 27]
CLC_EU27 = CLC_EU27.drop(CLC_EU27.columns[[0, 1, 2, 3, 4, 5, 6]], axis = 1)

print(CLC_EEA39.to_string())
print(CLC_EU27.to_string())

# CLC_EEA39.plot(
#     x="year", y="area", title="CLC forest area in EEA39 1990-2018 in hectares"
# )
# plt.show()




# print(COP_Forest)
# print(ESA_Forest)
# print(Modis_Forest)
