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

CLC_Forest_CF = CLC_Forest
CLC_Forest_NCF = CLC_Forest

# All categories together
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

# separate CF a NCF
CLC_Forest_CF['1990'] = CLC_Forest_CF['1990BLF'] + CLC_Forest_CF['1990CF'] + CLC_Forest_CF['1990MF']
CLC_Forest_CF['2000'] = CLC_Forest_CF['2000BLF'] + CLC_Forest_CF['2000CF'] + CLC_Forest_CF['2000MF']
CLC_Forest_CF['2006'] = CLC_Forest_CF['2006BLF'] + CLC_Forest_CF['2006CF'] + CLC_Forest_CF['2006MF']
CLC_Forest_CF['2012'] = CLC_Forest_CF['2012BLF'] + CLC_Forest_CF['2012CF'] + CLC_Forest_CF['2012MF']
CLC_Forest_CF['2018'] = CLC_Forest_CF['2018BLF'] + CLC_Forest_CF['2018CF'] + CLC_Forest_CF['2018MF']
CLC_Forest_CF = CLC_Forest_CF.drop(columns=['1990BLF', '1990CF', '1990MF', '1990TWS', '1990F',
                             '2000BLF', '2000CF', '2000MF', '2000TWS', '2000F',
                             '2006BLF', '2006CF', '2006MF', '2006TWS', '2006F',
                             '2012BLF', '2012CF', '2012MF', '2012TWS', '2012F',
                             '2018BLF', '2018CF', '2018MF', '2018TWS', '2018F'])

CLC_Forest_NCF['1990'] = CLC_Forest_NCF['1990MF']
CLC_Forest_NCF['2000'] = CLC_Forest_NCF['2000MF']
CLC_Forest_NCF['2006'] = CLC_Forest_NCF['2006MF']
CLC_Forest_NCF['2012'] = CLC_Forest_NCF['2012MF']
CLC_Forest_NCF['2018'] = CLC_Forest_NCF['2018MF']
CLC_Forest_NCF = CLC_Forest_NCF.drop(columns=['1990BLF', '1990CF', '1990MF', '1990TWS', '1990F',
                             '2000BLF', '2000CF', '2000MF', '2000TWS', '2000F',
                             '2006BLF', '2006CF', '2006MF', '2006TWS', '2006F',
                             '2012BLF', '2012CF', '2012MF', '2012TWS', '2012F',
                             '2018BLF', '2018CF', '2018MF', '2018TWS', '2018F'])


CLC_Forest_1 = CLC_Forest.dropna(axis=0, how='any', subset=['1990', '2000', '2006', '2012', '2018'])
CLC_Forest_1.loc['CLC_EEA39'] = CLC_Forest_1.sum(numeric_only=True, axis=0)/1000000 #mil. hectares
CLC_EEA39 = CLC_Forest_1.loc["CLC_EEA39"]
CLC_EEA39 = CLC_EEA39.iloc[7:]
print(CLC_EEA39)

CLC_Forest_2 = CLC_Forest.dropna(axis=0, how='any', subset=['1990', '2000', '2006', '2012', '2018'])
CLC_Forest_2 = CLC_Forest_2[CLC_Forest_2["EU27"] == 1]
CLC_Forest_2.loc['CLC_EU24'] = CLC_Forest_2.sum(numeric_only=True, axis=0)/1000000 #mil. hectares
CLC_EU24 = CLC_Forest_2.loc["CLC_EU24"]
CLC_EU24 = CLC_EU24.iloc[7:]
print(CLC_EU24)


#CLC_Forest_2 = CLC_Forest.dropna(axis=0, how='any', subset=['1990', '2000', '2006', '2012', '2018'])
CLC_Forest_3 = CLC_Forest[CLC_Forest["EU27"] == 1]
CLC_Forest_3.loc['CLC_EU27'] = CLC_Forest_3.sum(numeric_only=True, axis=0)/1000000 #mil. hectares
CLC_EU27 = CLC_Forest_3.loc["CLC_EU27"]
CLC_EU27 = CLC_EU27.iloc[8:]
print(CLC_EU27)
# #
CLC_Forest_CF = CLC_Forest_CF.dropna(axis=0, how='any', subset=['1990', '2000', '2006', '2012', '2018'])
CLC_Forest_CF = CLC_Forest_CF[CLC_Forest_CF["EU27"] == 1]
CLC_Forest_CF.loc['CLC_EU24'] = CLC_Forest_CF.sum(numeric_only=True, axis=0)/1000000 #mil. hectares
CLC_CF_EU24 = CLC_Forest_CF.loc["CLC_EU24"]
CLC_CF_EU24 = CLC_CF_EU24.iloc[7:]
print(CLC_CF_EU24)



#print(CLC_EEA39.to_string())
# print(CLC_EU27.to_string())

# CLC_EEA39.plot(
# ylabel="milion hectares", xlabel="year", title="CLC forest area in EEA39 1990-2018 ")
# plt.legend()
# plt.show()

CLC_EU27.plot(
ylabel="milion hectares", xlabel="year", title="CLC forest area 2000-2018")
plt.legend()
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/CLC_EU27.png')
plt.show()

CLC_EU24.plot(
ylabel="milion hectares", xlabel="year", title="CLC forest area 1990-2018")
plt.legend()
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/CLC_EU24.png')
plt.show()

CLC_CF_EU24.plot(
ylabel="milion hectares", xlabel="year", title="CLC forest area 1990-2018", label = "CLC_CF_EU24")
plt.legend()
plt.savefig('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_charts/CLC_CF_EU24.png')
plt.show()
