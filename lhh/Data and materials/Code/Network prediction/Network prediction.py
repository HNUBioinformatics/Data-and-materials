# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 11:21:24 2018

@author: Administrator
"""

import numpy as np
import pandas as pd
import pylab as pl
import random
list_key_CN=[]
list_key_JA=[]
list_key_PA=[]
NC = []
JA = []
path = '.\\Drug-cluster association data\\data.csv'
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
    list2.append(i[0])  # 对第一个元素排序
    list3.append(i[1])  # 对第二个元素排序
# print(np.sort(list2))
# print(np.sort(list3))
# 主要作用是找到矩阵行列的值
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
##把有相互关系的读入矩阵并输出行列的值


matrix_2 = np.zeros((M, N))  # 初始一个零矩阵
matrix_3 = np.zeros((M, N))
matrix_PA = np.zeros((M, N))

cn = 0
d = 0
d1 = 0
d2 = 0
for i in range(M):  # 遍历每一行
    print('number %d is running\n', i)
    for j in range(N):  # 遍历每一列
        if matrix_1[i, j] == 0:  # 找到药物和蛋白质没有关系的位置
            list_x = matrix_1[i]  # 把所在行赋予list_x
            list_y = matrix_1[:, j]  # 把所在列赋予list_y
            for l in range(len(list_y)):
                if list_y[l] == 1:
                    d1 += 1
            # print(list_x)
            # print(list_y)
            for h in range(len(list_x)):  # 遍历list_x
                if list_x[h] == 1:
                    d += 1

                    list_z = matrix_1[:, h]

                    for K in range(M):
                        if list_z[K] == 1:
                            d2 += 1
                        if list_y[K] * list_z[K] == 1:
                            cn = cn + 1  # 有共同的邻居则+1
            matrix_2[i, j] = cn
            # 计算CN
            if (d1 + d2 - d) != 0:
                matrix_3[i, j] = cn / (d1 + d2 - d - cn)
            # 计算J
            matrix_PA[i, j] = (d1 * d)
            # 计算PA

            d = 0
            cn = 0
            d1 = 0
            d2 = 0

list_all_CN = []
list_all_JA = []
list_all_PA = []
for i in range(matrix_2.shape[0]):  # 遍历行
    for j in range(matrix_2.shape[1]):  # 遍历列
        list_all_CN.append([matrix_2[i, j], [i, j]])  # 把预测矩阵中不等于0的保存list_all
list_sort_CN = sorted(list_all_CN, key=lambda s: s[0], reverse=True)
#print(len(list_sort_CN))
#print(list_sort_CN[0:1881])

for i in range(matrix_3.shape[0]):
    for j in range(matrix_3.shape[1]):
        list_all_JA.append([matrix_3[i, j], [i, j]])
list_sort_JA = sorted(list_all_JA, key=lambda s: s[0], reverse=True)
# print(list_sort_JA)

for i in range(matrix_PA.shape[0]):
    for j in range(matrix_PA.shape[1]):
        list_all_PA.append([matrix_PA[i, j], [i, j]])
list_sort_PA = sorted(list_all_PA, key=lambda s: s[0], reverse=True)
# print(list_sort_PA)

# list_key_CN=[]
for i in list_sort_CN:

    for key, val in dict1.items():
        if val == i[1][0]:
            #                print(key)
            a = key
    for key, val in dict2.items():
        if val == i[1][1]:
            #                print(key)
            b = key
    list_key_CN.append([a,b])
#    print(list_key_CN)

#    list_key_JA=[]
for i in list_sort_JA:

    for key, val in dict1.items():
        if val == i[1][0]:
            #                print(key)
            a = key
    for key, val in dict2.items():
        if val == i[1][1]:
            #                print(key)
            b = key
    list_key_JA.append([a, b])
#    print(list_key_JA)

#    list_key_PA=[]
for i in list_sort_PA:

    for key, val in dict1.items():
        if val == i[1][0]:
            #                print(key)
            a = key
    for key, val in dict2.items():
        if val == i[1][1]:
            #                print(key)
            b = key
    list_key_PA.append([a, b])
#    print(list_key_PA)

print(list_key_CN)
print(list_key_JA)
print(list_key_PA)

test = pd.DataFrame(data=list_key_CN)
path1 = '.\\prediction' + '\\' + 'CN.csv'
test.to_csv(path1, encoding='gbk')

# test = pd.DataFrame(data=list_key_JA)
# path1 = 'E:\\DNA\\prediction' + '\\' + 'JA.csv'
# test.to_csv(path1, encoding='gbk')
#
# test = pd.DataFrame(data=list_key_PA)
# path1 = 'E:\\DNA\\prediction' + '\\' + 'PA.csv'
# test.to_csv(path1, encoding='gbk')
