# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 10:06:59 2018

@author: Administrator
"""
import numpy as np
import os
import pandas as pd
import pylab as pl
import difflib
#####Hydrophobic analysis

#Hydrophobic index(ftp://ftp.genome.jp/pub/db/community/aaindex/aaindex1)
dict_Hyd={'ALA':0.61,'LEU':1.53,'ARG':0.60,'LYS':1.15,'ASN':0.06,\
      'MET':1.18,'ASP':0.46,'PHE':2.02,'CYS':1.07, 'PRO':1.95,\
      'GLN':0, 'SER':0.05,'GLU':0.47,'THR':0.05,'GLY':0.07,\
      'TRP':2.65, 'HIS':0.61,'TYR':1.88,'ILE':2.22,'VAL':1.32}
#Electron-ion interaction potential values
dict_Ele={'ALA':0.037,'LEU':0,'ARG':0.0959,'LYS':0.0371,'ASN':0.0036,\
      'MET':0.0823,'ASP':0.1263,'PHE':0.0946,'CYS':0.0829, 'PRO':0.0198,\
      'GLN':0.0761, 'SER':0.0829,'GLU':0.0058,'THR':0.0941,'GLY':0.0050,\
      'TRP':0.0548, 'HIS':0.0242,'TYR':0.0516,'ILE':0,'VAL':0.0057}
#charge
dict_Cha={'ALA':0,'LEU':0,'ARG':1,'LYS':1,'ASN':1,\
      'MET':1,'ASP':-1,'PHE':0,'CYS':0, 'PRO':0,\
      'GLN':0, 'SER':0,'GLU':-1,'THR':0,'GLY':0,\
      'TRP':0, 'HIS':0,'TYR':0,'ILE':0,'VAL':0}\
#Average accessible surface area
dict_Ave={'ALA':27.8,'LEU':27.6,'ARG':94.7,'LYS':103.0,'ASN':60.1,\
      'MET':33.5,'ASP':60.6,'PHE':25.5,'CYS':15.5, 'PRO':51.5,\
      'GLN':68.7, 'SER':42.0,'GLU':68.2,'THR':45.0,'GLY':24.50,\
      'TRP':34.70, 'HIS':50.70,'TYR':55.20,'ILE':22.80,'VAL':33.70}
###
###
path = '.\\train\\Clustering\\'
files = os.listdir(path)
files_csv = list(filter(lambda x: x[-4:]=='.csv', files))
#print(files_csv)
###
List=[]
List_sort=[]
j=0
for file in  files_csv:#
    #print(file)
    tmp = pd.read_csv(path + file)[['7', '8','9']]#
    #print(tmp)
    #print(type(tmp))

    LIst=[]
    for ide in tmp.index:
        AMI=tmp.loc[ide].values
        LIst.append((dict_Hyd[AMI[0]] + dict_Hyd[AMI[2]] + dict_Hyd[AMI[1]]))
    sum=0

    for i in LIst:
        sum+=i
    List.append(sum/len(LIst))

    List_sort.append([sum/len(LIst),file])
    j+=1

x=[]
for i in range(len(List)):
    x.append(i)
print(List)
print(len(List))
ListSort=np.sort(List)

L = sorted(List_sort, key=lambda s: s[0])
print(L)

X=[]
Y=[]
for i in L:
    X.append(i[0])
    Y.append(str(i[1]))
print(X)
# test = pd.DataFrame(data=X)
# path1 = 'F:\\DNA Binding protein\\SW.csv'
# test.to_csv(path1, encoding='gbk')

print((X[len(X)-1]-X[0])/2)
Av=(X[len(X)-1]-X[0])/2
F=0
for i in range(len(X)-1):
    if X[i]<=Av<=X[i+1]:
        print(Y[i])
        F = Y[i]
        break
loc=Y.index(F)
print(loc)
path_rea='.\\train\\Drug-cluster association data\\data.csv'
reader = pd.read_csv(path_rea)
rea=[]
for i in reader.iloc[:,1]:
    b=str(i)+'.csv'
    rea.append(b)
print(rea)
n=0

for i in Y[0:loc]:
    for j in rea:
        if i == j:
            n+=1
print(n/len(rea))
print(1-n/len(rea))