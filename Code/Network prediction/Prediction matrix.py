import numpy as np
import pandas as pd
np.set_printoptions(threshold=np.nan)
import pylab as pl
import random
list_key_CN=[]
list_key_JA=[]
list_key_PA=[]
NC = []
JA = []
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


matrix_1 = np.zeros((M, N))
for i in dataset:  #
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
#print(matrix_1)
print(matrix_2)
list_all_CN = []
list_all_JA = []
list_all_PA = []
for i in range(matrix_2.shape[0]):  #
    for j in range(matrix_2.shape[1]):  #
        if matrix_2[i, j]>0:

            list_all_CN.append(matrix_2[i, j])  #


print(len(list_all_CN))#


#
arr_mean = np.mean(list_all_CN)
#
arr_var = np.var(list_all_CN)

av=arr_var/(len(list_all_CN)**0.5)
#
arr_std = np.std(list_all_CN)
print("平均值为：%f" % arr_mean)
print("方差为：%f" % arr_var)
print("标准差为:%f" % arr_std)
# # print(av)


list_significant=[]
for i in range(matrix_2.shape[0]):  #
    for j in range(matrix_2.shape[1]):  #
        if matrix_2[i, j]>arr_std:##significant
            list_significant.append(matrix_2[i, j])

print(len(list_significant))#significant
print(0.2*len(list_significant))#important


L=sorted(list_significant,reverse=True)
#print(li[0:1484])
print(L[564])#20%
#####
print(dict2)
print(M)