#! /usr/bin/env python

from zplot import *
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent.parent) 
from zplot_config import *
import math

# populate zplot table from data file
ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]

c = canvas(ctype, title='distribution_bx', dimensions=[400, 200])


######################################real_time#################################

x_offset = 40
y_offset = 30
dx = 140
dy = 75

t = table(file='distribution_bx.data')
d = drawable(canvas=c, xrange=[0, 5],
             yrange=[0, 5], dimensions=[dx, dy], coord=[x_offset, y_offset])

axis(drawable=d, style='box', doxmajortics = False, doymajortics = False,
    xmanual=[['8',1],['16',2],['24',3],['32',4],['X',5]],
    xtitle='|L|',
    ytitle='|C|',
    xlabelfontsize=xlabelTextSize,
    ylabelfontsize=ylabelTextSize,
    xtitlesize=xtitleTextSize,
    ytitlesize=ytitleTextSize,
    ymanual=[['8',1],['16',2],['24',3],['32',4],['X',5]],
    xlabelshift=[0, 3],
    ylabelshift=[3, 0],
    xtitleshift=[0, 1],
    ytitleshift=[-3, 0],
    #  yauto=['','',1], xauto=['','',1]
    )
p = plotter()

table_data = t.query('')
x_items = len(table_data[0]) - 1
y_items = len(table_data)
x_step = dx / x_items
y_step = dy / y_items

front_color = (255.0/256,255.0/256,224.0/256)
back_color = (224.0/256,0.0/256,0.0/256)


for i in range(y_items):
  for j in range(x_items):
    color_0 = (back_color[0] - front_color[0]) *  math.sqrt (float(table_data[i][j+1])*1.5) + front_color[0]
    color_1 = (back_color[1] - front_color[1]) *  math.sqrt (float(table_data[i][j+1])*1.5) + front_color[1]
    color_2 = (back_color[2] - front_color[2]) *  math.sqrt (float(table_data[i][j+1])*1.5) + front_color[2]
    
    color = c.getcolor('%s,%s,%s' % (color_0, color_1, color_2))
    c.box(coord=[[x_offset+i*x_step, y_offset+j*y_step],
                 [x_offset+(i+1)*x_step, y_offset+(j+1)*y_step]], linewidth=0.1, fill=True, fillcolor=color, fillstyle='solid')
    c.text(coord=[x_offset+(i+0.5) *x_step, y_offset+(j+0.3)*y_step], text=table_data[i][j+1],size=8)

    c.text(coord=[x_offset-5, y_offset-9], text='0',size=8)

c.render()
