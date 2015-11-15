from snap import *
import pdb


def readRoadNodes():
    nodes = {}  # dict from node id to [lat, long]
    with open("roadNodes.txt") as f:
        for line in f:
            values = line.strip('\n').split(' ')
            (key, lat, lon) = values[0], values[1], values[2]
            nodes[int(key)] = [lat, lon]
    return nodes


def getPathLen(path):
    pathLen = 0
    for x in xrange(len(path) - 1):
        pathLen += nodeDistances[(path[x], path[x+1])]
    return pathLen


# BFS approach to find shortest
def shortestPath(start, end, path=[], pathQueue=[]):
    path = path + [start]
    pathQueue = pathQueue + [path]

    while(len(pathQueue)):
        path = pathQueue.pop(0)
        start = path[-1]

        for next in nodeMap[start]:
            if next == end:
                return path + [next]

            if next not in path:
                pathQueue = pathQueue + [path + [next]]

    return None


def printArray(args, f, toPrint):
    f.write("\t".join(args))
    if toPrint:
        print "\t".join(args)


def writeMatrixToFile(f, toPrint=False):
    for i in xrange(numNodes):
        printArray([str(distanceMatrix[i][j]) for j in xrange(numNodes)], f, toPrint)


edgeDistances = {}  # from edge id to distance
nodeMap = {}  # from node id to set of node neighbors
nodeDistances = {}  # from (n1, n2) to distance

with open("roadEdges.txt") as f:
    for line in f:
        r = line.strip('\n').split(' ')
        (edge, dist) = r[0], r[3]
        edgeDistances[int(edge)] = dist

        if not int(r[1]) in nodeMap:
            nodeMap[int(r[1])] = []
        if not int(r[2]) in nodeMap:
            nodeMap[int(r[2])] = []

        nodeMap[int(r[2])].append(int(r[1]))
        nodeMap[int(r[1])].append(int(r[2]))

        nodeDistances[(int(r[1]), int(r[2]))] = float(r[3])
        nodeDistances[(int(r[2]), int(r[1]))] = float(r[3])

# Graph = LoadEdgeList(PNGraph, "roadEdges.txt", 1, 2)

numNodes = 35

distanceMatrix = [[0 for x in xrange(numNodes)] for y in xrange(numNodes)]

for n1 in xrange(numNodes - 1):
    for n2 in range(n1 + 1, numNodes):
        if(n1, n2) in nodeDistances.keys():
            distanceMatrix[n1][n2] = nodeDistances[(n1, n2)]
            distanceMatrix[n2][n1] = nodeDistances[(n1, n2)]
        else:
            shortest = shortestPath(n1, n2)
            if shortest:
                distanceMatrix[n1][n2] = getPathLen(shortest)
                distanceMatrix[n2][n1] = getPathLen(shortest)

f = open('distanceMatrix.txt', 'w')
writeMatrixToFile(f)
f.close()
