from snap import *
import operator

#for original and 3 created OL graphs, make 3 tiers with edge betweenness cutoff

source_filename="modelOLEdges_lambda1.txt"
#iterate over all values of lambda1 in different files. 
Graph =LoadEdgeList(PUNGraph,source_filename, 0, 1)
MxWcc = GetMxWcc(Graph)

maxbetctr = [(None, None)] * 20 #node, value
fillcounter = 0
Nodes = TIntFltH()
Edges = TIntPrFltH()
GetBetweennessCentr(MxWcc, Nodes, Edges, 1.0)

edgemap = []
for edge in Edges:
	edgemap.append(((edge.GetVal1(), edge.GetVal2()),Edges[edge]))
sorted_edgemap = sorted(edgemap, key=lambda x: x[1], reverse=True)

alledges = {}
with open(source_filename) as f:
	for line in f:
		vals=line.split()
		alledges[(int(vals[0]), int(vals[1]))]=float(vals[2])



for i in [1, 2, 4, 10]:
	filename = "betw_centr_hierarchies/"+source_filename[:-4] + "_TO_top_1d" + str(i)+".txt"
	with open(filename, 'w+') as file:
		file.write("from to distance betweenness\n")
		for k in range(0, len(sorted_edgemap)/i):
			strres=str(sorted_edgemap[k][0][0])+" "+str(sorted_edgemap[k][0][1])+" "+str(alledges[sorted_edgemap[k][0]])+" "+str(sorted_edgemap[k][1])+"\n"
			file.write(strres)


# if we are curious about nodes as well:
# for node in Nodes:
#         if fillcounter < 20:
#                 maxbetctr[fillcounter]=(node, Nodes[node])
#                 fillcounter+=1
#         else:
#                 min_index, min_value = min(enumerate(maxbetctr), key=lambda t:t[1][1])
#                 if min_value[1]<Nodes[node]:
#                         maxbetctr[min_index]=(node, Nodes[node])
# print sorted(maxbetctr, key=lambda t:t[1])
