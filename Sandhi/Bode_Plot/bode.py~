#!/usr/bin/env python
# 
# Copyright 2014 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import wx
import numpy
from gnuradio import gr
#import sciscipy
#from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import sympy
from sympy import * 
from control import matlab


sympy.init_printing()
s = Symbol('s')


class bode(gr.sync_block):
    """
    magnitude and phase of the frequency
    response of a given transfer function
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="bode",
            in_sig=[numpy.float32],
            out_sig=[numpy.float])

    def set_parameters(self,x,y):
        self.a=x
        self.b=y
        from sympy.parsing.sympy_parser import parse_expr
        #parse_expr(self.a)
        #parse_expr(self.b)
        G1= parse_expr(self.a)/parse_expr(self.b)
        #parse_expr(G1)
        
        num = Poly(G1.as_numer_denom()[0],s).all_coeffs()
        den = Poly(G1.as_numer_denom()[1],s).all_coeffs()
        num_coe_lenght = len(num)
        den_coe_lenght = len(den)
        
        
        tf = matlab.tf(map(float,num),map(float,den))
        matlab.bode(tf)
        plt.show()
	    #self.nplot()
        

    def nplot(self):
        #inp = "s=poly(0,'s');h=syslin('c',("+self.a+")/("+self.b+"));clf();bode(h,0.1,100)"
        #sciscipy.eval(inp)

     def work(self, input_items, output_items):
        
        #Leave this unimplemented
	    return len(output_items[0])
