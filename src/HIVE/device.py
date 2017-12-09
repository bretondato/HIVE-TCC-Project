import numpy
import datetime
import matplotlib.dates as dt

class Actuator():
    def __init__(self):
        self.__timeA = ''
        self.__state = 0
        self.__durationA = ''

    def setTimeA(self, time):
        self.__timeA = time

    def getTimeA(self):
        return self.__timeA

    def setState(self, state):
        self.__state = state

    def getState(self):
        return self.__state

    def setDuration(self, durarion):
        self.__durationA =  durarion

    def getDuration(self):
        return self.__durationA

class Device():
    def __init__(self):
        self.__id = ''
        self.__state = []
        self.__eventList = []
        self.__trash = 0
        self.__timeList = []
        self.__durationList = []
        self.__time = 0
        self.__duration = 0
        self.__SomIn = []
        self.__data = []


    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setState(self, state):
        self.__state.append(state)

    def getState(self):
        return self.__state

    def setEventlist(self, dta):
        self.__eventList.append(dta)

    def getEventList(self):
        return self.__eventList

    def setTime(self, time):
        self.__timeList.append(time)

    def getTime(self):
        return self.__timeList

    def setDuration(self, duration):
        self.__durationList.append(duration)

    def getDuration(self):
        return self.__durationList

    def emptyDurationList(self):
        self.__durationList = []

    def setTrash(self):
        self.__trash = self.__trash + 1

    def getTrash(self):
        return self.__trash

    def getTimeAtIndex(self, index):
        return self.__timeList[index]

    def getEventAtIndex(self, index):
        return self.__eventList[index]

    def setSomIn(self, dta):
        self.__SomIn.append(dta)

    def getSomIn(self):
        return self.__SomIn

    def setData(self, dta):
        self.__data.append(dta)

    def getData(self):
        return self.__data

    def convertTimeToEvent(self, time):
        eValue = dt.datestr2num(time)
        return eValue