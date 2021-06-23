import numpy as np
from numpy.polynomial import Polynomial as P
import matplotlib.pyplot as plt
def plotMeasure(fileName):
    file = open(f"./datasources/{fileName}.txt", 'r')
    nums = list(map(float, file.read()[:-1].split()))
    x = [xi for xi in range(10 ** 1, 10 ** 1 + 1000 * len(nums), 1000)]
    y = nums

    plt.plot(x,y)
    plt.savefig(f"./plots/{fileName}.png")
    plt.clf()
def plotMeasureDijkstraA():
    file = open(f"./datasources/dijkstraA.txt", 'r')
    nums = list(map(float, file.read()[:-1].split()))
    x = [xi for xi in range(10 ** 3, 10 ** 3 + 1000 * len(nums), 1000)]
    y = nums

    plt.plot(x,y)
    plt.savefig(f"./plots/{fileName}.png")
    plt.clf()
# dijkstraA 10 ** 3, 10 ** 3 + 1000 * len(nums), 1000)
toPlot = [
    "dijkstraB", # 10 ** 1, 10 ** 1 + 1000 * len(nums), 1000)
    "bellmanFordA", # 10 ** 1, 10 ** 1 + 1000 * len(nums), 1000)
    "bellmanFordB" # 10 ** 1, 10 ** 1 + 1000 * len(nums), 1000)
]
for name in toPlot:
    plotMeasure(name )
plotMeasureDijkstraA()