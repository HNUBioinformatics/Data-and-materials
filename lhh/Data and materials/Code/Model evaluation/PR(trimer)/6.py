
#####
###PR
#####
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc  ###计算roc和auc
from sklearn.metrics import precision_recall_curve
list_key_allCNr=[]
list_key_allCNp=[]
list_key_allCNfpr=[]
list_key_allCNtpr=[]
list_key_allCNP=[]
list_key_allCNFPR=[]
list_key_allCNTPR=[]

list_key_allCNR=[]
path_Neg = 'E:\\DNA\\大修\\审稿人2-4\\Negative\\Negative\\'
files_Neg = os.listdir(path_Neg)
files_Negcsv = list(filter(lambda x: x[-4:] == '.csv', files_Neg))

path_Pos = 'E:\\DNA\\大修\\审稿人2-4\\Positive\\Positive\\'
files_Pos = os.listdir(path_Pos)
files_Poscsv = list(filter(lambda x: x[-4:] == '.csv', files_Neg))

path_Pre = 'E:\\DNA\\大修\\审稿人2-4\\\PA(trimer)\\'
files_Pre = os.listdir(path_Pre)
files_Precsv = list(filter(lambda x: x[-4:] == '.csv', files_Pre))

for file in files_Negcsv:  #
    # print(file[0:-4])
    list_Pre=[]
    list_Neg=[]
    list_Pos=[]
    F=open(path_Neg + file)
    tmp_Neg = pd.read_csv(F)[['0', '1']].values
    for i in tmp_Neg:
        list_Neg.append(list(i))

    Q=open(path_Pos + file)
    tmp_Pos = pd.read_csv(Q)[['0', '1']].values
    for i in tmp_Pos:
        list_Pos.append(list(i))

    P=open(path_Pre + file)
    tmp_Pre = pd.read_csv(P)[['0', '1']].values
    for i in tmp_Pre:
        list_Pre.append(list(i))
    #
    TP=0
    FP=0
    FN=0
    TN=0
    P=0
    R=0
    TPR=0
    FPR=0
    list_p=[]
    list_r=[]
    list_PR=[]
    list_tpr=[]
    list_fpr=[]
    N=0
    for i in list_Pre:
        print(i)
        N+=1
        if i in list_Pos:
            TP+=1
        if i in list_Neg:
            FP+=1
        # else:
        #     FN += 1
        #if i not in tmp_Neg:

        # if i not in tmp_Neg:
        #     TP+=1
        if (FP + TP) != 0:
            P = TP / (FP + TP)
            R = TP / len(tmp_Pos)
        # TPR = TP/ N
        # FPR = FP / len(tmp_Neg)
        list_PR.append([R,P])
        list_p.append(P)
        list_r.append(R)
        # list_tpr.append(TPR)
        # list_fpr.append(FPR)


    list_key_allCNr.append(list_r)
    list_key_allCNp.append(list_p)
        # list_key_allCNfpr.append(list_fpr)
        # list_key_allCNtpr.append(list_tpr)
    # for i in range(len(list_p)):
    #     list_PR.append([list_r[i],list_p[i]])
    # print(list_pre)
    # print(list_r)
    # plt.plot(list_r, list_p)
    # plt.show()
    test = pd.DataFrame(data=list_PR)
    test.to_csv('E:\\DNA\\大修\\审稿人2-4\\PR\\PA\\'+str(file[:-4])+'.csv')
    # test = pd.DataFrame(data=list_p)
    # test.to_csv('F:\\DNA Binding protein\\modify\\PR\\CN_PR\\' + str(file) + 'p.csv')

