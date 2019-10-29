# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 17:00:06 2018

@author: Administrator
"""
##The binding sites in "site.csv" are separated by 3 sliding windows and saved in "piece.csv"
import csv
import os
import pandas as pd
path = '.\\train\\Trimer'
pathID =  os.listdir(path)
n=0
for ID in pathID:
    path_site = path+'\\'+ID+'\\'+'site.csv'
    csv_file=open(path_site)
    csv_reader_lines = csv.reader(csv_file)
    data=[]
    data1=[]
    data2=[]

    for one_line in csv_reader_lines:
        data.append(one_line)
    for i in data:
        data1.append(i[1])
    del data1[0]
    print(data1)
    n+len(data1)
    list_piece=[]
    list_trimer = []
    for i in range(len(data1)):
        if len(data1)>=(i+3):
            list_piece.append(data1[i:i+3])
    test=pd.DataFrame(data=list_piece)
    path1  = path+'\\'+ID+'\\'+'piece3.csv'
    test.to_csv(path1,encoding='gbk')
print(n)