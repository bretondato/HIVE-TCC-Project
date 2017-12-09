from flask import Flask, redirect, request, session, g, url_for, abort, render_template, flash
from minisom import MiniSom
import numpy as np
import random
import matplotlib.pyplot as plt
import room
import device
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dt
import datetime
import SOM_TNSRFLW as som
from collections import Counter
from scipy import spatial
app = Flask(__name__)


def readFile(file):
    for w in file:
        print(w)

def setFileNames(diaI, diaF):
    filenames = []
    for i in range(diaI, diaF):
        filenames.append("1-"+ str(i) +"-2005-RAW.data")
    return filenames

@app.route('/')
def hello_world():
    return render_template('layout.html')


@app.route('/network', methods=['POST'])
def setData():
    neuQuant = request.form['neuQuant']
    itQuant = request.form['itQuant']

    initD = request.form['InitD']
    endD = request.form['EndD']
    limt = request.form['limt']
    comodo = request.form['room']

    filenames = setFileNames(int(initD), int(endD))

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

    mu = 0.0000
    mus = []
    std = []
    stds = []

    # and int(lines[u][33] + lines[u][34] + lines[u][35]) == 3

    for i in filedata.values():
        lines = i.readlines()
        # print(lines)
        for u in range(2, len(lines) - 2):
            if lines[u][23] == comodo:
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
                # eventsd.append(ev)
                # eventst.append(dates[i])
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
    net = som.SOM(int(neuQuant), int(neuQuant), 2, int(itQuant))
    net.train(som_in)
    image_grid = net.get_centroids()
    mapped = net.map_vects(som_in)

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

    euclidian_list1 = [((spatial.distance.euclidean(coord, list(image_grid[0][0]))), coord) for coord in clus1]
    euclidianLists.append(euclidian_list1)

    euclidian_list2 = [((spatial.distance.euclidean(coord, list(image_grid[0][1]))), coord) for coord in clus2]
    euclidianLists.append(euclidian_list2)

    euclidian_list3 = [((spatial.distance.euclidean(coord, list(image_grid[1][0]))), coord) for coord in clus3]
    euclidianLists.append(euclidian_list3)

    euclidian_list4 = [((spatial.distance.euclidean(coord, list(image_grid[1][1]))), coord) for coord in clus4]
    euclidianLists.append(euclidian_list4)

    for i in euclidianLists:
        print(i)
        for id, m in enumerate(i):
            e = m[0]
            mu += e
            std.append(e)

        mu = mu / len(i)
        mus.append(mu)
        stdt = np.std(std)
        stds.append(stdt)

    plt.subplot(221)
    for i, m in enumerate(som_in):
        # print(som_in[i][1])
        plt.plot(som_in[i][1], som_in[i][0], 'ro')

    plt.subplot(221)
    for i in range(0, len(image_grid)):
        for j in range(0, len(image_grid[i])):
            plt.plot(image_grid[i][j][1], image_grid[i][j][0], 'bo')

    plt.subplot(221)
    for idx, l in enumerate(euclidianLists):
        for i, m in enumerate(l):
            if m[0] > (mus[idx] + 1 * stds[idx]):
                plt.plot(m[1][1], m[1][0], 'go')

    plt.show()

    return render_template('layout.html')


def somInBuilder(lines, i, somInput):
    if lines[i][12] + lines[i][13] == '00':
        somInput[0].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '01':
        somInput[1].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '02':
        somInput[2].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '03':
        somInput[3].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '04':
        somInput[4].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '06':
        somInput[5].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '07':
        somInput[6].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '08':
        somInput[7].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '09':
        somInput[8].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '10':
        somInput[9].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '11':
        somInput[10].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '12':
        somInput[11].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '13':
        somInput[12].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '14':
        somInput[13].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '15':
        somInput[14].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '16':
        somInput[15].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '17':
        somInput[16].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '18':
        somInput[17].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '19':
        somInput[18].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '20':
        somInput[19].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '21':
        somInput[20].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '22':
        somInput[21].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '23':
        somInput[22].append(lines[i][49] + lines[i][50] + lines[i][51])

    return somInput


def calcDuration():
    for i in range(0, len(val)):
        if val[i] - 100 == - 100:
            ev = dates[i] - dates[i - 1]
            if ev < 0:
                pass
            else:
                # eventsd.append(ev)
                # eventst.append(dates[i])
                event_set.append(ev)
                event_set.append(dates[i])
                som_in.append(event_set)
                event_set = []


if __name__ == '__main__':
    #app.run(debug=True)

    f = open('/Users/brennotondato/GitHub/TCC-HIVE-Project/src/HIVE/sensorsDataset/1-5-2005-RAW.data', 'r')
    lines = f.readlines()

    Room_List_name = []
    Device_List_Name= []

    Room_List = []
    Device_list = []

    somInput_i = []


    for u in range(2, len(lines) - 2):
        room_Reader = lines[u][23]
        device_Reader = int(lines[u][33] + lines[u][34] + lines[u][35])
        value = int(lines[u][49] + lines[u][50] + lines[u][51])
        state = int(lines[u][43])
        time = lines[u][12:20]
        local = lines[u][53:64]

        #print("Room: ", room_Reader)
        #print("device_Reader: ", device_Reader)
        #print("value: ", value)
        #print("State: ", state)
        #print("Time: ", time)
        #print("Local: ", local)


        if room_Reader not in Room_List_name:
            r = room.Room()
            r.setName(room_Reader)
            Room_List.append(r)
            Room_List_name.append(r.getName())


        for i in Room_List:
            if i.getName() == room_Reader and device_Reader not in i.getDeviceNameList():
                d = device.Device()
                d.setId(device_Reader)
                i.setDeviceList(d)
                i.setDeviceNameList(d.getId())
                Device_List_Name.append(d.getId())

            for j in i.getDeviceList():
                if device_Reader == j.getId() and i.getName() == room_Reader:

                    if local == '| ArgusMS |':
                        #s = device.Sensor()
                        #s.setValue(value)
                        #s.setTimeS(time)
                        #j.setEventlist(s)
                        pass
                    else:
                        e = device.Actuator()
                        e.setState(state)
                        ev = j.convertTimeToEvent(time)
                        e.setTimeA(ev)
                        j.setEventlist(e)


    for i in Room_List:
        print(i.getName())
        for j in i.getDeviceList():
            print(j.getId())
            for k in j.getEventList():
                print(k.getTimeA())
                print(k.getState())
                #print(k.getTimeS())
                print()


