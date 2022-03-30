import pandas
import os
import csv
import matplotlib.pyplot as plt

os.chdir('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/output_tables')

CLC_Forest = pandas.read_csv('CLC_Forest_v2.csv')
COP_Forest = pandas.read_csv('COP_Forest_v01.csv')
ESA_Forest = pandas.read_csv('ESA_Forest_v2.csv')
Modis_Forest = pandas.read_csv('modis_forest_v1.csv')

CLC_Forest = pandas.DataFrame(CLC_Forest)
COP_Forest = pandas.DataFrame(COP_Forest)
ESA_Forest = pandas.DataFrame(ESA_Forest)
Modis_Forest = pandas.DataFrame(Modis_Forest)