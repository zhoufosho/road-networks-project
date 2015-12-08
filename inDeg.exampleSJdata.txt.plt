#
# San Joaquin - in-degree Distribution. G(18263, 23797). 10978 (0.6011) nodes with in-deg > avg deg (2.6), 12 (0.0007) with >2*avg.deg (Tue Dec  8 13:53:42 2015)
#

set title "San Joaquin - in-degree Distribution. G(18263, 23797). 10978 (0.6011) nodes with in-deg > avg deg (2.6), 12 (0.0007) with >2*avg.deg"
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
set output 'inDeg.exampleSJdata.txt.png'
plot 	"inDeg.exampleSJdata.txt.tab" using 1:2 title "" with linespoints pt 6
