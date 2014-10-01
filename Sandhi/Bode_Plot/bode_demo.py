import sympy
from sympy import * 
from control import matlab
from Tkinter import *
import numpy
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np


sympy.init_printing()
s = Symbol('s')
#denominator_value=0
#numerator_value=0

num=[]
den=[]
G1 = s/(1-s)
print(G1)
num_tf=6
deno_tf=s**2+5*s+6
G2 = (num_tf)/(deno_tf)


#G = G1*G2
#print(G)
#ans = G.simplify()
#print(ans)
#H = 50
#Tf = (G1*G2)/(1+(H*G1*G2))
print(G1)


def freqResponse(Ts):
    global num
    global den
    num = Poly(Ts.as_numer_denom()[0],s).all_coeffs()
    den = Poly(Ts.as_numer_denom()[1],s).all_coeffs()
    print(num)
    print(den)
    #creates_sliders(len(num),len(den))
def update_num(val):
    global num
    num=num+val
    print(num)
    tf = matlab.tf(map(float,num),map(float,den))
    matlab.bode(tf)
    plt.show()
def update_den(val):
    global den
    den=den+val
    print(den)
    tf = matlab.tf(map(float,num),map(float,den))
    matlab.bode(tf)
    plt.show()
    
def creates_sliders(v1,v2):
        for nume_slider in range(0,v1):
            master = Tk()
            w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
            w.pack()
        mainloop()
fig = plt.figure()
ax = fig.add_subplot(111)
ax.autoscale(True)
#plt.subplots_adjust(left=0.25, bottom=0.25)
#num_coe_sli = plt.axes([0.25, 0.1, 0.65, 0.03])
#deno_coe_sli = plt.axes([0.25,0.05,0.65,0.03])
#nume_slider = Slider(num_coe_sli, 'Numerator', 0, 99, valinit=0,valfmt='%d')
#deno_slider = Slider(deno_coe_sli, 'Denominator', 0, 99, valinit=0,valfmt='%d')
freqResponse(G2)
print(num)
print(den)
tf = matlab.tf(map(float,num),map(float,den))
matlab.bode(tf)
axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.20, 0.1, 0.65, 0.03], axisbg=axcolor)
axamp  = plt.axes([0.20, 0.15, 0.65, 0.03], axisbg=axcolor)
sfreq = Slider(axfreq, 'Numerator', 0.1, 30.0, valinit=0)
samp = Slider(axamp, 'Denominator', 0.1, 10.0, valinit=0)
plt.subplots_adjust(left=0.20, bottom=0.30)
plt.show()
sfreq.on_changed(update_num)
samp.on_changed(update_den)