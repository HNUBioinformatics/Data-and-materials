# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 21:39:26 2018
@
@author: Administrator
"""
####Save the drug name and binding site in the “Binding site”
import os
path = '.\\train\\DNA binding protein'
pathID = os.listdir(path)
i = 1
base = '.\\train\\Binding site'
for j in range(len(pathID)):
    file_name = base + str(i)
    os.mkdir(file_name)
    i = i + 1
########
########
j = 1
for ID in pathID:
    path_ligand = path + '\\' + ID + '\\' + 'ligand.mol2'
    path_site = path + '\\' + ID + '\\' + 'site.mol2'

    file1 = open(path_ligand, 'r+')
    content1 = file1.read()
    list_content1 = content1.split('@')

    file2 = open(path_site, 'r+')
    content2 = file2.read()
    list_content2 = content2.split('@')
    # print(list_content2[4][20:])

    path_ligand_new1 = base + str(j) + '\\' + 'drug.txt'
    file3 = open(path_ligand_new1, 'w')
    file3.write(list_content1[1][17:])
    file3.close()

    path_ligand_new1 = base + str(j) + '\\' + 'ligand.txt'
    file4 = open(path_ligand_new1, 'w')
    file4.write(list_content1[2][13:])
    file4.close()

    path_site_new1 = base + str(j) + '\\' + 'site.txt'
    file5 = open(path_site_new1, 'w')
    file5.write(list_content2[4][21:])
    file5.close()
    j += 1