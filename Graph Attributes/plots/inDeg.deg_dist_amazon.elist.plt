#
# Undirected Graph. G(57168, 57378). 12711 (0.2223) nodes with in-deg > avg deg (2.0), 3205 (0.0561) with >2*avg.deg (Sat Sep 26 13:17:28 2020)
#

set title "Undirected Graph. G(57168, 57378). 12711 (0.2223) nodes with in-deg > avg deg (2.0), 3205 (0.0561) with >2*avg.deg"
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
set terminal png font arial 10 size 1000,800
set output 'inDeg.deg_dist_amazon.elist.png'
plot 	"inDeg.deg_dist_amazon.elist.tab" using 1:2 title "" with linespoints pt 6
