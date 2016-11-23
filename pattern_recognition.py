import matplotlib.pyplot as plt
import matplotlib
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import time
from numpy import loadtxt
from matplotlib import style
style.use("ggplot")

import matplotlib.dates as mdates

startTime = time.time()

def bytedate2num(fmt):
    def converter(b):
        return mdates.strpdate2num(fmt)(b.decode('ascii'))
    return converter

date_converter = bytedate2num("%Y%m%d%H%M%S")



date,bid,ask = np.loadtxt('GBPUSD1d.txt', unpack=True,delimiter=',',converters={0: date_converter})

patternAr = []
performanceAr = []
avgLine = ((bid+ask)/2)
patForRec = []


def patternRecognition():
    for eachPattern in patternAr:
        sim = []
        for i in range(10):
            sim.append(100.00 - abs(percentChange(eachPattern[i], patForRec[i])))
        howSim = sum(sim)/10.00
        if howSim > 70:
            patdex = patternAr.index(eachPattern)
            print("#######################################")
            print(patForRec)
            print("=======================================")
            print(eachPattern )
            print("=======================================")
            print("predicted outcome", performanceAr[patdex])
            xp = range(1, 11)
            print("#######################################")


def currentPattern():
    for i in range(10):
        patForRec.append(percentChange(avgLine[-11], avgLine[i-10]))
    print(patForRec)

def percentChange(startPoint,currentPoint):
    return ((currentPoint-startPoint)/abs(startPoint))*100.00


def patternStorage():
    patStartTime = time.time()
    x = len(avgLine)-30

    y = 11
    while y < x:
        p = []
        pattern = []
        for i in reversed(range(10)):
            p.append(percentChange(avgLine[y-10], avgLine[y-i]))
        outcomeRange = avgLine[y+20:y+30]
        currentPoint = avgLine[y]
        avgOutcome = sum(outcomeRange) / len(outcomeRange)
        futureOutcome = percentChange(currentPoint, avgOutcome)
        pattern += p
        patternAr.append(pattern)
        performanceAr.append(futureOutcome)
        y+=1
    patEndTime = time.time()
    print( len(patternAr) )
    print( len(performanceAr) )
    print('pattern finder took :', patEndTime - patStartTime, ' seconds')

def graphRawFX():

    fig=plt.figure(figsize=(10,7))

    ax1 = plt.subplot2grid((40,40), (0,0), rowspan=40, colspan=40)
    ax1.plot(date,bid)
    ax1.plot(date,ask)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    #####
    plt.grid(True)
    for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(45)
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)

    #######
    ax1_2 = ax1.twinx()

    ax1_2.plot(date, (ask-bid))

    ax1_2.fill_between(date, 0, (ask-bid), facecolor='g',alpha=.3)

    ax1_2.set_ylim(0, 3*ask.max())
    #######

    plt.subplots_adjust(bottom=.23)
    #plt.grid(True)

    plt.show()



patternStorage()
currentPattern()
patternRecognition()
endTotaltime = time.time()
print(endTotaltime-startTime)
# video 9...
