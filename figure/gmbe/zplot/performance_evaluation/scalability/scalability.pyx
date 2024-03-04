#! /usr/bin/env python


from zplot import *
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent.parent) 
from zplot_config import *


styles = [
    ['blue',         'circle',False],
    ['black',         'square',False],
    ['black',         'xline',False],
    ['black',         'plusline',False],
    ['blue',         'square',True],
    ['blue',         'square',False],
    ['red',         'circle',True],
    ['red',         'circle',False],
]

NormalizedTextSize = 4

xtitle_line_height = 30 
ytitle_line_width = 50 
dataset_text_height = 15 
L_height = 20
L_width = 80

ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]
c = canvas(ctype, 'scalability', dimensions=[400, 150])

t_1 = table(file='scalability.data')
# print(min_value)

d_1 = drawable(canvas=c, xrange=[-0.6, t_1.getmax('rownumber')+0.6],
             yrange=[1, 10000], coord=[40, 30], dimensions=[pictureWidthShort, pictureHeight], yscale='log10')


axis(drawable=d_1, style='box', ticstyle='out', dominortics=False,
     xminorticcnt=0, doxminortics=False, doyminortics=False, yminorticcnt=0,
     #xtitle='Threads number',
     ytitle='Running time (s)',
     ytitleshift=[ytitleShiftX,ytitleShiftY],
     xlabelshift=[0,2],
     xlabelfontsize=xlabelTextSize,
     ylabelfontsize=ylabelTextSize,
     xtitlesize=xtitleTextSize,
     ytitlesize=ytitleTextSize,
     linewidth=0.8, #xauto=[0, 300, 0], 
     ymanual=[['1', 1], ['10', 10], ['100', 100], ['1000', 1000]],
     xmanual = t_1.getaxislabels(column='Serie'),
     )

p = plotter()

L = legend()
L_line = legend()

series_list = ['gmbe', 'parmbe', 'oombe']
series_name = ['GMBE','PARMBE','OOMBEA']


for idx in range(len(series_list)):
    p.line(drawable=d_1, table=t_1, xfield='rownumber', yfield=series_list[idx], linecolor=styles[idx][0],
               linewidth=0.7,legend=L_line)

    p.points(drawable=d_1, table=t_1, xfield='rownumber', yfield=series_list[idx], linecolor=styles[idx][0],
                 linewidth=0.7, style=styles[idx][1], fill=False, fillcolor='black', size=2.5,
                legend=L, legendtext=series_name[idx])


L.draw(canvas=c, coord=[d_1.left()-10, d_1.top()+12], skipnext=1, skipspace=65,
    hspace=3, fontsize=legendTextSize,  width=7, height=7 )


c.render()
