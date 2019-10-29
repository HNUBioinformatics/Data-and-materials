# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 11:21:24 2018

@author: Administrator
"""
#####PR
####
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

for h in range(10):
    test = random.sample(dataset, 217)
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


    data_neg=random.sample(list_test_3,217)
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

    TP_CN=1
    FP_CN=0
    FN_CN=0
    P_CN=0
    R_CN=0
    TPR_CN=0
    FPR_CN=0
    list_CN_p = []
    list_CN_r = []
    list_CN_tpr = []
    list_CN_fpr = []
    for i in list_sort_CN[0:5000]:
        if i[1] in test:
            TP_CN+=1
        if i[1] in data_neg:
            FP_CN+=1

        if (FP_CN + TP_CN) != 0:
            P_CN = TP_CN / (FP_CN + TP_CN)
            R_CN = TP_CN / len(test)
            TPR_CN = TP_CN / len(test)
            FPR_CN = FP_CN / len(data_neg)
        list_CN_p.append(P_CN)
        list_CN_r.append(R_CN)
        list_CN_tpr.append(TPR_CN)
        list_CN_fpr.append(FPR_CN)
    F1_CN = 2 * (P_CN * R_CN) / (P_CN + R_CN)
    Sensitive_CN=TP_CN/len(test)
    specificity_CN=FP_CN/len(data_neg)


    # plt.plot(list_CN_fpr, list_CN_tpr)
    # plt.show()

    TP_JA = 0
    FP_JA = 0
    FN_JA = 0
    P_JA = 0
    R_JA = 0
    TPR_JA = 0
    FPR_JA = 0
    list_JA_p = []
    list_JA_r = []
    list_JA_tpr = []
    list_JA_fpr = []
    for i in list_sort_JA[0:5000]:
        if i[1] in test:
            TP_JA += 1
        if i[1] in data_neg:
            FP_JA += 1
        if (FP_JA + TP_JA) != 0:
            P_JA = TP_JA / (FP_JA + TP_JA)
            R_JA = TP_JA / len(test)
            TPR_JA = TP_JA / len(test)
            FPR_JA = FP_JA / len(data_neg)


        list_JA_p.append(P_JA)
        list_JA_r.append(R_JA)
        list_JA_tpr.append(TPR_JA)
        list_JA_fpr.append(FPR_JA)
        # list_tpr.append(TPR)
        # list_fpr.append(FPR)
    F1_JA = 2 * (P_JA * R_JA) / (P_JA + R_JA)
    Sensitive_JA = TP_JA / len(test)
    specificity_JA = FP_JA / len(data_neg)

    # plt.plot(list_JA_fpr, list_JA_tpr)
    # plt.show()

    TP_PA = 0
    FP_PA = 0
    FN_PA = 0
    P_PA = 0
    R_PA = 0
    TPR_PA = 0
    FPR_PA = 0
    list_PA_p = []
    list_PA_r = []
    list_PA_tpr = []
    list_PA_fpr = []
    for i in list_sort_PA[0:5000]:
        if i[1] in test:
            TP_PA += 1
        if i[1] in data_neg:
            FP_PA += 1
        if (FP_PA + TP_PA) != 0:
            P_PA = TP_PA / (FP_PA + TP_PA)
            R_PA = TP_PA / len(test)
            TPR_PA = TP_PA / len(test)
            FPR_PA = FP_PA / len(data_neg)
        list_PA_p.append(P_PA)
        list_PA_r.append(R_PA)
        list_PA_tpr.append(TPR_PA)
        list_PA_fpr.append(FPR_PA)
        # list_tpr.append(TPR)
        # list_fpr.append(FPR)
    F1_PA = 2 * (P_PA * R_PA) / (P_PA + R_PA)
    Sensitive_PA = TP_PA / len(test)
    specificity_PA = FP_PA / len(data_neg)

    F1_cn.append(F1_CN)
    F1_ja.append(F1_JA)
    F1_pa.append(F1_PA)
    Sensitive_cn.append(Sensitive_CN)
    Sensitive_ja.append(Sensitive_JA)
    Sensitive_pa.append(Sensitive_PA)
    specificity_cn.append(specificity_CN)
    specificity_ja.append(specificity_JA)
    specificity_pa.append(specificity_PA)


    list_key_allCNr.append(list_CN_r)
    list_key_allCNp.append(list_CN_p)
    list_key_allCNfpr.append(list_CN_fpr)
    list_key_allCNtpr.append(list_CN_tpr)


    list_key_allJAr.append(list_JA_r)
    list_key_allJAp.append(list_JA_p)
    list_key_allJAfpr.append(list_JA_fpr)
    list_key_allJAtpr.append(list_JA_tpr)


    list_key_allPAr.append(list_PA_r)
    list_key_allPAp.append(list_PA_p)
    list_key_allPAfpr.append(list_PA_fpr)
    list_key_allPAtpr.append(list_PA_tpr)

for i in list_key_allCNr:
    print(len(i))



for i in range(len(list_key_allCNr[0])):
    sum_cn_r = 0
    #print(len(list_key_allCNr))
    for j in range(10):
        sum_cn_r+=list_key_allCNr[j][i]
    list_key_allCNR.append(sum_cn_r/10)

for i in range(len(list_key_allCNp[0])):
    sum_cn_p = 0
    for j in range(10):
        sum_cn_p += list_key_allCNp[j][i]
    list_key_allCNP.append(sum_cn_p / 10)

for i in range(len(list_key_allCNfpr[0])):
    sum_cn_fpr = 0
    #print(len(list_key_allCNr))
    for j in range(10):
        sum_cn_fpr+=list_key_allCNfpr[j][i]
    list_key_allCNFPR.append(sum_cn_fpr/10)

for i in range(len(list_key_allCNtpr[0])):
    sum_cn_tpr = 0
    for j in range(10):
        sum_cn_tpr += list_key_allCNtpr[j][i]
    list_key_allCNTPR.append(sum_cn_tpr / 10)

for i in range(len(list_key_allJAr[0])):
    sum_ja_r = 0
    #print(len(list_key_allCNr))
    for j in range(10):
        sum_ja_r+=list_key_allJAr[j][i]
    list_key_allJAR.append(sum_ja_r/10)

for i in range(len(list_key_allJAp[0])):
    sum_ja_p = 0
    for j in range(10):
        sum_ja_p += list_key_allJAp[j][i]
    list_key_allJAP.append(sum_ja_p / 10)

for i in range(len(list_key_allJAfpr[0])):
    sum_ja_fpr = 0
    #print(len(list_key_allCNr))
    for j in range(10):
        sum_ja_fpr+=list_key_allJAfpr[j][i]
    list_key_allJAFPR.append(sum_ja_fpr/10)

for i in range(len(list_key_allJAtpr[0])):
    sum_ja_tpr = 0
    for j in range(10):
        sum_ja_tpr += list_key_allJAtpr[j][i]
    list_key_allJATPR.append(sum_ja_tpr / 10)


for i in range(len(list_key_allPAr[0])):
    sum_pa_r = 0
    #print(len(list_key_allCNr))
    for j in range(10):
        sum_pa_r+=list_key_allPAr[j][i]
    list_key_allPAR.append(sum_pa_r/10)

for i in range(len(list_key_allPAp[0])):
    sum_pa_p = 0
    for j in range(10):
        sum_pa_p += list_key_allPAp[j][i]
    list_key_allPAP.append(sum_pa_p / 10)

for i in range(len(list_key_allPAfpr[0])):
    sum_pa_fpr = 0
    #print(len(list_key_allCNr))
    for j in range(10):
        sum_pa_fpr+=list_key_allPAfpr[j][i]
    list_key_allPAFPR.append(sum_pa_fpr/10)

for i in range(len(list_key_allPAtpr[0])):
    sum_pa_tpr = 0
    for j in range(10):
        sum_pa_tpr += list_key_allPAtpr[j][i]
    list_key_allPATPR.append(sum_pa_tpr / 10)


# print(list_key_allCNR)
# print(len(list_key_allCNR))
# print(list_key_allCNP)
# print(len(list_key_allCNP))

print(sum(F1_cn)/len(F1_cn))
print(sum(F1_ja)/len(F1_ja))
print(sum(F1_pa)/len(F1_pa))
print(sum(Sensitive_cn)/len(Sensitive_cn))
print(sum(Sensitive_ja)/len(Sensitive_ja))
print(sum(Sensitive_pa)/len(Sensitive_pa))
print(sum(specificity_cn)/len(specificity_cn))
print(sum(specificity_ja)/len(specificity_ja))
print(sum(specificity_pa)/len(specificity_pa))

    # print(F1_CN)
    # print(F1_JA)
    # print(F1_PA)
plt.plot(list_key_allCNR, list_key_allCNP)
plt.show()
#test = pd.DataFrame(data=list_key_allCNR)
plt.plot(list_key_allCNFPR,list_key_allCNTPR)
plt.show()
plt.plot(list_key_allJAR, list_key_allJAP)
plt.show()
plt.plot(list_key_allJAFPR,list_key_allJATPR)
plt.show()
plt.plot(list_key_allPAR, list_key_allPAP)
plt.show()
plt.plot(list_key_allPAFPR,list_key_allPATPR)
plt.show()

testallCNR = pd.DataFrame(data=list_key_allCNR)
testallCNR.to_csv('E:\\DNA\\PR and ROC\\CNR.csv', encoding='gbk')
testallCNP = pd.DataFrame(data=list_key_allCNP)
testallCNP.to_csv('E:\\DNA\\PR and ROC\\CNP.csv', encoding='gbk')
testallJAR = pd.DataFrame(data=list_key_allJAR)
testallJAR.to_csv('E:\\DNA\\PR and ROC\\JAR.csv', encoding='gbk')
testallJAP = pd.DataFrame(data=list_key_allJAP)
testallJAP.to_csv('E:\\DNA\\PR and ROC\\JAP.csv', encoding='gbk')
testallPAR = pd.DataFrame(data=list_key_allPAR)
testallPAR.to_csv('E:\\DNA\\PR and ROC\\PAR.csv', encoding='gbk')
testallPAP = pd.DataFrame(data=list_key_allPAP)
testallPAP.to_csv('E:\\DNA\\PR and ROC\\PAP.csv', encoding='gbk')
