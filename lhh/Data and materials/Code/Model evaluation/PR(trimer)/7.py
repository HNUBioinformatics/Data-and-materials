import os
import pandas as pd
path = 'E:\\DNA\\大修\\审稿人2-4\\PR\\JA\\'
file = os.listdir(path)
files = list(filter(lambda x: x[-4:] == '.csv', file))

list_all = []

for file in files:  #
    list_ = []
    F = open(path + file)
    tmp_Neg = pd.read_csv(F)[['0', '1']].values
    for i in tmp_Neg:
        list_.append(list(i))
    list_all.append(list_)

list_A = []
for i in range(len(list_all[3])):
    sum = 0
    sum_ = 0
    # print(len(list_key_allCNr))
    for j in range(10):
        sum += list_all[j][i][0]
        sum_ += list_all[j][i][1]

    list_A.append([sum / 10,sum_/10])
print(list_A)
test = pd.DataFrame(data=list_A)
test.to_csv('E:\\DNA\\大修\\审稿人2-4\\PR\\JA.csv')
    # test = pd.DataFrame(data=list_p)