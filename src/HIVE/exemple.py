import datetime
from minisom import MiniSom

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as dt
import datetime

# FILES = []
# FILES = f = open('2-6-2005-RAW.data', 'r')
# FILES = f2 = open('2-7-2005-RAW.data', 'r')
# FILES = f3 = open('2-8-2005-RAW.data', 'r')

f = open('1-4-2005-RAW.data', 'r')

i = 3
j = 26251
# j = [00, 01, 03, 04, 05, 06, 07]
dta = []
hour = []
day = []
list_of_days = []
val = []
list_of_datetimes = []
aux = []
eventst = []
eventsd = []
dates = []

lines = f.readlines()
for u in range(2, len(lines) - 2):
    if lines[u][23] == 'i' and int(lines[u][33] + lines[u][34] + lines[u][35]) == 5:
        # print(lines)
        value = int(lines[u][49] + lines[u][50] + lines[u][51])
        date = lines[u][12:20]
        list_of_datetimes.append(date)
        val.append(value)

print("value: ", val)
print("Time: ", list_of_datetimes)

#for i in range(0, len(list_of_datetimes)):
 #   dates[i] = dt.datestr2num(list_of_datetimes[i])

for i in dates:
    print(i)

for i in range(0, len(val)):
    if val[i] - 100 == -100:
        ev = dates[i] - dates[i - 1]
        eventsd.append(ev)
        eventst.append(dates[i])

# v = [values, dates]



# print(val)
# print(dates)

print("event t", eventst)
print("event d", eventsd)
print("value: ", val)
print("Time: ", dates)

plt.plot(eventst, eventsd, 'ro')
# plt.plot(eventst, eventsd)
plt.show

