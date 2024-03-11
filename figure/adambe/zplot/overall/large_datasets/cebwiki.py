#! /usr/bin/env python

from zplot import *
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent.parent) 
from zplot_config import *
import math

# populate zplot table from data file
ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]

######################################large_data#################################

c = canvas(ctype, title='cebwiki', dimensions=[400, 200])
t = table(file='cebwiki.data')
d = drawable(canvas=c, xrange=[-0.6, t.getmax('rownumber')+0.6],
             yrange=[0, 3600*11.5], dimensions=[pictureWidthShort, pictureHeight], coord=[40,30])

c.box(coord=[[205,30],[40+pictureWidthShort,30+pictureHeight]],linecolor="black", linedash="3",linewidth=0.5,fillcolor="",bgcolor="gainsboro",fillstyle='')

c.text(coord=[248,3],text="Parallel algorithms", size=9, color="black", font="Times-Bold")

c.text(coord=[115,3],text="Serial algorithms", size=9, color="black", font="Times-Bold")

axis(drawable=d,style='y',ticstyle='in',
     doxmajortics=False,doymajortics=True,
     ymanual=[['0', 0],['2', 3600*2],['4', 3600*4],['6', 3600*6],['8', 3600*8],['10', 3600*10]],
     ticmajorsize = 3,         
     ylabelfontsize=ylabelTextSize,         
     ytitlesize=ytitleTextSize,)

axis(drawable=d, style='box', ticstyle='in',
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, #yminorticcnt=0,
         #xtitle='(b) Large datasets.', 
         ytitle='Running time (h)', doylabels=True, ytitleshift=[ytitleShiftX,ytitleShiftY],
         linewidth=0.8,
         #yaxisposition=1,
         #xaxisposition=0, yauto=['','',3],
        xlabelrotate=20,
        xaxisposition=0, #yauto=['','',0.5], 
        xlabelshift=[0, -5],
         xlabelfontsize=xlabelTextSize,
         ylabelfontsize=ylabelTextSize,
         xtitlesize=xtitleTextSize,
         ytitlesize=ytitleTextSize,
         ymanual=[['0', 0],['2', 3600*2],['4', 3600*4],['6', 3600*6],['8', 3600*8],['10', 3600*10]],
        xmanual = t.getaxislabels('Serie'),
     )
p = plotter()
L = legend()
L_line = legend()

# grid(drawable=d, x=False, y=True, ystep=0.4,  yrange=[0.2, 1.5],
#     linedash=[1,1], linewidth=0.3, linecolor='black')

bartypes = [('solid', 1, 4),
            ('solid', 1, 4),
            ('solid', 1, 4),
            ('dline2', 1, 4),
            ('hline', 1, 2),
            ('dline1', 1, 4),
            ('dline2', 1, 4),
            ('solid', 1, 4),
            ('solid', 1, 1),]

series_list = ['AdaMBEFinder', 'AdaMBEFinderRand', 'AdaMBEFinderUC']
series_name = ['AdaMBE-INC','AdaMBE-RAND','AdaMBE-UC']
bgcolors    = ['white', 'white', 'white', 'white', 'white','lightgrey', 'lightgrey', 'black']
fillcolors  = fig_colors_light # ['darkgreen', 'lightcyan', 'lightyellow', 'black', 'black','black', 'black', 'black',]


p.verticalbars(drawable=d, table=t, xfield='rownumber', yfield='time',
               barwidth=0.5, 
               linewidth=0.7, 
               labelformat='%s samples/ms',labelrotate=0,labelsize=8,
               fill=True, fillcolor=fig_colors[1], bgcolor='white',
               fillstyle='solid', fillsize=0.4, fillskip=1)

x_start = 23.8
x_step = 40.4
y_start = -6
y_step = 0.002

values=t.getvalues('time')
value0 = float(values[0])

for i in range(len(values)):
  value = float(values[i])
  y_offset = y_start + value * y_step
  text = "OOM"
  if value > 0 and value < 3600:
    text = "%.0fs" % value
  elif value >= 3600:
    text = "%.1fh" % (value/3600)
  c.text(coord=[d.left()+x_start+i*x_step, d.bottom()+y_offset+8],text =text, size=8)

# times=t.getvalues('time')
# for i in range(len(values)):
#   value = float(values[i])
#   y_offset = y_start + value * y_step
#   c.text(coord=[d.left()+x_start+i*x_step, d.bottom()+y_offset+1],text ="(%.1fh)" %(float(times[i])/3600), size=8, color="gray")

c.render()

