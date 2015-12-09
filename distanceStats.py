from snap import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

orig = [
    'oldenburgEdges.txt',
    'SJdata.txt'
]

files = [
    'modelOLEdges_MDS.txt',
    'modelOLEdges_ISO.txt',
    'modelOLEdges_MDS_rand.txt',
    'modelOLEdges_ISO_rand.txt',
    'modelOLEdges_MDS_hopScaled.txt'
]


ROUND_TO = 1


def round_to_value(number, roundto):
    return (round(number / roundto) * roundto)


def getOrigDistances(filename):
    distances = {}  # dict from node id to [lat, long]
    with open(filename) as f:
        for line in f:
            values = line.strip('\n').split(' ')
            d = round_to_value(float(values[3]), ROUND_TO)
            if not d in distances:
                distances[d] = 0
            distances[d] += 1

    maxD = max(distances.values())
    for d in distances:
        new_key = float(d) / len(distances.keys())
        distances[new_key] = distances.pop(d)
        distances[new_key] = float(distances[new_key]) / maxD

    return distances


def getDistances(filename):
    distances = {}  # dict from node id to [lat, long]
    with open(filename) as f:
        for line in f:
            values = line.strip('\n').split('\t')
            d = round_to_value(float(values[2]), ROUND_TO)
            if not d in distances:
                distances[d] = 0
            distances[d] += 1

    maxD = max(distances.values())
    for d in distances:
        new_key = float(d) / len(distances.keys())
        distances[new_key] = distances.pop(d)
        distances[new_key] = float(distances[new_key]) / maxD

    return distances


def expFunc(x, a, b):
    return a * np.power(x, b)


colors = ['r', 'b', 'g', 'y', 'c', 'm']
d = getOrigDistances(orig[0])
plt.scatter(d.keys(), d.values(), c=colors[0])


for x in xrange(len(files)):
    f = files[x]
    d = getDistances(f)
    plt.scatter(d.keys(), d.values(), c=colors[x+1])

    newX = np.logspace(-1, 2, base=10)
    popt, pcov = curve_fit(expFunc, d.keys(), d.values())
    # plt.plot(newX, expFunc(newX, *popt), c=colors[x+1])

plt.xlabel('Path Length / Diameter')
plt.ylabel('Relative Frequency')

axes = plt.gca()
axes.set_ylim([0, 1])
plt.xscale('log')
plt.legend(('original', 'MDS', 'ISO', 'MDS + Random', 'ISO + Random', 'Hop Scaled'))

plt.show()
