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
        somInput[12].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '01':
        somInput[12].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '02':
        somInput[12].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '03':
        somInput[12].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '04':
        somInput[12].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '06':
        somInput[12].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '07':
        somInput[12].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '08':
        somInput[12].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '09':
        somInput[12].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '10':
        somInput[12].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '11':
        somInput[12].append(lines[i][49] + lines[i][50] + lines[i][51])

    if lines[i][12] + lines[i][13] == '12':
        somInput[12].append(lines[i][49] + lines[i][50] + lines[i][51])

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
    #data = np.genfromtxt('iris.csv', delimiter=',', usecols=(0, 1, 2, 3))

    n = 3333
    print(lines[12][23])
    print(lines[12][12] + lines[12][13])
    # print(somInput[12])

    value_i = 0
    values_i = []
    somInput_i = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    #somInput_i = np.zeros((24, 0))
    print(somInput_i)


    value_S = 0
    values_S = []
    somInput_S = [[], [], [], [], [], [], [], [], [], [], [], [],
                [], [], [], [], [], [], [], [], [], [], [], []]


    value_a = 0
    values_a = []
    somInput_a = [[], [], [], [], [], [], [], [], [], [], [], [],
                [], [], [], [], [], [], [], [], [], [], [], []]


    value_c = 0
    values_c = []
    somInput_c = [[], [], [], [], [], [], [], [], [], [], [], [],
                [], [], [], [], [], [], [], [], [], [], [], []]


    value_v = 0
    values_V = []
    somInput_V = [[], [], [], [], [], [], [], [], [], [], [], [],
                [], [], [], [], [], [], [], [], [], [], [], []]


    value_b = 0
    values_b = []
    somInput_b = [[], [], [], [], [], [], [], [], [], [], [], [],
                [], [], [], [], [], [], [], [], [], [], [], []]


    # values = np.random.rand(24,10)
    # print(values)


    for i in range(0, len(lines) - 2):
        if lines[i][23] == 'i':
            #value_i = (lines[i][49] + lines[i][50] + lines[i][51])
            #alues_i.append(int(value_i))
            somInput_i = somInBuilder(lines, i, somInput_i)


        if (lines[i][23] == 'S'):
            #value_S = (lines[i][49] + lines[i][50] + lines[i][51])
            #values_S.append(int(value_S))
            somInput_S = somInBuilder(lines, i, somInput_S)

        if (lines[i][23] == 'a'):
            #value_a = (lines[i][49] + lines[i][50] + lines[i][51])
            #values_a.append(int(value_a))
            somInput_a = somInBuilder(lines, i, somInput_a)

        if (lines[i][23] == 'c'):
            #value_c = (lines[i][49] + lines[i][50] + lines[i][51])
            #values_c.append(int(value_c))
            somInput_c = somInBuilder(lines, i, somInput_c)

        if (lines[i][23] == 'V'):
            somInput_V = somInBuilder(lines, i, somInput_V)


        if (lines[i][23] == 'b'):
            #value_b = (lines[i][49] + lines[i][50] + lines[i][51])
            #values_b.append(int(value_b))
            somInput_b = somInBuilder(lines, i, somInput_b)


    for i in range(0, len(somInput_S)):
        print("i["+ str(i) +"]:")
        print(somInput_S[i])


    plt.plot(somInput_S[21], 'ro')
    #plt.plot(somInput_S[22], 'ro')
    plt.show()

