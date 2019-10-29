# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 10:06:59 2018

@author: Administrator
"""
#Summarize all vectorized trimers and save them in "All.csv"

import csv 
import os
import pandas as pd

path = '.\\train\\Trimer'
pathID =  os.listdir(path)
list_1=[]
list_2=[]

for ID in pathID:
    path_site = path+'\\'+ID+'\\'+'cha3.csv'
    csv_file=open(path_site)   
    csv_reader_lines = csv.reader(csv_file)
    list_1=[]
    for one_line in csv_reader_lines:
        del one_line[0]
        list_1.append(one_line)
        #del list_1[0][0]
    del list_1[0]
    #print(list_1)
    
    for i in list_1:
        if i[0] !='0.0':
            list_2.append(i)
print(list_2)


test=pd.DataFrame(data=list_2)
path1  = '.\\Vectorization of trimers\\All.csv'
test.to_csv(path1,encoding='gbk')