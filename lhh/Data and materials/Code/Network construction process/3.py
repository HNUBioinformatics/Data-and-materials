# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 10:13:06 2018

@author: Administrator
"""
#####binding sites are joined in sequence to form a
# binding site sequence and saved in site.csv
import os
import pandas as pd
import re
path = '.\\train\\Binding site'
pathID =  os.listdir(path)
i = 1
base = '.\\train\\Trimer'
for j in range(len(pathID)):
        file_name = base+str(i)
        os.mkdir(file_name)
        i=i+1
j=1
for ID in pathID:
        #print(ID)
        #len(pathID)
        list_0=[]
        list_pdbid=[]
        path_drug = path+'\\'+ID+'\\'+'drug.txt'
        path_ligand = path+'\\'+ID+'\\'+'ligand.txt'
        path_site = path+'\\'+ID+'\\'+'site1.txt'
       
        file1=open(path_drug, 'r+')
        content1 = file1.read()
        #print(content1)
        drugname=re.search('_(.*?)_',content1).group(1)
        #print(drugname)
        pdbid=re.search('(.*?)_',content1).group(1)
        
        list_0.append(str(drugname))
        list_pdbid.append(pdbid)
        
        name=['drug']
        test=pd.DataFrame(columns=name,data=list_0)
        path1  = base+str(j)+'\\'+'drug.csv'
        test.to_csv(path1,encoding='gbk')
        
        name=['ID']
        test=pd.DataFrame(columns=name,data=list_pdbid)
        path1  = base+str(j)+'\\'+'ID.csv'
        test.to_csv(path1,encoding='gbk')

        list_1=[]
        list_2=[]
        list_3=[]
        list_4=[]
        list_5=[]
        list_6=[]
        list_7=[]
        file2=open(path_ligand, 'r+')
        for line in file2.readlines():
            #print(line)
            ATOM=line.split()[1]
            FUN=line.split()[5]
            list_1.append(ATOM)
            list_2.append(FUN)
        for i in range(len(list_1)):
            list_3.append([list_1[i],list_2[i]])
        print(list_3)
        print(list_1)
        print(list_2)
        name=['one','two']
        test=pd.DataFrame(columns=name,data=list_3)
        path2  = base+str(j)+'\\'+'ligand.csv'
        test.to_csv(path2,encoding='gbk')
        file3=open(path_site, 'r+')
        for line in file3.readlines():
            #print(line)
            AMI=line.split()[9]
            CHA=line.split()[10]
            LOC=int(line[-5:])#在site1.txt文件中解决链号与链挨着的问题   
            #LOC=line.split()[11]
            list_4.append(AMI)
            list_5.append(CHA)
            list_6.append(LOC)
        print(list_4)
        print(list_5)
        print(list_6)
        for i in range(len(list_4)):
            list_7.append([list_4[i],list_5[i],list_6[i]])
        print(list_7)
        name=['one','two','three']
        test=pd.DataFrame(columns=name,data=list_7)
        path3  = base+str(j)+'\\'+'site.csv'
        test.to_csv(path3,encoding='gbk')
        j+=1







