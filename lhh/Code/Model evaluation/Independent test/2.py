# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 16:33:14 2018

@author: Administrator
"""
import os
path = '.\\test\\Binding site\\'
pathID = os.listdir(path)
for ID in pathID:
    path_site = path + '\\' + ID + '\\' + 'site.txt'
    file3 = open(path_site, 'r+')
    list_w = []
    path1 = path + '\\' + ID + '\\' + 'site1.txt'
    f = open(path1, "w")
    for line in file3.readlines():
        AMI = line.split()[9]
        if AMI == 'ALA' or AMI == 'ARG' or AMI == 'ASN' or AMI == 'ASP' or AMI == 'CYS' or AMI == 'GLN' \
                or AMI == 'GLU' or AMI == 'GLY' or AMI == 'HIS' \
                or AMI == 'ILE' or AMI == 'LEU' or AMI == 'LYS' or AMI == 'MET' or AMI == 'PHE' or AMI == 'PRO' or AMI == 'SER' or AMI == 'THR' or AMI == 'TRP' or AMI == 'TYR' or AMI == 'VAL':
            f.write(line)

    f.close()