from snap import *


nodes = {}  # dict from node id to [lat, long]
with open("roadNodes.txt") as f:
    for line in f:
        values = line.strip('\n').split(' ')
        (key, lat, lon) = values[0], values[1], values[2]
        nodes[int(key)] = [lat, lon]

edgeDistances = {}  # dict from edge id to distance
with open("roadEdges.txt") as f:
    for line in f:
        values = line.strip('\n').split(' ')
        (edge, dist) = values[0], values[3]
        edgeDistances[int(edge)] = dist

Graph = LoadEdgeList(PNGraph, "roadEdges.txt", 1, 2)
print nodes[10]
print edgeDistances[18]
