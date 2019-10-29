#####
#####
####
dict={'ALA':'A','ARG':'R','ASN':'N','ASP':'D','CYS':'C','GLN':'Q',
 'GLU':'E','GLY':'G','HIS':'H','ILE':'I','LEU':'L','LYS':'K',
 'MET':'M','PHE':'F','PRO':'P','SER':'S','THR':'T','TRP':'W',
 'TYR':'Y', 'VAL':'V'}
import pandas as pd
import os
import re

path_ID = '.\\test\\Trimer\\'
file_ID =  os.listdir(path_ID)
path_JA = '.\\prediction\\CN.csv'
CN_pre = pd.read_csv(path_JA)[['0','1']].values
path_clu = '.\\train\\Clustering\\'
file_clu =  os.listdir(path_clu)
N = 0
for ID in file_ID:
    list_clu=[]
    list_pre=[]
    path_drug = path_ID + '\\' + ID + '\\' + 'drug.csv'
    path_Tri = path_ID + '\\' + ID + '\\' + 'piece3.csv'
    path_id = path_ID + '\\' + ID + '\\' + 'ID.csv'
    F = open(path_drug)
    G = open(path_Tri)
    H = open(path_id)
    drug = pd.read_csv(F)['drug'].values
    trimer = pd.read_csv(G)['0'].values
    PDB = pd.read_csv(H)['ID'].values

    for i in CN_pre[0:10000]:
        if i[1]==drug[0]:
            list_clu.append(i[0])
        ####
    # print(list_clu)
    for file in list_clu:
        clu = pd.read_csv(path_clu + str(file)+'.csv')[['7', '8', '9']].values
        for i in clu:
            A = dict[i[0]] + dict[i[1]] + dict[i[2]]


            list_pre.append(A)
    # print(list_pre)
    # print(trimer)
    num=0
    for i in trimer:
        if i in list_pre:
            num+=1

    if 0.8<num / len(trimer) <=1:
        N+=1
        print(PDB[0])
        print(drug[0])
        # print(len(trimer))
        # print(num)
        print(num / len(trimer))
print(N)






