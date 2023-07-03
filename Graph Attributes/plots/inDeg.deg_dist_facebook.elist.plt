#
# Undirected Graph. G(3213, 57832). 1056 (0.3287) nodes with in-deg > avg deg (36.0), 489 (0.1522) with >2*avg.deg (Sat Sep 26 13:16:51 2020)
#

set title "Undirected Graph. G(3213, 57832). 1056 (0.3287) nodes with in-deg > avg deg (36.0), 489 (0.1522) with >2*avg.deg"
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
set output 'inDeg.deg_dist_facebook.elist.png'
plot 	"inDeg.deg_dist_facebook.elist.tab" using 1:2 title "" with linespoints pt 6
