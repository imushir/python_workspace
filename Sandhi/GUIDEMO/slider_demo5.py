from pylab import *
from matplotlib.widgets import Slider
import numpy as np
hte = np.array([10,11,12,13,15,20,21,22,25,30])
hre = np.array([1,2,3,4,5,6,7,8,9,10])
k = 20 * hte
n4 = 10 * hre
t,w4 = 6,25
x = arange(1,100,10)
d = log10(x) / 10

y = k + n4 * d + t + w4 + 8

ax = subplot(111)
subplots_adjust(left=0.15,bottom=0.25)
line, = plot(x,y,linewidth=2,color='r')

xlabel('X-Title')
ylabel('Y-title')
title('$Our Chart$')
grid(True)

axcolor = 'lightgoldenrodyellow'
axhte = axes([0.15,0.1,0.65,0.03], axisbg=axcolor)
axhre = axes([0.15,0.15,0.65,0.03],axisbg=axcolor)

shte = Slider(axhte,'hte',0.1,30.0,valinit=1)
shre = Slider(axhre,'hre',0.1,10.0,valinit=1)

def update(val):
    k = 20* hte * shte.val
    n4 = 10*hre * shre.val
    
    y = k + n4 * d + t + w4 +8
    line.set_ydata(y)
    ax.set_ylim(y.min(),y.max())
    draw()
shte.on_changed(update)
shre.on_changed(update)    
    
    




