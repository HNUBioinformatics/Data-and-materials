
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 15:05:07 2018

@author: Administrator
"""
# Trimers are vectorized according to five
# physical and chemical properties

import math 
import csv 
import os
import pandas as pd
path = '.\\train\\Trimer'
pathID =  os.listdir(path)
for ID in pathID:
    path_site = path+'\\'+ID+'\\'+'piece3.csv'
    path_drug = path+'\\'+ID+'\\'+'drug.csv'
    path_ID = path+'\\'+ID+'\\'+'ID.csv'
    
    csv_file=open(path_site)   
    csv_reader_lines = csv.reader(csv_file)
    
    reader = pd.read_csv(path_drug)
    for i in reader.iloc[:,1]:
        drug=i

    reader_ID = pd.read_csv(path_ID)
    for j in reader_ID.iloc[:,1]:
        Id=j
        
    data=[]
    list_1=[]
    for one_line in csv_reader_lines:
        #print(one_line)
        data.append(one_line)
    del data[0]
    print(data)
    
    for one_line in data:
        print(one_line)
        
        E1=1961.504
        E2=788.2
        E3=539.776
        E4=276.624
        E5=244.106
        T=0
        D=0
        M=0
        N=0
        Q=0
        LIST=[]
        for Ami in one_line:
            #print(Ami)
            if Ami=='ALA':            
                [λ1,λ2,λ3,λ4,λ5]=[0.008,0.134,-0.475,-0.039,0.181]
                
                T=math.sqrt(E1)*λ1
                D=math.sqrt(E2)*λ2
                M=math.sqrt(E3)*λ3
                N=math.sqrt(E4)*λ4
                Q=math.sqrt(E5)*λ5
            if Ami=='ARG':
                [λ1,λ2,λ3,λ4,λ5]=[0.171,-0.361,0.107,-0.258,-0.364]
                
                T=math.sqrt(E1)*λ1
                D=math.sqrt(E2)*λ2
                M=math.sqrt(E3)*λ3
                N=math.sqrt(E4)*λ4
                Q=math.sqrt(E5)*λ5
                
            if Ami=='ASN':
                [λ1,λ2,λ3,λ4,λ5]=[0.255,0.038,0.117,0.118,-0.055]
                
                T3=math.sqrt(E1)*λ1
                D3=math.sqrt(E2)*λ2
                M3=math.sqrt(E3)*λ3
                N3=math.sqrt(E4)*λ4
                Q3=math.sqrt(E5)*λ5
                
            if Ami=='ASP':
                [λ1,λ2,λ3,λ4,λ5]=[0.303,-0.057,-0.014,0.225,0.156]
                
                T=math.sqrt(E1)*λ1
                D=math.sqrt(E2)*λ2
                M=math.sqrt(E3)*λ3
                N=math.sqrt(E4)*λ4
                Q=math.sqrt(E5)*λ5
                
            if Ami=='CYS':
                [λ1,λ2,λ3,λ4,λ5]=[-0.132,0.174,0.07,0.565,-0.374]
                
                T=math.sqrt(E1)*λ1
                D=math.sqrt(E2)*λ2
                M=math.sqrt(E3)*λ3
                N=math.sqrt(E4)*λ4
                Q=math.sqrt(E5)*λ5
                
            if Ami=='GLN':
                [λ1,λ2,λ3,λ4,λ5]=[0.149,-0.184,-0.03,0.035,-0.112]
                T=math.sqrt(E1)*λ1
                D=math.sqrt(E2)*λ2
                M=math.sqrt(E3)*λ3
                N=math.sqrt(E4)*λ4
                Q=math.sqrt(E5)*λ5
                
            if Ami=='GLU':
                [λ1,λ2,λ3,λ4,λ5]=[0.221,-0.28,-0.315,0.157,0.303]
                T=math.sqrt(E1)*λ1
                D=math.sqrt(E2)*λ2
                M=math.sqrt(E3)*λ3
                N=math.sqrt(E4)*λ4
                Q=math.sqrt(E5)*λ5
                
            if Ami=='GLY':
                [λ1,λ2,λ3,λ4,λ5]=[0.218,0.562,-0.024,0.018,0.106]
                T=math.sqrt(E1)*λ1
                D=math.sqrt(E2)*λ2
                M=math.sqrt(E3)*λ3
                N=math.sqrt(E4)*λ4
                Q=math.sqrt(E5)*λ5
                
            if Ami=='HIS':
                [λ1,λ2,λ3,λ4,λ5]=[0.023,-0.177,0.041,0.28,-0.021]
                T=math.sqrt(E1)*λ1
                D=math.sqrt(E2)*λ2
                M=math.sqrt(E3)*λ3
                N=math.sqrt(E4)*λ4
                Q=math.sqrt(E5)*λ5
                
            if Ami=='ILE':
                [λ1,λ2,λ3,λ4,λ5]=[-0.353,0.071,-0.088,-0.195,-0.107]
                T=math.sqrt(E1)*λ1
                D=math.sqrt(E2)*λ2
                M=math.sqrt(E3)*λ3
                N=math.sqrt(E4)*λ4
                Q=math.sqrt(E5)*λ5
                
            if Ami=='LEU':
                [λ1,λ2,λ3,λ4,λ5]=[-0.267,0.018,-0.265,-0.274,0.206]
                T=math.sqrt(E1)*λ1
                D=math.sqrt(E2)*λ2
                M=math.sqrt(E3)*λ3
                N=math.sqrt(E4)*λ4
                Q=math.sqrt(E5)*λ5
                
            if Ami=='LYS':
                [λ1,λ2,λ3,λ4,λ5]=[0.243,-0.339,-0.044,-0.325,-0.027]
                T=math.sqrt(E1)*λ1
                D=math.sqrt(E2)*λ2
                M=math.sqrt(E3)*λ3
                N=math.sqrt(E4)*λ4
                Q=math.sqrt(E5)*λ5
                
            if Ami=='MET':
                [λ1,λ2,λ3,λ4,λ5]=[-0.239,-0.141,-0.155,0.321,0.077]
                T=math.sqrt(E1)*λ1
                D=math.sqrt(E2)*λ2
                M=math.sqrt(E3)*λ3
                N=math.sqrt(E4)*λ4
                Q=math.sqrt(E5)*λ5
                
            if Ami=='PHE':
                [λ1,λ2,λ3,λ4,λ5]=[-0.329,-0.023,0.072,-0.002,0.208]
                T=math.sqrt(E1)*λ1
                D=math.sqrt(E2)*λ2
                M=math.sqrt(E3)*λ3
                N=math.sqrt(E4)*λ4
                Q=math.sqrt(E5)*λ5
                
            if Ami=='PRO':
                [λ1,λ2,λ3,λ4,λ5]=[0.173,0.286,0.407,-0.215,0.384]
                T=math.sqrt(E1)*λ1
                D=math.sqrt(E2)*λ2
                M=math.sqrt(E3)*λ3
                N=math.sqrt(E4)*λ4
                Q=math.sqrt(E5)*λ5
                
            if Ami=='SER':
                [λ1,λ2,λ3,λ4,λ5]=[0.199,0.238,-0.015,-0.068,-0.196]
                T=math.sqrt(E1)*λ1
                D=math.sqrt(E2)*λ2
                M=math.sqrt(E3)*λ3
                N=math.sqrt(E4)*λ4
                Q=math.sqrt(E5)*λ5
                
            if Ami=='THR':
                [λ1,λ2,λ3,λ4,λ5]=[0.068,0.147,-0.015,-0.132,-0.274]
                T=math.sqrt(E1)*λ1
                D=math.sqrt(E2)*λ2
                M=math.sqrt(E3)*λ3
                N=math.sqrt(E4)*λ4
                Q=math.sqrt(E5)*λ5
                
            if Ami=='TRP':
                [λ1,λ2,λ3,λ4,λ5]=[-0.296,-0.186,0.389,0.083,0.297]
                T=math.sqrt(E1)*λ1
                D=math.sqrt(E2)*λ2
                M=math.sqrt(E3)*λ3
                N=math.sqrt(E4)*λ4
                Q=math.sqrt(E5)*λ5
                
            if Ami=='TYR':
                [λ1,λ2,λ3,λ4,λ5]=[-0.141,-0.057,0.425,-0.096,-0.091]
                T=math.sqrt(E1)*λ1
                D=math.sqrt(E2)*λ2
                M=math.sqrt(E3)*λ3
                N=math.sqrt(E4)*λ4
                Q=math.sqrt(E5)*λ5
                
            if Ami=='VAL':
                [λ1,λ2,λ3,λ4,λ5]=[-0.274,0.136,-0.187,-0.196,-0.299]
                T=math.sqrt(E1)*λ1
                D=math.sqrt(E2)*λ2
                M=math.sqrt(E3)*λ3
                N=math.sqrt(E4)*λ4
                Q=math.sqrt(E5)*λ5
                
            LIST.append([T,D,M,N,Q])
        T=LIST[1][0]+LIST[0][0]/2+LIST[2][0]/4
        D=LIST[1][1]+LIST[0][1]/2+LIST[2][1]/4
        M=LIST[1][2]+LIST[0][2]/2+LIST[2][2]/4
        N=LIST[1][3]+LIST[0][3]/2+LIST[2][3]/4
        Q=LIST[1][4]+LIST[0][4]/2+LIST[2][4]/4
        list_1.append([T,D,M,N,Q,drug,Id,one_line[1],one_line[2],one_line[3]])
    print(list_1)
    
    
    test=pd.DataFrame(data=list_1)
    path1  = path+'\\'+ID+'\\'+'cha3.csv'
    test.to_csv(path1,encoding='gbk')

                
            
            
            

            
