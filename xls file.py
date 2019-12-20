# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 15:27:45 2019

@author: carj
"""
import pandas as pd
data=r"C:\\Users\\carj\\Desktop\\AU00_LHZA_P3_BS_X out of 1 - Copy.xls"
print ("Starting...")
datafile=pd.read_excel(data, sep= 'delimiter',encoding='ISO-8859-1', error_bad_lines=False,skiprows= 5)
print("reading the xls file....")
df=pd.DataFrame(datafile)
print("creating dataframe....")
writer= pd.ExcelWriter(r"C:\\Users\\carj\\Desktop\\aaa.xlsx")
print("writing the sheet...")
df.to_excel(writer, index=False)
print ("creating the excel sheet...")
writer.save()
writer.close()
