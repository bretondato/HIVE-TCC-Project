import numpy
import datetime

class Sensor():
    def __init__(self):
        self.__timeS = ""
        self.__value = 0


    def setTimeS(self, time):
        self.__timeS = time

    def getTimeS(self):
        return self.__timeS

    def setValue(self, value):
        self.__value = value

    def getValue(self):
        return self.__value



class Actuator():
    def __init__(self):
        self.__timeA = ''
        #self.__endTime = ''
        self.__state = 0

    #def setEvent(self, event_duration):
    #   self.__event_duration = event_duration

    #def getEvent(self):
     #   return self.__event_duration

    def setTimeA(self, time):
        self.__timeA = time

    def getTimeA(self):
        return self.__timeA

    #def setEndTime(self, endTime):
     #   self.__endTime = endTime

    #def getEndTime(self):
     #   return self.__endTime

    def setState(self, state):
        self.__state = state

    def getState(self):
        return self.__state

    #def calcEvent(self):
    #    date = datetime.datetime.strptime(self.__timeA, "%H:%M:%S")
    #    end_date = datetime.datetime.strptime(self.__endTime, "%H:%M:%S")
    #    self.__event_duration = ((end_date-date).total_seconds() / 60)


class Device():
    def __init__(self):
        self.__id = ''
        self.__state = 0
        self.__eventList = []


    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setEventlist(self, dta):
        self.__eventList.append(dta)

    def getEventList(self):
        return self.__eventList


