# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 11:21:24 2018

@author: Administrator
"""
import numpy as np
import pandas as pd
import pylab as pl
import random
import matplotlib.pyplot as plt
list_key_allCNR=[]
list_key_allCNP=[]
list_key_allCNr=[]
list_key_allCNp=[]
list_key_allCNtpr=[]
list_key_allCNfpr=[]
list_key_allCNTPR=[]
list_key_allCNFPR=[]
list_key_allJAR=[]
list_key_allJAP=[]
list_key_allJAr=[]
list_key_allJAp=[]
list_key_allJAtpr=[]
list_key_allJAfpr=[]
list_key_allJATPR=[]
list_key_allJAFPR=[]

list_key_allPAR=[]
list_key_allPAP=[]
list_key_allPAr=[]
list_key_allPAp=[]
list_key_allPAtpr=[]
list_key_allPAfpr=[]
list_key_allPATPR=[]
list_key_allPAFPR=[]
F1_cn = []
F1_ja = []
F1_pa = []
Sensitive_cn=[]
Sensitive_ja=[]
Sensitive_pa=[]
specificity_cn=[]
specificity_ja=[]
specificity_pa=[]
path = '.\\train\\Drug-cluster association data\\data.csv'
reader = pd.read_csv(path)

dict1 = {}
num = 0
for i in reader.iloc[:, 1]:
    if i not in list(dict1.keys()):
        dict1[i] = num
        num += 1

dict2 = {}
num = 0
for i in reader.iloc[:, 2]:
    if i not in list(dict2.keys()):
        dict2[i] = num
        num += 1

num = 0
dataset = []
while num < len(reader.iloc[:, 2]):
    dataset.append([dict1[reader.iloc[num, 1]], dict2[reader.iloc[num, 2]]])
    num += 1
# print(dataset)

list2 = []
list3 = []
list4 = []
list5 = []
for i in dataset:
    list2.append(i[0])  #
    list3.append(i[1])  #
# print(np.sort(list2))
# print(np.sort(list3))
#
list4 = np.sort(list2)
list5 = np.sort(list3)
A = len(list4)
B = len(list5)
M = list4[A - 1] + 1
N = list5[B - 1] + 1

Dataset1 = []


list_all_PR = []
list_all_PR_2 = []
list_all_PR_PA = []

for H in range(10):
    test = random.sample(dataset, 217)
    test_pos = pd.DataFrame(data=test)
    test_pos.to_csv('E:\\DNA\\大修\\审稿人2-4\\Positive\\'+str(H)+'.csv', encoding='gbk')

    # print(test)
    ###

    list_test = []
    list_test_1 = []
    list_test_2 = []
    list_test_3 = []

###
    for i in test:
        list_test_1.append(i[0])
        list_test_2.append(i[1])
    list_test_1 = list(set(list_test_1))
    list_test_2 = list(set(list_test_2))
    for i in list_test_1:
        for j in list_test_2:
            list_test_3.append([i, j])
    # print(list_test_3)
    # list_4=set(list_3)-set(test)
    for i in test:
        if i in list_test_3:
            list_test_3.remove(i)
            # print(list_test_3)
    # print(len(list_test_3))
####

    Test = []
    for i in test:
        Test.append([i, 1])
    ###


    data_neg=random.sample(list_test_3,214)
    test_neg = pd.DataFrame(data=data_neg)
    test_neg.to_csv('E:\\DNA\\大修\\审稿人2-4\\Negative\\'+str(H) + '.csv', encoding='gbk')

    for j in data_neg:
        Test.append([j, 0])
    #print(len(Test))
    ###

    train = []
    for i in dataset:
        if i not in test:
            train.append(i)

    matrix_1 = np.zeros((M, N))
    for i in train:  #
        matrix_1[i[0], i[1]] = 1
    # print(matrix_1)
    # print(matrix_1.shape)
    ##


    matrix_2 = np.zeros((M, N))  #
    matrix_3 = np.zeros((M, N))
    matrix_PA = np.zeros((M, N))

    cn = 0
    d = 0
    d1 = 0
    d2 = 0
    for i in range(M):  #
        print('number %d is running\n', i)
        for j in range(N):  #
            if matrix_1[i, j] == 0:  #
                list_x = matrix_1[i]  #
                list_y = matrix_1[:, j]  #
                for l in range(len(list_y)):
                    if list_y[l] == 1:
                        d1 += 1
                # print(list_x)
                # print(list_y)
                for h in range(len(list_x)):  #
                    if list_x[h] == 1:
                        d += 1

                        list_z = matrix_1[:, h]

                        for K in range(M):
                            if list_z[K] == 1:
                                d2 += 1
                            if list_y[K] * list_z[K] == 1:
                                cn = cn + 1  #
                matrix_2[i, j] = cn
                #
                if (d1 + d2 - d) != 0:
                    matrix_3[i, j] = cn / (d1 + d2 - d - cn)
                #
                matrix_PA[i, j] = (d1 * d)
                #

                d = 0
                cn = 0
                d1 = 0
                d2 = 0

    list_all_CN = []
    list_all_JA = []
    list_all_PA = []

    for i in range(matrix_2.shape[0]):  #
        for j in range(matrix_2.shape[1]):  #
            if matrix_2[i][j] != 0:
                list_all_CN.append([matrix_2[i,j],[i,j]])  #
    list_sort_CN = sorted(list_all_CN, key=lambda s: s[0], reverse=True)
    for i in range(matrix_3.shape[0]):
        for j in range(matrix_3.shape[1]):
            if matrix_3[i][j] != 0:
                list_all_JA.append([matrix_3[i,j],[i,j]])
    list_sort_JA = sorted(list_all_JA, key=lambda s: s[0], reverse=True)

    for i in range(matrix_PA.shape[0]):
        for j in range(matrix_PA.shape[1]):
            if matrix_PA[i][j] != 0:
                list_all_PA.append([matrix_PA[i,j],[i,j]])
    list_sort_PA = sorted(list_all_PA, key=lambda s: s[0], reverse=True)

    list_CNPr=[]
    list_JAPr=[]
    list_PAPr = []
    for i in list_sort_CN[0:5000]:
        list_CNPr.append(i[1])
    for i in list_sort_JA[0:5000]:
        list_JAPr.append(i[1])
    for i in list_sort_PA[0:5000]:
        list_PAPr.append(i[1])
    test_CNPr = pd.DataFrame(data=list_CNPr)
    test_CNPr.to_csv('E:\\DNA\\大修\\审稿人2-4\\CNPr\\' + str(H) + '.csv', encoding='gbk')
    test_JAPr = pd.DataFrame(data=list_JAPr)
    test_JAPr.to_csv('E:\\DNA\\大修\\审稿人2-4\\JAPr\\' + str(H) + '.csv', encoding='gbk')
    test_PAPr = pd.DataFrame(data=list_PAPr)
    test_PAPr.to_csv('E:\\DNA\\大修\\审稿人2-4\\PAPr\\' + str(H) + '.csv', encoding='gbk')


