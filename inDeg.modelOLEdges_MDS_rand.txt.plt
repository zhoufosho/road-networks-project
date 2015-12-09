#
# Oldenburg - Degree Distribution. G(4739, 7339). 1331 (0.2809) nodes with in-deg > avg deg (3.1), 470 (0.0992) with >2*avg.deg (Tue Dec  8 22:58:10 2015)
#

set title "Oldenburg - Degree Distribution. G(4739, 7339). 1331 (0.2809) nodes with in-deg > avg deg (3.1), 470 (0.0992) with >2*avg.deg"
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
set output 'inDeg.modelOLEdges_MDS_rand.txt.png'
plot 	"inDeg.modelOLEdges_MDS_rand.txt.tab" using 1:2 title "" with linespoints pt 6
