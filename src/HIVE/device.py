import numpy
import datetime


class Device():
    def __init__(self):
        self.__id = ''
        self.__intTime = 0
        self.__duration = 0

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


