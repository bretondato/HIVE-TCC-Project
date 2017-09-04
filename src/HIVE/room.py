"""
Esta classe representa determinado comodo, possui uma lista de sensores 
e uma lista de atuadores

"""

import math
import numpy
import datetime
import matplotlib.pyplot as plt
import device


class Room():

    def __init__(self):
        self.__nome = ''
        self.__device_name_list = []
        self.__deviceList = []
        self.__eventlist = [[], []]


    def setName(self, name):
        self.__nome = name


    def setSensorsDta(self, lines, i):
        if lines[i][12] + lines[i][13] == '00':
            self.__sensorDta[0].append(lines[i][49] + lines[i][50] + lines[i][51])

        if lines[i][12] + lines[i][13] == '01':
            self.__sensorDta[1].append(lines[i][49] + lines[i][50] + lines[i][51])

        if lines[i][12] + lines[i][13] == '02':
            self.__sensorDta[2].append(lines[i][49] + lines[i][50] + lines[i][51])

        if lines[i][12] + lines[i][13] == '03':
            self.__sensorDta[3].append(lines[i][49] + lines[i][50] + lines[i][51])

        if lines[i][12] + lines[i][13] == '04':
            self.__sensorDta[4].append(lines[i][49] + lines[i][50] + lines[i][51])

        if lines[i][12] + lines[i][13] == '06':
            self.__sensorDta[5].append(lines[i][49] + lines[i][50] + lines[i][51])

        if lines[i][12] + lines[i][13] == '07':
            self.__sensorDta[6].append(lines[i][49] + lines[i][50] + lines[i][51])

        if lines[i][12] + lines[i][13] == '08':
            self.__sensorDta[7].append(lines[i][49] + lines[i][50] + lines[i][51])

        if lines[i][12] + lines[i][13] == '09':
            self.__sensorDta[8].append(lines[i][49] + lines[i][50] + lines[i][51])

        if lines[i][12] + lines[i][13] == '10':
            self.__sensorDta[9].append(lines[i][49] + lines[i][50] + lines[i][51])

        if lines[i][12] + lines[i][13] == '11':
            self.__sensorDta[10].append(lines[i][49] + lines[i][50] + lines[i][51])

        if lines[i][12] + lines[i][13] == '12':
            self.__sensorDta[11].append(lines[i][49] + lines[i][50] + lines[i][51])

        if lines[i][12] + lines[i][13] == '13':
            self.__sensorDta[12].append(lines[i][49] + lines[i][50] + lines[i][51])

        if lines[i][12] + lines[i][13] == '14':
            self.__sensorDta[13].append(lines[i][49] + lines[i][50] + lines[i][51])

        if lines[i][12] + lines[i][13] == '15':
            self.__sensorDta[14].append(lines[i][49] + lines[i][50] + lines[i][51])

        if lines[i][12] + lines[i][13] == '16':
            self.__sensorDta[15].append(lines[i][49] + lines[i][50] + lines[i][51])

        if lines[i][12] + lines[i][13] == '17':
            self.__sensorDta[16].append(lines[i][49] + lines[i][50] + lines[i][51])

        if lines[i][12] + lines[i][13] == '18':
            self.__sensorDta[17].append(lines[i][49] + lines[i][50] + lines[i][51])

        if lines[i][12] + lines[i][13] == '19':
            self.__sensorDta[18].append(lines[i][49] + lines[i][50] + lines[i][51])

        if lines[i][12] + lines[i][13] == '20':
            self.__sensorDta[19].append(lines[i][49] + lines[i][50] + lines[i][51])

        if lines[i][12] + lines[i][13] == '21':
            self.__sensorDta[20].append(lines[i][49] + lines[i][50] + lines[i][51])

        if lines[i][12] + lines[i][13] == '22':
            self.__sensorDta[21].append(lines[i][49] + lines[i][50] + lines[i][51])

        if lines[i][12] + lines[i][13] == '23':
            self.__sensorDta[22].append(lines[i][49] + lines[i][50] + lines[i][51])

        print(self.__nome)
        print(self.__sensorDta)


    def setActuatorsDta(self, actuatorsDta):
        self.__actuatorsDta = actuatorsDta


    def getName(self):
        return self.__nome


    def getSensorsDta(self):
        return self.__sensorDta


    def getActuators(self):
        return self.__actuatorsDta


    def printData(self, time):

        for i in range(0, len(self.__sensorDta)):
            print("i[" + str(i) + "]:")
            print(self.__sensorDta[i])

        plt.plot(self.__sensorDta[time], 'ro')
        ##plt.plot(somInput_S[22], 'ro')
        plt.show()

    def setDeviceList(self, dta):
        self.__deviceList.append(dta)

    def getDeviceList(self):
        return self.__deviceList

    def setDeviceNameList(self, deviceId):
        self.__device_name_list.append(deviceId)

    def getDeviceNameList(self):
        return self.__device_name_list



