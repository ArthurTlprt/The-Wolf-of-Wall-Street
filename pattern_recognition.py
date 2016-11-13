import matplotlib.pyplot as plt
import pylab as pl
import numpy as np
import pandas as pd


df = pd.read_csv('GOOG.csv', names=['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'])

def percentChange(startPoint, currentPoint):
    return (float(currentPoint)-startPoint/startPoint) * 100

def patternFinder():

def draw():
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    x = df['Close'][1:]
    ax1.plot(x, color='r', label='the data frame')

    plt.gca().invert_xaxis()
    plt.show()

    variations = []
    x = list(map(float, x))
    for i,item in enumerate(x):
        print(item - x[i+1])

def main():
    draw()

if __name__ == '__main__':
    main()
