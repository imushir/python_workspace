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

import numpy as np
from gnuradio import gr
import gras
class multiorder_tf(gras.Block):
    """
    docstring for block ztransform
    """
    def __init__(self):
        gras.Block.__init__(self,
            name="ztransform",
            in_sig=[np.float32],
            out_sig=[np.float32])
	

    def set_parameters(self,P,I,D,n0,n1,n2,n3,d0,d1,d2,d3,window):
		#self.num = list(map(float,num.split(" ")))
	    #self.den = list(map(float,den.split(" ")))
        print("self.num")
        print("self.den")
        self.param0 = P
        self.param1 = I
        self.param2 = D
        self.param3 = n0
        self.param4 = n1
        self.param5 = n2
        self.param6 = n3
        self.param7 = d0
        self.param8 = d1
        self.param9 = d2
        self.param10 = d3 
        self.n = window
        self.num = np.poly1d([self.param3])
        self.den = np.poly1d([self.param7,self.param8,self.param9])
        self.den_coeff = self.den.c
        self.nm_coeff = self.num.c
        self.den_ord = self.den.order
        self.num_ord = self.num.order
        for i in range(0,self.den_ord-self.num_ord):
            nm_coeff = np.insert(self.nm_coeff,0,0)
            self.num_coeff = nm_coeff
            #print self.num_coeff
            self.in_q = [0]*(self.den_ord + 1)
            self.out_q = [0]*(self.den_ord + 1)
            self.final_q = []

    def work(self, input_items, output_items):

        in0 = input_items[0]
        out = output_items[0]
        #print "i am in work function"
        # <+signal processing here+>
        ans1 = 0
        ans2 = 0
        for i in range(1,self.den_ord + 1):
            ans1 += self.den_coeff[i]*self.out_q[len(self.out_q)-i]
            self.in_q.append(float(in0[0]))
        #print self.in_q	
        for i in range(0,self.den_ord + 1):
            ans2 += self.num_coeff[i]*self.in_q[len(self.in_q)-i-1]
        #print ans2
        ans = ans2 - ans1
        ans = ans/self.den_coeff[0]
        self.out_q.append(ans)
        self.out_q.pop(0)
        self.in_q.pop(0)

        out[:self.n] = ans
        print "OUTPUT:",out
        #self.final_q.append(ans)
        self.consume(0,1)
        self.produce(0,1)
