import pandas
import os
import csv
import matplotlib.pyplot as plt
import numpy as np
os.chdir('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/sum_tables')
sum_CLC_EU27 = pandas.read_csv('sum_CLC_EU27.csv')
change_CLC_EU27 = pandas.read_csv('change_CLC_EU27.csv')
sum_COP_EU27 = pandas.read_csv('sum_COP_EU27.csv')
change_COP_EU27 = pandas.read_csv('change_COP_EU27.csv')
sum_ESA_EU27 = pandas.read_csv('sum_ESA_EU27.csv')
change_ESA_EU27 = pandas.read_csv('change_ESA_EU27.csv')
sum_MODIS_EU27 = pandas.read_csv('sum_MODIS_EU27.csv')
change_MODIS_EU27 = pandas.read_csv('change_MODIS_EU27.csv')
sum_UNECE_EU27 = pandas.read_csv('sum_UNECE_EU27.csv')
change_UNECE_EU27 = pandas.read_csv('change_UNECE_EU27.csv')

sum_key_table = pandas.concat([sum_CLC_EU27, sum_COP_EU27, sum_ESA_EU27, sum_MODIS_EU27, sum_UNECE_EU27], axis=1)
sum_key_table.to_csv('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/sum_tables/sum_key_table.csv')
change_key_table = pandas.concat([change_CLC_EU27, change_COP_EU27, change_ESA_EU27, change_MODIS_EU27, change_UNECE_EU27], axis=1)
change_key_table.to_csv('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/sum_tables/change_key_table.csv')


