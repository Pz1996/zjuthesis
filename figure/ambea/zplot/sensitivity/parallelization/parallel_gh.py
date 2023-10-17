#!/usr/bin/env python
# coding=utf-8
#! /usr/bin/env python


from zplot import *
import math
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent.parent) 
from zplot_config import *


styles = [
    ['lightcoral',        'circle',False],
    ['darkseagreen',      'square',False],
    ['lightblue',         'triangle',False],
    ['black',         'plusline',False],
    ['blue',         'square',True],
    ['blue',         'square',False],
    ['red',         'circle',True],
    ['red',         'circle',False],
]

# xlabelTextSize = 8.5
# ylabelTextSize = 10
# xtitleTextSize = 10
# ytitleTextSize = 10
# legendTextSize = 10
# NormalizedTextSize = 4

ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]
c = canvas(ctype, 'parallel_gh', dimensions=[400, 300])

t = table(file='parallel_gh.data')

# print(min_value)

d = drawable(canvas=c, xrange=[3, 120],
             yrange=[20, 500000], dimensions=[pictureWidthShort*0.8, pictureHeight], coord=[40,30], yscale='log10', xscale='log2')


axis(drawable=d, style='box', ticstyle='in', dominortics=False,
     xminorticcnt=0, doxminortics=False, yminorticcnt=0,doxmajortics=True,
     # xtitle='Dataset', 
     ytitle='Running time (s)',
     xtitle='The number of threads',
     xlabelshift=[0,-10],
     xlabelfontsize=xlabelTextSize,
     ylabelfontsize=ylabelTextSize,
     xtitlesize=xtitleTextSize,
     xaxisposition=50,
     xlabelrotate=0,
     ytitlesize=ytitleTextSize,
     linewidth=0.8, #yauto=['', '', 4],
     ymanual=[['100', 100],['1k',1000],['10k',10000],['100k',100000]],
     xmanual=[['4', 4],['8', 8], ['16', 16],['32', 32],['64', 64],['96',96]]
     )

p = plotter()

L = legend()
L_line = legend()

series_list = ['parambea','parmbe']
series_name = ['ParAMBEA','ParMBE']

# print 32 line


# print 64 line
for idx in range(len(series_list)):

    p.line(drawable=d, table=t, xfield='thread_num', yfield=series_list[idx], linecolor=styles[idx][0],
               linewidth=1.2,legend=L_line)

    p.points(drawable=d, table=t, xfield='thread_num', yfield=series_list[idx], linecolor=styles[idx][0],
                 linewidth=1.2, style=styles[idx][1], fill=styles[idx][2], fillcolor='black', size=2.5,
                legend=L, legendtext=series_name[idx])


L.draw(canvas=c, coord=[d.left()+3, d.top()+10], width=5, height=5, fontsize=legendTextSize, skipnext=1, skipspace=70)
L_line.draw(canvas=c, coord=[d.left(), d.top()+10], width=10, height=15, fontsize=legendTextSize, skipnext=1, skipspace=70)


# ----- drawing circle


c.render()
