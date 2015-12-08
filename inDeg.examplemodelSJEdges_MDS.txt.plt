#
# San Joaquin - in-degree Distribution. G(5481, 24099). 2316 (0.4226) nodes with in-deg > avg deg (8.8), 549 (0.1002) with >2*avg.deg (Tue Dec  8 13:53:42 2015)
#

set title "San Joaquin - in-degree Distribution. G(5481, 24099). 2316 (0.4226) nodes with in-deg > avg deg (8.8), 549 (0.1002) with >2*avg.deg"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "In-degree"
set ylabel "Count"
set tics scale 2
set terminal png size 1000,800
set output 'inDeg.examplemodelSJEdges_MDS.txt.png'
plot 	"inDeg.examplemodelSJEdges_MDS.txt.tab" using 1:2 title "" with linespoints pt 6
