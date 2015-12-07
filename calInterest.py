from snap import *
from scipy.spatial import distance


def printArray(args, f, toPrint):
    f.write("\t".join(args))
    if toPrint:
        print "\t".join(args)


def writeMatrixToFile(f, toPrint=False):
    for i in xrange(numNodes):
        printArray([str(distanceMatrix[i][j]) for j in xrange(numNodes)], f, toPrint)


nodes = {}
count = 0

with open("caldata.txt") as f:
    for line in f:
        r = line.strip('\n').split(' ')
        (lat, lon) = float(r[0]), float(r[1])
        nodes[count] = (lat, lon)
        count += 1

numNodes = len(nodes)
print numNodes
print count

coords = nodes.values()

distanceMatrix = distance.cdist(coords, coords, 'euclidean')

f = open('distanceMatrix-calPointsOfInterest.txt', 'w')
writeMatrixToFile(f)
f.close()
