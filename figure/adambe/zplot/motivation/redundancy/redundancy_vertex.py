#! /usr/bin/env python

from zplot import *
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent.parent) 
from zplot_config import *
import math

# populate zplot table from data file
ctype = 'pdf' if len(sys.argv) < 2 else sys.argv[1]

c = canvas(ctype, title='redundancy_vertex', dimensions=[400, 200])


######################################real_time#################################

t = table(file='redundancy_vertex.data')
d = drawable(canvas=c, xrange=[-0.6, t.getmax('rownumber')+0.6],
             yrange=[0.85, 1], dimensions=[pictureWidthShort, pictureHeight], coord=[40,30])

# axis(drawable=d,style='y',ticstyle='in',
#      doxmajortics=False,doymajortics=True,
#      ymanual=[['0',0.85],['88%',0.88],['90%',0.9],['92%',0.92],['94%',0.94],['96%',0.96],['98%',0.98],['100%',1]],
#      ticmajorsize = 3,         
#      ylabelfontsize=ylabelTextSize,         
#      ytitlesize=ytitleTextSize,)

axis(drawable=d, style='box', ticstyle='in',
         doxmajortics=False, doymajortics=True,
         xminorticcnt=0, doxminortics=False, #yminorticcnt=0,
         #xtitle='(a) Real workloads.', 
         ytitle='Percentage', doylabels=True, ytitleshift=[ytitleShiftX,ytitleShiftY],
         linewidth=0.8,
         #yaxisposition=1,
         #xaxisposition=0, yauto=['','',3],
#          xlabelrotate=20,
        #xaxisposition=0.2 * 0.3, #yauto=['','',0.5], 
        # xlabelshift=[0, xlableShiftY],
         xlabelfontsize=xlabelTextSize,
         ylabelfontsize=ylabelTextSize,
         xtitlesize=xtitleTextSize,
         ytitlesize=ytitleTextSize,
         ymanual=[['0',0.85],['88%',0.88],['90%',0.9],['92%',0.92],['94%',0.94],['96%',0.96],['98%',0.98],['100%',1]],
        xmanual = t.getaxislabels('Serie'),
        #xmanual=[['Unicode', 0], ['UCforum', 1], ['Writers', 2],
        #        ['YouTube', 3], 
        #         ['Teams', 4], ['ActorMovies', 5],
        #        ['IMDB', 6] , ['Wikipedia', 7], ['DBLP', 8], ['Wikinews', 9],
        #        ['MovieLens', 10], ['Amazon', 11],]
     )
p = plotter()
L = legend()
L_line = legend()

# grid(drawable=d, x=False, y=True, ystep=0.4,  yrange=[0.2, 1.5],
#     linedash=[1,1], linewidth=0.3, linecolor='black')

bartypes = [('solid', 1, 4),
            ('solid', 1, 4),
            ('solid', 1, 4),
            ('solid', 1, 4),
            ('solid', 1, 2),
            ('dline1', 1, 4),
            ('dline2', 1, 4),
            ('solid', 1, 4),
            ('solid', 1, 1),]

#series_list = ['MBEA','iMBEA','PMBE','MineLMBC','FMBE','MMBEA_FAST','MMBEA_MIN','MMBEA']
#series_name = ['MBEA','iMBEA','PMBE','MineLMBC','FMBE','MMBEA_FAST','MMBEA_MIN','MMBEA']
series_list = ['value']
series_name = ['Vertices outside CGs']
bgcolors    = ['whitesmoke', 'white', 'white', 'white', 'white','lightgrey', 'lightgrey', 'black']
fillcolors  = ['black','lightcoral','darkseagreen','honeydew','whitesmoke']
# ['darkgreen', 'lightcyan', 'lightyellow', 'black', 'black','black', 'black', 'black',]


this_color = c.getcolor('%s,%s,%s' % (248.0/256, 196.0/256, 196.0/256))

p.verticalbars(drawable=d, table=t, xfield='rownumber', yfield='Overlap',
            barwidth=0.5, 
            linewidth=0.7, cluster =[0,1], legend=L, legendtext='Vertices inside CGs',
            labelformat='%s samples/ms',labelrotate=0,labelsize=8,
            fill=True, fillcolor=this_color, bgcolor='',
            fillstyle='solid', fillsize=1, fillskip=2)

for i in range(len(series_list)):
    p.verticalbars(drawable=d, table=t, xfield='rownumber', yfield=series_list[i],
               barwidth=0.5, 
               linewidth=0.7, cluster =[i,len(series_list)], legend=L, legendtext=series_name[i],
               labelformat='%s samples/ms',labelrotate=0,labelsize=8,
               fill=True, fillcolor=fig_colors_light[5], bgcolor=bgcolors[i],
               fillstyle=bartypes[i][0], fillsize=0.4, fillskip=bartypes[i][2])




# max line
# p.line(drawable=d, table=t, xfield='rownumber', yfield='CSwap_max', linecolor='black',
#                linewidth=0.6,legend=L_line)
#
# p.points(drawable=d, table=t, xfield='rownumber', yfield='CSwap_max', linecolor='black',
#                  linewidth=0.7, style='circle', fill=False, fillcolor='black', size=0.8,
#                 legend=L, legendtext='CSwap max')


### text for each normalized time
x_start = 5.0
x_step = 28.7

rindex = t.getrindex()
rows  = t.query()

# c.box(coord=[[d.left()+192, d.top()-40], [d.left()+300, d.top()-70]], fill=True, fillcolor="white", linewidth=0.5)
#### legend
# L.draw(canvas=c, coord=[d.left()+200, d.top()-50], skipnext=2,
#     hspace=3, fontsize=legendTextSize,  width=7, height=7)
# L_line.draw(canvas=c, coord=[d.left()+118, d.top()-9], width=10, height=15, fontsize=8, skipnext=1, skipspace=55)
L.draw(canvas=c, coord=[d.left()+1, d.top()+8], skipnext=1, skipspace=180,
    hspace=3, fontsize=legendTextSize,  width=7, height=7 )
##################zoom###################################

c.render()
