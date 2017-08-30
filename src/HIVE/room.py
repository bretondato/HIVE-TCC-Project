"""
Esta classe representa determinado comodo, possui uma lista de sensores 
e uma lista de atuadores

"""

import math
import numpy

class Room():

    def __init__(self):
        self.__nome = ''

        self.__sensorDta = [[], [], [], [], [], [],
                            [], [], [], [], [], [],
                            [], [], [], [], [], [],
                            [], [], [], [], [], []]

        self.__actuatorsDta = [[], [], [], [], [], [],
                            [], [], [], [], [], [],
                            [], [], [], [], [], [],
                            [], [], [], [], [], []]



    def setName(self, name):
        self.__nome = name


    def setSensorsDta(self, sensorsDta):
        self.__sensorDta = sensorsDta


    def setActuatorsDta(self, actuatorsDta):
        self.__actuatorsDta = actuatorsDta


    def getName(self):
        return self.__nome


    def getSensorsDta(self):
        return self.__sensorDta


    def getActuators(self):
        return self.__actuatorsDta




