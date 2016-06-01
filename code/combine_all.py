import os
import glob
import csv
import xlwt
import pandas
fileList=glob.glob("*.csv")
dfList=[]
for filename in fileList:
    print(filename)
    df=pandas.read_csv(filename)
    colnames=['University','Name','Info','Email']
    dfList.append(df)
concatDf=pandas.concat(dfList,axis=0)
concatDf.columns=colnames
concatDf.to_csv("FinalOutput.csv",index=None)





