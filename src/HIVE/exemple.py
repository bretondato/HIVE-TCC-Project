import datetime
from minisom import MiniSom

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dt
import datetime

filenames = ['1-3-2005-RAW.data', '1-4-2005-RAW.data', '1-5-2005-RAW.data', '1-6-2005-RAW.data', '1-7-2005-RAW.data', '1-8-2005-RAW.data',
             '1-9-2005-RAW.data', '1-10-2005-RAW.data', '1-11-2005-RAW.data', '1-12-2005-RAW.data', '1-13-2005-RAW.data', '1-14-2005-RAW.data',
             '1-15-2005-RAW.data', '1-16-2005-RAW.data', '1-17-2005-RAW.data', '1-18-2005-RAW.data', '1-19-2005-RAW.data', '1-20-2005-RAW.data',
             '1-21-2005-RAW.data', '1-22-2005-RAW.data', '1-23-2005-RAW.data', '1-24-2005-RAW.data', '1-25-2005-RAW.data', '1-26-2005-RAW.data',
             '1-27-2005-RAW.data', '1-28-2005-RAW.data', '1-29-2005-RAW.data', '1-30-2005-RAW.data', '1-31-2005-RAW.data']

filedata = {filename: open(filename, 'r') for filename in filenames}

# f = open('2-8-2005-RAW.data', 'r')

# lines = f.readlines()

i = 3
j = 26251

dta = []
hour = []
day = []
list_of_days = []
val = []
list_of_datetimes = []
aux = []
eventst = []
eventsd = []

for i in filedata.values():
    lines = i.readlines()
    #print(lines)
    for u in range(2, len(lines) - 2):
        if lines[u][23] == 'i' and int(lines[u][33] + lines[u][34] + lines[u][35]) == 3:
            # print(lines)
            value = int(lines[u][49] + lines[u][50] + lines[u][51])
            date = lines[u][12:20]
            list_of_datetimes.append(date)
            val.append(value)


# for i in range(0, len(list_of_datetimes)):
dates = dt.datestr2num(list_of_datetimes)

for i in range(0, len(val)):
    if val[i] - 100 == -100:
        ev = dates[i] - dates[i - 1]
        if ev < 0:
            pass
        else:
            eventsd.append(ev)
            eventst.append(dates[i])

# v = [values, dates]



# print(val)
# print(dates)



print("event t", eventst)
print("event d", eventsd)
print("Time: ", list_of_datetimes)
print()
print("value: ", val)
print("Time: ", dates)

plt.plot(eventst, eventsd, 'ro')
plt.show()