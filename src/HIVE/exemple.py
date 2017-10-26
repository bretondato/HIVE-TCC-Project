import datetime
from minisom import MiniSom

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dt
import datetime
import SOM_TNSRFLW as som
from collections import Counter
from scipy import spatial
import pylab

filenames = ['1-3-2005-RAW.data', '1-4-2005-RAW.data', '1-5-2005-RAW.data', '1-6-2005-RAW.data', '1-7-2005-RAW.data', '1-8-2005-RAW.data',
             '1-9-2005-RAW.data', '1-10-2005-RAW.data', '1-11-2005-RAW.data', '1-12-2005-RAW.data', '1-13-2005-RAW.data', '1-14-2005-RAW.data',
             '1-15-2005-RAW.data', '1-16-2005-RAW.data', '1-17-2005-RAW.data', '1-18-2005-RAW.data', '1-19-2005-RAW.data', '1-20-2005-RAW.data',
             '1-21-2005-RAW.data', '1-22-2005-RAW.data', '1-23-2005-RAW.data', '1-24-2005-RAW.data', '1-25-2005-RAW.data', '1-26-2005-RAW.data',
             '1-27-2005-RAW.data', '1-28-2005-RAW.data', '1-29-2005-RAW.data', '1-30-2005-RAW.data', '1-31-2005-RAW.data']

filedata = {filename: open(filename, 'r') for filename in filenames}

# f = open('2-8-2005-RAW.data', 'r')

# lines = f.readlines()

i = 3
j = 26251

dta = []
hour = []
day = []
list_of_days = []
val = []
list_of_datetimes = []
aux = []
eventst = []
eventsd = []

#and int(lines[u][33] + lines[u][34] + lines[u][35]) == 3

for i in filedata.values():
    lines = i.readlines()
    #print(lines)
    for u in range(2, len(lines) - 2):
        if lines[u][23] == 'a':
            # print(lines)
            value = int(lines[u][49] + lines[u][50] + lines[u][51])
            date = lines[u][12:20]
            list_of_datetimes.append(date)
            val.append(value)


# for i in range(0, len(list_of_datetimes)):
dates = dt.datestr2num(list_of_datetimes)

event_set = []
som_in = []

for i in range(0, len(val)):
    if val[i] - 100 == -100:
        ev = dates[i] - dates[i - 1]
        if ev < 0:
            pass
        else:
            #eventsd.append(ev)
            #eventst.append(dates[i])
            event_set.append(ev)
            event_set.append(dates[i])
            som_in.append(event_set)
            event_set = []



# v = [values, dates]


"""
# print(val)
# print(dates)
som_in = []
ev = []

for i, w in enumerate(eventsd):
    ev.append(eventsd[i])
    ev.append(eventst[i])
    som_in.append(ev)

    ev = []
"""
som = som.SOM(2, 2, 2, 100)
som.train(som_in)
image_grid = som.get_centroids()
mapped = som.map_vects(som_in)

fr = []

clus1 = []
clus2 = []
clus3 = []
clus4 = []


for i, m in enumerate(mapped):
    fr.append(m)
    count = Counter(map(tuple, fr))
    count = dict(count)

    if list(m) == [0, 0]:
        clus1.append(som_in[i])
    if list(m) == [0, 1]:
        clus2.append(som_in[i])
    if list(m) == [1, 0]:
        clus3.append(som_in[i])
    if list(m) == [1, 1]:
        clus4.append(som_in[i])


clus1 = np.array(clus1)
clus2 = np.array(clus2)
clus3 = np.array(clus3)
clus4 = np.array(clus4)

#d1 = np.sqrt(np.add(((g1[:, [0]] - image_grid[0][0])**2), ((g1[:, [1]] - image_grid[0][1])**2)))

#print("C1", ((g1[:, [0]] - image_grid[0][0])**2))


euclidian_list1 = [((spatial.distance.euclidean(coord, list(image_grid[0][0]))), coord) for coord in clus1]

euclidian_list2 = [(spatial.distance.euclidean(coord, list(image_grid[0][1]))) for coord in clus2]

euclidian_list3 = [(spatial.distance.euclidean(coord, list(image_grid[1][0]))) for coord in clus3]

euclidian_list4 = [(spatial.distance.euclidean(coord, list(image_grid[1][1]))) for coord in clus4]


#mu = (np.mean(euclidian_list1[:, 0]))
#std = np.std(euclidian_list1[0])

#pdfClus1 = pylab.normpdf(euclidian_list1, mu, std)

plt.subplot(221)
for i, m in enumerate(som_in):
    #print(som_in[i][1])
    plt.plot(som_in[i][1], som_in[i][0], 'ro')


plt.subplot(221)
for i in range(0, len(image_grid)):
    for j in range(0, len(image_grid[i])):
        plt.plot(image_grid[i][j][1], image_grid[i][j][0], 'bo')


#print("Som Input", som_in)
#print("G1: ", clus1)
#print("Centroids", image_grid[0][0])
#print(image_grid)
#print("Mapped: ", mapped)

eu = euclidian_list1[:, [0]]
print("Euclidian List Cluster 1: ", euclidian_list1)
print("Euclidian distance data 1: ", eu)
print("tamanho: ", len(euclidian_list1))


#print("Media do cluster 1:", mu)
#print("Desvio Padrao cluster 1:", std)
#pdfClus1 = (1/pdfClus1)
#pdfClus1.sort()
#print("Distribuição Normal Cluster 1:", pdfClus1)
#print("tamanho:", len(pdfClus1))

plt.show()