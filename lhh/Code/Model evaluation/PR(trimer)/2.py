
###
import numpy as np
import os
import pandas as pd

path = '.\\train\\Clustering\\'
files = os.listdir(path)
files_csv = list(filter(lambda x: x[-4:]=='.csv', files))
#print(files_csv)
###
dict={'ALA':'A','ARG':'R','ASN':'N','ASP':'D','CYS':'C','GLN':'Q',
 'GLU':'E','GLY':'G','HIS':'H','ILE':'I','LEU':'L','LYS':'K',
 'MET':'M','PHE':'F','PRO':'P','SER':'S','THR':'T','TRP':'W',
 'TYR':'Y', 'VAL':'V'}
for file in  files_csv:#
    # print(file[0:-4])
    list_tri=[]
    tmp = pd.read_csv(path + file)[['7', '8','9']].values#
    for i in tmp:
        #print(i[1])
        #dataSet.append(i[0])
        A=dict[i[0]]+dict[i[1]]+dict[i[2]]
        list_tri.append(A)

    # list_tri=[]
    #
    # for i in tmp:
    #     for j in i:
    #         list_tri.append(j)
    #
    # #print(list(set(list_tri)))
    list_set=list(set(list_tri))
    #ist_set.append(file[0:-4])
    # # print(list_set)
    test = pd.DataFrame(data=list_set)
    test.to_csv('E:\\DNA\\大修\\审稿人2-4\\cluster(trimer)\\' + file[0:-4] + '.csv', encoding='gbk')
    #
