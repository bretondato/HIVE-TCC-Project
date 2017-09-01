from flask import Flask
from minisom import MiniSom
import numpy as np
import random
import matplotlib.pyplot as plt
import room

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
    f = open('1-4-2005-RAW.data', 'r')
    #f = open('2-6-2005-RAW.data', 'r')
    lines = f.readlines()

    somInput_i = [[], [], [], [], [], [],
                [], [], [], [], [], [],
                [], [], [], [], [], [],
                [], [], [], [], [], []]

    n = 3333
    print(lines[12][23])
    print(lines[12][12] + lines[12][13])
    # print(somInput[12])

    i = room.Room()
    s = room.Room()
    a = room.Room()
    c = room.Room()
    v = room.Room()
    b = room.Room()

    for u in range(0, len(lines) - 2):

        if (lines[u][23] == 'i'):
            #i = room.Room()
            #i.setName(lines[u][23])
            #i.setSensorsDta(lines, u)
            #somInBuilder(lines, i, somInput_i)
            pass


        if (lines[u][23] == 'S'):
            #s = room.Room()
            #s.setName(lines[u][23])
            #s.setSensorsDta(lines, u)
            #somInBuilder(lines, u, somInput)
            pass

        if (lines[u][23] == 'a'):
            #a = room.Room()
            #a.setName(lines[u][23])
            #a.setSensorsDta(lines, u)
            #somInBuilder(lines, u, somInput)
            somInBuilder(lines, u, somInput_i)

        if (lines[u][23] == 'c'):
            #c = room.Room()
            #c.setName(lines[u][23])
            #c.setSensorsDta(lines, u)
            #somInBuilder(lines, u, somInput)
            pass

        if (lines[u][23] == 'V'):
            #v = room.Room()
            #v.setName(lines[u][23])
            #v.setSensorsDta(lines, u)
            #somInBuilder(lines, u, somInput)
            pass

        if (lines[u][23] == 'b'):
            #b = room.Room()
            #b.setName(lines[u][23])
            #b.setSensorsDta(lines, u)
            #somInBuilder(lines, u, somInput)
            pass


    #i.printData()
    print(i.getName())
    print(a.getName())
    print(somInput_i)

