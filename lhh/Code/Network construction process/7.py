# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 09:51:01 2018

@author: Administrator
"""
##Clustering

import pandas as pd
import math
def dist(a, b):
#    return math.sqrt(math.pow(a[0][0]-b[0][0], 2)+math.pow(a[0][1]-b[0][1], 2)\
#+math.pow(a[0][2]-b[0][2], 2))#First three properties
    return math.sqrt(math.pow(a[0][0]-b[0][0], 2)+math.pow(a[0][1]-b[0][1], 2)\
+math.pow(a[0][2]-b[0][2], 2)+math.pow(a[0][3]-b[0][3], 2)+math.pow(a[0][4]-b[0][4], 2)\
)#Top five properties

#dist_min
def dist_min(Ci, Cj):
    return min(dist(i, j) for i in Ci for j in Cj)
#dist_max
def dist_max(Ci, Cj):
    return max(dist(i, j) for i in Ci for j in Cj)

def find_Min(M):  #Find the subscript with the smallest distance
    min = 100000000#Set an arbitrary large number
    x = 0; y = 0
    for i in range(len(M)):
        for j in range(len(M[i])):
            if i != j and M[i][j] < min:#Find the minimum of i, j not equal
                min = M[i][j];x = i; y = j
    return (x, y, min)
def turappend(site,x,y,D):
    x1=x[0]
    y1=y[0]
    if len(x)>1:
        x1=x[0]
    if len(y) > 1:
        y1 = y[0]
    site.append([D.index(x1),D.index(y1)])
    return site

#Algorithm model：
def AGNES(dataset,k):
    #Initialize C and M
    C = [];M = [];D=[];site=[]#c is the storage data, m is the storage distance
    for i in dataset:#Add the data in the dataset to c
        Ci = []
        Ci.append(i)
        D.append(i)
        C.append(Ci)
    for i in C:#Calculated distance
        Mi = []#Store the distance of each line
        for j in C:
            Mi.append(dist(i, j))#Calculate the distance between two points i, j
        M.append(Mi)#Add the distance of each line
    q = len(dataset)#Initialize q
    #Merge update
    while q > k:
        x, y, min = find_Min(M)#Find the minimum distance
        site=turappend(site,C[x],C[y],D)
        C[x]=C[x]+C[y]#Combine two points into one family
        C.remove(C[y])#Delete the point corresponding to y
        M = []
        for i in C:#Recalculate the distance, that is,
            # delete the row and column corresponding to point y
            Mi = []
            for j in C:
                Mi.append(dist(i, j))
            M.append(Mi)
        q -= 1
    return C,site
if __name__ == '__main__':
    file = open(',\\train\\Vectorization of trimers\\All.csv', 'r')
    pf = pd.read_csv(file)
    file.close()
    dataset = []
    for i in range(pf.shape[0]):
        dataset.append([round(float(pf.iloc[i,1]),3), round(float(pf.iloc[i,2]),3),\
round(float(pf.iloc[i,3]),3),round(float(pf.iloc[i,4]),3),round(float(pf.iloc[i,5]),3),pf.iloc[i,6],pf.iloc[i,7],pf.iloc[i,8],pf.iloc[i,9],pf.iloc[i,10]])
        #Convert and keep 3 decimal places in the dataset
    #print(dataset)
    C ,site= AGNES(dataset, 97)#Computing hierarchical clustering

    for i in range(len(C)):
        print((i+1),'---',C[i])
        da=C[i]
        print(da)
        test=pd.DataFrame(data=da)
        path1  = '.\\train\\Clustering\\'+str(i)+'.csv'
        test.to_csv(path1,encoding='gbk')
