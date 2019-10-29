import numpy as np
import pandas as pd
import pylab as pl
import random
Length=[]
list_All = []
list_All_1 = []
list_All_PA = []
dataSet = []
for i in range(97):
    for j in range(97):
        dataSet.append([i,j])
print(dataSet)
for i in range(10):
    dataset = random.sample(dataSet,2170)
    # print(dataset)
    # print(len(dataset))

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

    for h in range(100):
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

        list_all = []
        list_all_2 = []
        list_all_PA = []

        for i in range(matrix_2.shape[0]):  #
            for j in range(matrix_2.shape[1]):  #
                if matrix_2[i][j] != 0:
                    list_all.append([i, j])  #

        for i in range(matrix_3.shape[0]):
            for j in range(matrix_3.shape[1]):
                if matrix_3[i][j] != 0:
                    list_all_2.append([i, j])

        for i in range(matrix_PA.shape[0]):
            for j in range(matrix_PA.shape[1]):
                if matrix_PA[i][j] != 0:
                    list_all_PA.append([i, j])

        TP = 0
        FP = 0
        FN = 0
        TN = 0
        TPR = 0
        FPR = 0
        P = 0
        R = 0
        list_singe_PR = []
        list_singe_PR_2 = []
        list_singe_PR_PA = []
        X = []
        Y = []
        list_test = []
        list_test_2 = []
        list_test_PA = []
        for i in Test:
            list_test.append([matrix_2[i[0][0]][i[0][1]], i[1]])
            list_test_2.append([matrix_3[i[0][0]][i[0][1]], i[1]])
            list_test_PA.append([matrix_PA[i[0][0]][i[0][1]], i[1]])
            #
        #    print(list_test)
        #    print(list_test_2)

        list_sort = sorted(list_test, key=lambda s: s[0], reverse=True)
        list_sort_2 = sorted(list_test_2, key=lambda s: s[0], reverse=True)
        list_sort_PA = sorted(list_test_PA, key=lambda s: s[0], reverse=True)
        ############################
        n = 0
        m = 0
        x = 0
        y = 0
        TPR = 0
        FPR = 0
        X = []
        Y = []

        for i in list_sort[0:370]:
                if i[1]==1:
                    n+=1
                if i[1]==0:
                    m+=1
        for j in range(370):
                x = 0
                y = 0
                for i in list_sort[0:j]:

                    if i[1] == 1:
                        y += 1
                    if i[1] == 0:
                        x += 1
                TPR = y / n
                FPR = x / m
                Y.append(TPR)
                X.append(FPR)

        for i in range(len(X)):
            list_singe_PR.append([X[i],Y[i]])
        list_all_PR.append(list_singe_PR)


        n_2 = 0
        m_2 = 0
        x_2 = 0
        y_2 = 0
        TPR_2 = 0
        FPR_2 = 0
        X_2 = []
        Y_2 = []

        for i in list_sort_2[0:370]:
                if i[1]==1:
                    n_2+=1
                if i[1]==0:
                    m_2+=1
        for j in range(370):
            x_2 = 0
            y_2 = 0
            for i in list_sort_2[0:j]:
                if i[1] == 1:
                    y_2 += 1
                if i[1] == 0:
                    x_2 += 1
            TPR_2 = y_2 / n_2
            FPR_2 = x_2 / m_2
            Y_2.append(TPR_2)
            X_2.append(FPR_2)
        for i in range(len(X_2)):
            list_singe_PR_2.append([X_2[i],Y_2[i]])
        list_all_PR_2.append(list_singe_PR_2)

        n_PA = 0
        m_PA = 0
        x_PA = 0
        y_PA = 0
        TPR_PA = 0
        FPR_PA = 0
        X_PA = []
        Y_PA = []
        for i in list_sort_PA[0:370]:
                if i[1]==1:
                    n_PA+=1
                if i[1]==0:
                    m_PA+=1
        for j in range(370):
            x_PA = 0
            y_PA = 0
            for i in list_sort_PA[0:j]:
                if i[1] == 1:
                    y_PA += 1
                if i[1] == 0:
                    x_PA += 1
            TPR_PA = y_PA / n_PA
            FPR_PA = x_PA / m_PA
            Y_PA.append(TPR_PA)
            X_PA.append(FPR_PA)
        for i in range(len(X_PA)):
            list_singe_PR_PA.append([X_PA[i],Y_PA[i]])
        list_all_PR_PA.append(list_singe_PR_PA)

####
    list_toall = []
    for j in range(len(list_all_PR[4])):  #
        o = 0
        c = 0
        for i in range(len(list_all_PR)):
            # print(list_all_PR[i][j])
            # print(list_all_PR[i][j][1])
            o = list_all_PR[i][j][0] + o
            c = list_all_PR[i][j][1] + c
        z = o / len(list_all_PR)
        x = c / len(list_all_PR)
        list_toall.append([z, x])  #
    #print(list_toall)
    #
    list_All.append(list_toall)
    #

    list_toall_2 = []
    for j in range(len(list_all_PR_2[4])):  #
        o = 0
        c = 0
        for i in range(len(list_all_PR_2)):
            # print(list_all_PR[i][j])
            # print(list_all_PR[i][j][1])
            o = list_all_PR_2[i][j][0] + o
            c = list_all_PR_2[i][j][1] + c
        z = o / len(list_all_PR_2)
        x = c / len(list_all_PR_2)
        list_toall_2.append([z, x])  #
    #print(list_toall_2)
    #
    list_All_1.append(list_toall_2)
    #

    list_toall_PA = []
    for j in range(len(list_all_PR_PA[4])):  #
        o = 0
        c = 0
        for i in range(len(list_all_PR_PA)):
            # print(list_all_PR[i][j])
            # print(list_all_PR[i][j][1])
            o = list_all_PR_PA[i][j][0] + o
            c = list_all_PR_PA[i][j][1] + c
        z = o / len(list_all_PR_PA)
        x = c / len(list_all_PR_PA)
        list_toall_PA.append([z, x])  #
    #print(list_toall_PA)
    #
    list_All_PA.append(list_toall_PA)
    #

####
LIST = []
for j in range(len(list_All[0])):
    o = 0
    c = 0
    for i in range(len(list_All)):
        # print(list_all_PR[i][j])
        # print(list_all_PR[i][j][1])
        o = list_All[i][j][0] + o
        c = list_All[i][j][1] + c
    z = o / len(list_All)
    x = c / len(list_All)
    LIST.append([z, x])  # z

LIST_1 = []
for j in range(len(list_All_1[0])):
    o = 0
    c = 0
    for i in range(len(list_All_1)):
        # print(list_all_PR[i][j])
        # print(list_all_PR[i][j][1])
        o = list_All_1[i][j][0] + o
        c = list_All_1[i][j][1] + c
    z = o / len(list_All_1)
    x = c / len(list_All_1)
    LIST_1.append([z, x])  #
print(LIST_1)

LIST_PA = []
for j in range(len(list_All_PA[0])):
    o = 0
    c = 0
    for i in range(len(list_All_PA)):
        # print(list_all_PR[i][j])
        # print(list_all_PR[i][j][1])
        o = list_All_PA[i][j][0] + o
        c = list_All_PA[i][j][1] + c
    z = o / len(list_All_PA)
    x = c / len(list_All_PA)
    LIST_PA.append([z, x])  # 
print(LIST_PA)

X_1 = []
Y_1 = []
X_3 = []
Y_3 = []
X_PA = []
Y_PA = []

for i in LIST:
    Y_1.append(i[1])
    X_1.append(i[0])

#        print(p)
#        print(R)
for i in LIST_1:
    Y_3.append(i[1])
    X_3.append(i[0])

#        print(p)
#        print(R)
for i in LIST_PA:
    Y_PA.append(i[1])
    X_PA.append(i[0])

#        print(p)
#        print(R)

pl.title('ROC')
pl.xlabel("FPR")
pl.ylabel("TPR")
# pl.plot(X_1, Y_1,marker='o',color='red', label='N',mfc='w')
# pl.plot(X_3, Y_3,marker='o', color='green', label='J',mfc='w')
# pl.plot(X_PA, Y_PA,marker='o', color='yellow', label='P',mfc='w')
pl.plot(X_1, Y_1, color='red', label='N', mfc='w')
pl.plot(X_3, Y_3, color='green', label='J', mfc='w')
pl.plot(X_PA, Y_PA, color='yellow', label='P', mfc='w')
pl.show()

test = pd.DataFrame(data=LIST)
test.to_csv('G:\\DNA binding protein\PR and ROC\\BaseCN.csv', encoding='gbk')

test = pd.DataFrame(data=LIST_1)
test.to_csv('G:\\DNA binding protein\PR and ROC\\BaseJA.csv', encoding='gbk')

test = pd.DataFrame(data=LIST_PA)
test.to_csv('G:\\DNA binding protein\PR and ROC\\BasePA.csv.csv', encoding='gbk')
