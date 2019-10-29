
####degree distributions
import pandas as pd
import numpy as np
dataSet=pd.read_csv('.\\train\\Drug-cluster association data\\data.csv')
matrix = np.zeros((97, 97))

X = dataSet.iloc[:, 1:3].values #
#print(X)
dict1 = {}
num = 0
for i in dataSet.iloc[:, 2]:
    #print(i)
    if i not in list(dict1.keys()):
        dict1[i] = num
        num += 1

for i in X:
    matrix[i[0],dict1[i[1]]]=1
# print(matrix)
# print(matrix.sum(axis=1))#Calculate the sum of each row of the matrix, ie the degree of the cluster
# print(matrix.sum(axis=0))#Calculate the sum of each column of the matrix, ie the degree of drug
array_Row=matrix.sum(axis=1)
list_Row=array_Row.tolist()

array_Column=matrix.sum(axis=0)
list_Column=array_Column.tolist()
print(list_Row)
print(list_Column)

#####Step size is 5
####the degree of cluster
number_Row=0
for j in range(20):
    n=0
    for i in list_Row:
        if number_Row<=i<(number_Row + 5):
            n+=1
    print(n)
    number_Row+=5


print('--------')

###Step size is 5
#####the degree of drug
number_Column=0
for j in range(20):
    n=0
    for i in list_Column:
        if number_Column<=i<(number_Column + 5):
            n+=1
    print(n)
    number_Column+=5
