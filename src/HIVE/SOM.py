import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dt
import datetime
import SOM_TNSRFLW as som
from collections import Counter
from scipy import spatial
import room
import device
import pylab



class SelfMaps():
    def __init__(self):
        self.__neurons = 0
        self.__iterations = 0
        self.__ray = 0

    def setNeurons(self, state):
        self.__neurons = state

    def getNeurons(self):
        return self.__neurons

    def setIterations(self, state):
        self.__neurons = state

    def getIterations(self):
        return self.__neurons

    def setRay(self, state):
        self.__neurons = state

    def getRay(self):
        return self.__neurons



