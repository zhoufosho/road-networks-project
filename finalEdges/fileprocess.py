import numpy as np
import sys

if __name__ == '__main__':
	with open(sys.argv[1]) as nodef: 
		with open(sys.argv[2]) as edgef:
			with open(sys.argv[3], "w") as op:
				op.write("nodedef>name,label,population DOUBLE,x DOUBLE,y DOUBLE\n")
				for line in nodef:
					arr = line.split();
					op.write(arr[0]+","+arr[0]+",1,"+arr[1]+","+arr[2]+"\n")
				op.write("edgedef>node1,node2,weight DOUBLE,distance DOUBLE, betweenness DOUBLE\n")
				for line in edgef:
					arr = line.split();
					op.write(arr[0]+","+arr[1]+","+arr[3]+","+arr[2]+","+arr[3]+"\n")

 
#turn into:
# 	nodedef>name,label,population DOUBLE,x DOUBLE,y DOUBLE
# 01_001,"Autauga Alabama",54571,-4324.70825,1625.01945
#AFTER, with no line breaks
# edgedef>node1,node2,weight DOUBLE,workers DOUBLE,error DOUBLE
# 01_001,01_001,9.06357899058078,8635,597


	# labels, wordVecsMatrix = word_vecs.get_matrix(word_vecs.load("../data/vectors.txt"))

	# # #runs tsne on wordVecsMatrix (change if we want to just look at some subset of the bigrams)
	# points = tsne.bh_tsne(wordVecsMatrix);
	# np.save("../data/tsne_coordinates", points);