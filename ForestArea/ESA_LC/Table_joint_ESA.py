import pandas
from simpledbf import Dbf5
import os
import csv

os.chdir('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/ESA_LC/output')

Countries_CODES = pandas.read_csv('Countries extended CODES_eea.csv')
ESA_Forest = pandas.DataFrame(Countries_CODES)

table_dbfs = [f for f in os.listdir('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/ESA_LC/output') if f.endswith('.dbf') and not(f.endswith(".tif.vat.dbf"))]

for table_dbf in table_dbfs:
    size = len(table_dbf)     #count number of the letters in the name
    table_name = table_dbf[:size - 4] #create a name for the table - deleting last four characters
    table = Dbf5(table_dbf)      #load data from the dbf to the table
    table_df = table.to_dataframe() #create a dataframe

    table_df = table_df.rename(columns={'SUM': table_name})  # rename a column SUM  for first 7 letters from the table name
    table_df = table_df.drop(columns=['COUNT', 'AREA'])  # delete columns COUNT a AREA
    table_df = table_df.rename(columns={'Value': 'GRID_CODE'})

    ESA_Forest = ESA_Forest.merge(table_df, how='left', on="GRID_CODE")

print(ESA_Forest)

# #EXPORT CSV
ESA_Forest.to_csv('C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/ESA_LC/output/ESA_Forest.csv')