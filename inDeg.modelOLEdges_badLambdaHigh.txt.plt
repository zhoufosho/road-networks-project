#
# Oldenburg - Degree Distribution. G(2652, 3711). 1025 (0.3865) nodes with in-deg > avg deg (2.8), 318 (0.1199) with >2*avg.deg (Tue Dec  8 22:39:43 2015)
#

set title "Oldenburg - Degree Distribution. G(2652, 3711). 1025 (0.3865) nodes with in-deg > avg deg (2.8), 318 (0.1199) with >2*avg.deg"
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
set output 'inDeg.modelOLEdges_badLambdaHigh.txt.png'
plot 	"inDeg.modelOLEdges_badLambdaHigh.txt.tab" using 1:2 title "" with linespoints pt 6
