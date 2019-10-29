#Analysis of trimers
#### we analyzed the trimers that describe local information
#### of binding sites to check the extent of overlap of local
#### binding sites in different proteins
import os
import pandas as pd

list_all=[]
path = '.\\train\\Trimer'
pathID =  os.listdir(path)
for ID in pathID:
    path_site = path+'\\'+ID+'\\'+'piece3.csv'
    read = pd.read_csv(path_site)
    X = read.iloc[:, 1:4].values#trimer
    #print(X)
    list_1 = list(set([tuple(t) for t in X]))#
    #print(list_1)
    for i in list_1:
        #print(list(i))
        list_all.append(list(i))#
#print(len(list_all))

####The number of trimers not in the same DBP
if __name__ == '__main__':
    map = {}
    for item in list_all:
        s = str(item)
        if s in map.keys():
            map[s] = map[s] + 1
        else:
            map[s] = 1
    number=0
    n=0
    for key in map.keys():
        # print('%s的次数为%d' % (key, map[key]))
        if map[key]==1:###Setting 1-12
            number+=map[key]
            n += 1
            print('%s的次数为%d' % (key, map[key]))
    #print(number)#
    print(n)#

