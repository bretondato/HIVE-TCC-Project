import numpy
import datetime



class Device():

    def __init__(self):
        self.__id = ''
        self._initH = 0
        self._initM = 0
        self._initS = 0
        self.__intTime = datetime.time(self._initH, self._initM, self._initS)
        self.__duration = 0
        self.__list = []


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

    def getDuration(self):
        return self.__duration


