# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 17:00:06 2018

@author: Administrator
"""
import csv
import os
import pandas as pd
dict={'ALA':'A','ARG':'R','ASN':'N','ASP':'D','CYS':'C','GLN':'Q',
 'GLU':'E','GLY':'G','HIS':'H','ILE':'I','LEU':'L','LYS':'K',
 'MET':'M','PHE':'F','PRO':'P','SER':'S','THR':'T','TRP':'W',
 'TYR':'Y', 'VAL':'V'}
path = '.\\test\\Trimer\\'
pathID = os.listdir(path)
for ID in pathID:
    DICT=[]
    path_site = path + '\\' + ID + '\\' + 'site.csv'
    csv_file = open(path_site)
    csv_reader_lines = csv.reader(csv_file)
    data = []
    data1 = []
    data2 = []

    for one_line in csv_reader_lines:
        data.append(one_line)


    for i in data:
        data1.append(i[1])

    del data1[0]

    print(data1)

    list_piece = []
    for i in range(len(data1)):
        if len(data1) >= (i + 3):
            list_piece.append(data1[i:i + 3])

    print(list_piece)
    for i in list_piece:
        #print(i)
        #dataSet.append(i[0])
        A=dict[i[0]]+dict[i[1]]+dict[i[2]]
        DICT.append(A)
    print(DICT)
    test = pd.DataFrame(data=DICT)
    path1 = path + '\\' + ID + '\\' + 'piece3.csv'
    test.to_csv(path1, encoding='gbk')
#