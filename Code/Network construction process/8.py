# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 17:31:55 2018

@author: Administrator
"""

#Cluster-drug association data
import os
import pandas as pd
path = '.\\train\\Clustering'
pathID =  os.listdir(path)

list_1=[]
for ID in pathID:
    path_1 = path+'\\'+ID
    reader = pd.read_csv(path_1)
    list_drug=[]
    for i in reader.iloc[:,6]:
        list_drug.append(i)
    b=list(set(list_drug))
    #print(b)
    for h in b:
        list_1.append([ID[:-4],h])
#print(list_1)
test=pd.DataFrame(data=list_1)
path1  = '.\\train\\Drug-cluster association data\\data.csv'
test.to_csv(path1,encoding='gbk')



    