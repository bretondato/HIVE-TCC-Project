import numpy
import datetime

class Sensor():
    def __init__(self):
        self.__value = 0
        self.__timeS = ""

    def setValue(self, value):
        self.__value = value

    def getValue(self):
        return self.__value

    def setTimeS(self, time):
        self.__timeS = time

    def getTimeS(self):
        return self.__timeS


class Actuator():
    def __init__(self):
        self.__event_duration = 0.0
        self.__timeA = ''
        self.__endTime = ''

    def setEvent(self, event_duration):
        self.__event_duration = event_duration

    def getEvent(self):
        return self.__event_duration

    def setTimeA(self, time):
        self.__timeA = time

    def getTimeA(self):
        return self.__timeA

    def setEndTime(self, endTime):
        self.__endTime = endTime

    def getEndTime(self):
        return self.__endTime

    def calcEvent(self):
        date = datetime.datetime.strptime(self.__timeA, "%H:%M:%S")
        end_date = datetime.datetime.strptime(self.__endTime, "%H:%M:%S")
        self.__event_duration = ((end_date-date).total_seconds() / 60)


class Device(Sensor, Actuator):
    def __init__(self):
        self.__id = ''
        self.__day = ''
        self.__eventList = []


    def setId(self, id):
        self.__id = id

    def setTime(self, time):
        self.__intTime = time

    def setDuration(self, duration):
        self.__duration = duration

    def getId(self):
        return self.__id

    def getTime(self):
        return self.__intTime

    def setEventlist(self, dta):
        self.__eventList.append(dta)

    def getEventList(self):
        return self.__eventList

