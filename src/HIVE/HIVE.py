from flask import Flask
from minisom import MiniSom
import numpy as np
import random
import matplotlib.pyplot as plt
import room
import device

app = Flask(__name__)


def readFile(file):
    for w in file:
        print(w)

@app.route('/')
def hello_world():
    return 'Hello World!'


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


if __name__ == '__main__':
    #app.run()
    f = open('1-3-2005-RAW.data', 'r')
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
        #print(local)

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
                        e.setTimeA(time)
                        j.setEventlist(e)

    """
    for i in Room_List:
        print(i.getName())
        for j in i.getDeviceList():
            print(j.getId())
            for k in j.getEventList():
                print(k.getTimeA())
                print(k.getState())
                #print(k.getTimeS())
                print()
    """




