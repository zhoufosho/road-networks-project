from snap import *
import matplotlib.pyplot as plt
import numpy as np


orig = [
    'oldenburgEdges.txt',
    'SJdata.txt'
]

# files = [
#     'modelOLEdges_MDS.txt',
#     'modelOLEdges_ISO.txt'
# ]

files = [
    'modelSJEdges_MDS.txt',
    'modelSJEdges_ISO.txt'
]

lambdas = [1, 2, 3]

sccSz = []
effDiams = []
fullDiams = []
triads = []
clustcffs = []

count = 0

values = {}

for f in [orig[1]]:
    Graph = LoadEdgeList(PUNGraph, f, 1, 2)
    size = GetMxSccSz(Graph)
    sccSz.append(size)
    effDiam = GetBfsEffDiam(Graph, 100, False)
    effDiams.append(effDiam)
    fullDiam = GetBfsFullDiam(Graph, 100, False)
    fullDiams.append(fullDiam)
    triad = GetTriads(Graph, 100)
    triads.append(triad)
    clustcff = GetClustCf(Graph, -1)
    clustcffs.append(clustcff)

    PlotInDegDistr(Graph, f, "San Joaquin - in-degree Distribution")

    values[count] = [size, effDiam, triad, clustcff]
    print values[count]
    count += 1


for f in files:
    Graph = LoadEdgeList(PUNGraph, f, 0, 1, '\t')
    size = GetMxSccSz(Graph)
    sccSz.append(size)
    effDiam = GetBfsEffDiam(Graph, 100, False)
    effDiams.append(effDiam)
    fullDiam = GetBfsFullDiam(Graph, 100, False)
    fullDiams.append(fullDiam)
    triad = GetTriads(Graph, 100)
    triads.append(triad)
    clustcff = GetClustCf(Graph, -1)
    clustcffs.append(clustcff)

    PlotInDegDistr(Graph, f, "San Joaquin - in-degree Distribution")

    # connectedness, avg. shortest path, triad, cluster
    values[count] = [size, effDiam, triad, clustcff]
    print values[count]
    count += 1

N = len(values[0])

ind = np.arange(N)  # the x locations for the groups
width = 0.18       # the width of the bars

colors = ['r', 'b', 'g', 'y']

fig, ax = plt.subplots()

for x in xrange(len(lambdas)):
    rects = ax.bar(ind + x*width, values[x], width, color=colors[x])


# add some text for labels, title and axes ticks
ax.set_xticks(ind + width)
ax.set_xticklabels(('MxSccSz', 'BfsFullDiam', 'Triads', 'ClustCf'))
ax.legend(('original', 'MDS', 'ISO'))
ax.set_yscale('log')
plt.ylabel('Magnitude of Parameter')
plt.xlabel('Network Properties')
plt.show()
# plt.scatter(lambdas, effDiams, label=lambdas)
# plt.xlabel('Lambda Value')
# plt.ylabel('Diameter')
# plt.legend()
# plt.show()

# plt.scatter(lambdas, fullDiams, label=lambdas)
# plt.xlabel('Lambda Value')
# plt.ylabel('Diameter')
# plt.legend()
# plt.show()
