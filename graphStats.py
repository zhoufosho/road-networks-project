from snap import *
import matplotlib.pyplot as plt
import numpy as np


# files = [
#     'modelOLEdges_lambda1.txt',
#     'modelOLEdges_lambda2.txt',
#     'modelOLEdges_lambda3.txt',
#     'modelOLEdges_lambda4.txt'
# ]

files = [
    'modelSJEdges_lambda1.txt',
    'modelSJEdges_lambda2.txt',
    'modelSJEdges_lambda3.txt'
]

lambdas = [0.001, 0.01, 1, 2, 3, 4]
lambdaDim2 = [1, 2, 3]

sccSz = []
effDiams = []
fullDiams = []
triads = []
clustcffs = []

count = 0

values = {}

for f in ['SJdata.txt']:
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

    values[count] = [size, fullDiam, triad, clustcff]
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

    values[count] = [size, fullDiam, triad, clustcff]
    print values[count]
    count += 1

N = len(values[0])

ind = np.arange(N)  # the x locations for the groups
width = 0.18       # the width of the bars

colors = ['r', 'b', 'g', 'y']

fig, ax = plt.subplots()

for x in xrange(4):
    rects = ax.bar(ind + x*width, values[x], width, color=colors[x])


# add some text for labels, title and axes ticks
ax.set_xticks(ind + width)
ax.set_xticklabels(('MxSccSz', 'BfsFullDiam', 'Triads', 'ClustCf'))
ax.legend(('original', 'lambda = 0.01', 'lambda = 0.1', 'lambda = 1'))
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
