set term png
set output 'covid.png'

set multiplot

set title 'Crescimento Exponencial para COVID-19 no Brazil'
set yrange[50:35000]
set xrange[20:36]

set grid

set ylabel "Numero de casos"

set label 1 at 25, 30000

set style fill  transparent pattern 3 border

set xtics("16/03" 20,"18/03" 22,"20/03" 24,"hoje" 26,"24/03" 28,"26/03" 30,"28/03" 32,"30/03" 34, "01/04" 36)

plot 'result_2_old_data.dat' u 1:3:4 "%lf %lf %lf %lf" w filledcu lc rgb "dark-violet" title '99% C.L., usando dados de 15/03', '' u 1:3 lt -1 notitle, '' u 1:4 lt -1 notitle ,'result_2_new_data.dat' u 1:3:4 "%lf %lf %lf %lf" w filledcu  lc rgb "orange"  title '99% C.L., usando dados de 22/03', '' u 1:3 lt -1 notitle, '' u 1:4 lt -1 notitle,'dados_novos.dat' u 1:2 w p title 'dados de 22/03'

set origin 0.14,  0.25
set size .5,.5

clear

unset title
unset ylabel
set yrange[35000:2000000]
set xrange[37:50]

set style fill  transparent pattern 3 border

set logscale y

set ytics("100 mil" 100000,"300 mil" 300000, "1 milhao" 1000000)
set xtics("01/04" 37,"08/04" 44,"14/04" 50)

plot 'result_2_old_data.dat' u 1:3:4 "%lf %lf %lf %lf" w filledcu lc rgb "dark-violet" notitle, '' u 1:3 lt -1 notitle, '' u 1:4 lt -1 notitle ,'result_2_new_data.dat' u 1:3:4 "%lf %lf %lf %lf" w filledcu  lc rgb "orange"  notitle , '' u 1:3 lt -1 notitle, '' u 1:4 lt -1 notitle

unset multiplot
set term x11
