#
# Oldenburg - Degree Distribution. G(3952, 7173). 1507 (0.3813) nodes with in-deg > avg deg (3.6), 444 (0.1123) with >2*avg.deg (Tue Dec  8 22:58:10 2015)
#

set title "Oldenburg - Degree Distribution. G(3952, 7173). 1507 (0.3813) nodes with in-deg > avg deg (3.6), 444 (0.1123) with >2*avg.deg"
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
set output 'inDeg.modelOLEdges_ISO.txt.png'
plot 	"inDeg.modelOLEdges_ISO.txt.tab" using 1:2 title "" with linespoints pt 6
