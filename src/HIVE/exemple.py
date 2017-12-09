import datetime
from minisom import MiniSom

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dt
import datetime
import SOM_TNSRFLW as som
from collections import Counter
from scipy import spatial
import room
import device
import pylab


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

mu = 0.0000
mus = []
std = []
stds = []

Room_List_name = []
Device_List_Name = []

Room_List = []
Device_list = []

somInput_i = []



filenames = ['1-3-2005-RAW.data', '1-4-2005-RAW.data', '1-5-2005-RAW.data', '1-6-2005-RAW.data', '1-7-2005-RAW.data', '1-8-2005-RAW.data',
             '1-9-2005-RAW.data', '1-10-2005-RAW.data', '1-11-2005-RAW.data', '1-12-2005-RAW.data', '1-13-2005-RAW.data', '1-14-2005-RAW.data',
             '1-15-2005-RAW.data', '1-16-2005-RAW.data', '1-17-2005-RAW.data', '1-18-2005-RAW.data', '1-19-2005-RAW.data', '1-20-2005-RAW.data',
             '1-21-2005-RAW.data', '1-22-2005-RAW.data', '1-23-2005-RAW.data', '1-24-2005-RAW.data', '1-25-2005-RAW.data', '1-26-2005-RAW.data',
             '1-27-2005-RAW.data', '1-28-2005-RAW.data', '1-29-2005-RAW.data', '1-30-2005-RAW.data', '1-31-2005-RAW.data', '2-1-2005-RAW.data',
             '2-2-2005-RAW.data', '2-3-2005-RAW.data', '2-4-2005-RAW.data', '2-5-2005-RAW.data', '2-6-2005-RAW.data', '2-7-2005-RAW.data',
             '2-8-2005-RAW.data', '2-9-2005-RAW.data', '2-10-2005-RAW.data', '2-11-2005-RAW.data', '2-12-2005-RAW.data', '2-13-2005-RAW.data',
             '2-14-2005-RAW.data', '2-15-2005-RAW.data', '2-16-2005-RAW.data', '2-17-2005-RAW.data', '2-18-2005-RAW.data','2-19-2005-RAW.data',
             '2-20-2005-RAW.data']

#filenames = ['1-3-2005-RAW.data', '1-4-2005-RAW.data', '1-5-2005-RAW.data', '1-6-2005-RAW.data', '1-7-2005-RAW.data', '1-8-2005-RAW.data']

filedata = {filename: open(filename, 'r') for filename in filenames}



# ======================================== Captura da Base ===========================================
for i in filedata.values():
    lines = i.readlines()

    for u in range(2, len(lines) - 2):
        room_Reader = lines[u][23]
        device_Reader = int(lines[u][33] + lines[u][34] + lines[u][35])
        value = int(lines[u][49] + lines[u][50] + lines[u][51])
        state = int(lines[u][43])
        time = lines[u][12:20]
        local = lines[u][53:64]

        if room_Reader not in Room_List_name:
            r = room.Room()
            r.setName(room_Reader)
            Room_List.append(r)
            Room_List_name.append(r.getName())

        for i in Room_List:
            if i.getName() == room_Reader and device_Reader not in i.getDeviceNameList():
                d = device.Device()
                d.setId(device_Reader)
                #d.setState(value)
                i.setDeviceList(d)
                i.setDeviceNameList(d.getId())
                Device_List_Name.append(d.getId())

            for j in i.getDeviceList():
                if device_Reader == j.getId() and i.getName() == room_Reader:

                    if local == '| ArgusMS |':
                        pass
                    else:
                        #e = device.Actuator()
                        #e.setState(value)
                        ev = j.convertTimeToEvent(time)
                        #e.setTimeA(ev)
                        j.setEventlist(value)
                        j.setTime(time)


    # ===================== Metedo para capturar dados de apenas um comodo ================
    """
    for u in range(2, len(lines) - 2):
        if lines[u][23] == 'a':
            # print(lines)
            value = int(lines[u][49] + lines[u][50] + lines[u][51])
            date = lines[u][12:20]
            list_of_datetimes.append(date)
            val.append(value)
    """
    # =====================================================================================
# ====================================================================================================

# ======================================== Calculo de Eventos ========================================
# Loop para calcular a duração dos eventos e quantizar a quantidade de lixo em cada um dos comodos
for i in Room_List:
    for j in i.getDeviceList():
        nudur = dt.datestr2num(j.getTime())

        for k in range(0, len(j.getEventList()) - 2):

            if j.getEventAtIndex(k) == 0:
                k = k + 1
            if j.getEventAtIndex(k) - j.getEventAtIndex(k + 1) <= 0:
                j.setTrash()
            else:
                dur =  nudur[k + 1] - nudur[k]
                if dur < 0:
                    pass
                else:
                    j.setDuration(dur)
                    j.setDuration(nudur[k])
                    j.setSomIn(j.getDuration())
                    j.emptyDurationList()

# ====================================================================================================

# ================ Versão para um comomdo ======================
"""
# for i in range(0, len(list_of_datetimes)):
dates = dt.datestr2num(list_of_datetimes)

event_set = []
som_in = []
k = 0


for i in range(0, len(val)-1):
    if val[0] == 0:
        i = i + 1
    if val[i] - val[i + 1] <= 0:
        k += 1
    else:
        ev = dates[i + 1] - dates[i]
        if ev < 0:
            pass
        else:
            event_set.append(ev)
            #print("event set: ", event_set)
            event_set.append(dates[i])
            som_in.append(event_set)
            #print("som in: ", som_in)
            event_set = []

print("som_in", som_in)
"""
# ==============================================================

# =============================================== Clusterização ===============================================
trash = 0
som_in = []

for i, m in enumerate(Room_List):
    if m.getName() == 'i':
        title = m.getName()
        for j, n in enumerate(m.getDeviceList()):
            som_in = som_in + n.getSomIn()
            trash = trash + n.getTrash()


#
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

euclidianLists = []
outs = []

euclidian_list1 = [((spatial.distance.euclidean(coord, list(image_grid[0][0]))), coord) for coord in clus1]
euclidianLists.append(euclidian_list1)

euclidian_list2 = [((spatial.distance.euclidean(coord, list(image_grid[0][1]))), coord) for coord in clus2]
euclidianLists.append(euclidian_list2)

euclidian_list3 = [((spatial.distance.euclidean(coord, list(image_grid[1][0]))), coord) for coord in clus3]
euclidianLists.append(euclidian_list3)

euclidian_list4 = [((spatial.distance.euclidean(coord, list(image_grid[1][1]))), coord) for coord in clus4]
euclidianLists.append(euclidian_list4)

#print(euclidianLists)

# ===============================================================================================================

# ======================================== Detecção =====================================
for i in euclidianLists:
    print(i)
    for id, m in enumerate(i):
        e = m[0]
        mu += e
        std.append(e)

    if len(i) == 0:
        pass
    else:
        mu = mu / len(i)
        mus.append(mu)
        stdt = np.std(std)
        stds.append(stdt)

print("Medias:", mus)
print("Desvios Padrão: ", stds)

acoord = []
for idx, l in enumerate(euclidianLists):
    for i, m in enumerate(l):
        if m[0] > (mus[idx] + 2*stds[idx]):
            acoord.append(m[1][1])
            acoord.append(m[1][0])
            outs.append(acoord)
            acoord = []

distList = []
NormDist_1 = []
for i, k in enumerate(euclidian_list4):
    distList.append(k[0])

NormDist_1 = [1 / pylab.normpdf(i, mus[0], stds[0]) for i in distList]
print("Distribuição Normal do Cluster 1: ", NormDist_1)

plt.hist(NormDist_1, normed=True)


#print(outs)
# =======================================================================================

# ================================= Plot ==================================
# Ploter de Eventos
#plt.subplot(221)
"""
for i, m in enumerate(som_in):
    #print(som_in[i][1])
    plt.title(title)
    plt.plot(som_in[i][1], som_in[i][0], 'ro')

# Ploter de Neuronios
#plt.subplot(221)
for i in range(0, len(image_grid)):
    for j in range(0, len(image_grid[i])):
        plt.plot(image_grid[i][j][1], image_grid[i][j][0], 'bo')

#Ploter de Anomalias
for idx, l in enumerate(outs):
    plt.plot(l[0], l[1], 'go')
"""


# ==========================================================================


print("Total de Dados: ", len(euclidian_list2) + len(euclidian_list1) + len(euclidian_list3) + len(euclidian_list4))
print("Quantidade de eventos dispensados: ", trash)

plt.show()