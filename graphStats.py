from snap import *
import matplotlib.pyplot as plt
import numpy as np


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

# files = [
#     'modelSJEdges_MDS.txt',
#     'modelSJEdges_ISO.txt'
# ]

avgPaths = [40.69, 3.35, 7.21, 12.93, 5.47, 28.95]

sccSz = []
effDiams = []
fullDiams = []
triads = []
clustcffs = []

count = 0

values = {}

for f in [orig[0]]:
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

    PlotInDegDistr(Graph, f, "Oldenburg - Degree Distribution")

    values[count] = [size, effDiam, triad, clustcff, avgPaths[count]]
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

    PlotInDegDistr(Graph, f, "Oldenburg - Degree Distribution")

    # connectedness, avg. shortest path, triad, cluster
    values[count] = [size, effDiam, triad, clustcff, avgPaths[count]]
    print values[count]
    count += 1

N = len(values[0])

ind = np.arange(N)  # the x locations for the groups
width = 0.12       # the width of the bars

colors = ['r', 'b', 'g', 'y', 'c', 'm', 'darkgoldenrod']

fig, ax = plt.subplots()


# vs = [[1.0, 57.73159115887166, 0, 0.010799890799890808, 104, 40.69, 1.0],
#         [0.022527863410007114, 5.231395348837211, 96, 0.20862239902912197, 17, 3.35, 0.01556],
#         [0.07970647773279352, 18.578400000000002, 82, 0.15606829064928954, 33, 7.21, 0.051605],
#         [0.7849757332770627, 17.606962761830875, 46, 0.12820041094859724, 35, 12.93, 0.609436],
#         [0.7981220657276995, 14.349562104942505, 37, 0.0766123710923304, 18, 5.47, 0.6127129],
#         [0.44983310426075007, 55.162237174095885, 13, 0.06191569082792315, 79, 28.95, 0.375327]]


# for x in xrange(len(files) + 1):
#     values[x].append(avgPaths[x])


for x in xrange(len(files) + 1):
    rects = ax.bar(ind + x*width, values[x], width, color=colors[x])


# add some text for labels, title and axes ticks
ax.set_xticks(ind + width)
ax.set_xticklabels(('Percent SCC', 'Diameter', 'Triads', 'ClustCf', 'AvgPathLen'), fontsize='large')
plt.legend(('original', 'MDS', 'ISO', 'MDS + Random', 'ISO + Random', 'Hop Scaled', 'bad lambda'), loc=2)
ax.set_yscale('log')
plt.ylabel('Magnitude of Parameter', fontsize='large')
plt.xlabel('Network Properties', fontsize='large')
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
