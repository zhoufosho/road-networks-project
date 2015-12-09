#
# Oldenburg - Degree Distribution. G(5093, 7091). 2388 (0.4689) nodes with in-deg > avg deg (2.8), 444 (0.0872) with >2*avg.deg (Tue Dec  8 22:58:11 2015)
#

set title "Oldenburg - Degree Distribution. G(5093, 7091). 2388 (0.4689) nodes with in-deg > avg deg (2.8), 444 (0.0872) with >2*avg.deg"
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
set output 'inDeg.modelOLEdges_MDS_hopScaled.txt.png'
plot 	"inDeg.modelOLEdges_MDS_hopScaled.txt.tab" using 1:2 title "" with linespoints pt 6
