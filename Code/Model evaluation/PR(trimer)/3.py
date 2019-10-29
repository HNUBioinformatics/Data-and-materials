import numpy as np
import os
import pandas as pd
path = 'E:\\DNA\\大修\\审稿人2-4\\PAPr\\'
files = os.listdir(path)
files_csv = list(filter(lambda x: x[-4:] == '.csv', files))

###
for file in files_csv:  #
    print(file)
    f = open(path + file)
    tmp = pd.read_csv(f)[['0', '1']].values  #
    list_trimer = []
    list_drug = []
    list_all = []
    for i in tmp:
        list_i = []
        path_clu = 'E:\\DNA\\大修\\审稿人2-4\\cluster(trimer)\\' + str(i[0]) + '.csv'
        q = open(path_clu)
        trimer = pd.read_csv(q)['0'].values

        for j in trimer:
            list_all.append([j, i[1]])
    print(list_all)
    test = pd.DataFrame(data=list_all)
    test.to_csv('E:\\DNA\\大修\\审稿人2-4\\PA(trimer)\\' + file[0:-4] + '.csv', encoding='gbk')
        #