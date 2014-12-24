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

import numpy
import math
#from operator import add
#import copy
#from gnuradio import gr
import gras
from matplotlib.dates import num2date
#from gnuradio import plot_data

class expo(gras.Block):
    """
    docstring for block expo
    """
    def __init__(self):
        gras.Block.__init__(self,
            name="expo",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])

    def set_parameters(self,g,a,b,f):
        self.gama  = g
        self.alpha = a
        self.beta  = b
        self.n = f #window
   

    def isIntegralWin(self, input_item,f):
                if (len(input_item) % f ):
                        raise Exception("Value of Window should be an integral value of length of input items")
               
    
    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        #n_input_items = len(input_items)
        #tmrg = []
        o1 = []
        o2 = []
        o3 = []
        #ans = []
        ans = []
        #final_output = []        
       
     
        
        for i in range(0,20):
            #t = (0.0001)*(i+10)
            o1.append((self.gama)/(self.alpha*self.beta))
            print "o1 : ", o1[i]
            o2.append(((self.gama)*(-numpy.exp((-self.alpha*i)))/(self.alpha*(self.beta-self.alpha))))
            print "o2 : ",o2[i]
            o3.append(((self.gama)*(-numpy.exp((-self.beta*i)))/(self.beta*(self.alpha-self.beta))))
            print "o3 : ",o3[i]
            ans.append(o1[i]+o2[i]+o3[i])
            print "Final Ans : ",ans
            print "Lenght of Ans :",len(ans)
            
        for i in range(0,len(ans)):
            out = ans
            #self.consume(0,len(in0))
            self.produce(0,len(ans))
        
        #for i1 in range(len(ans)):
            #out[:1] += ans[i1]
            #out[:1] = ans[i1]
                
      
        
       
        #out[0:1] = ans
        #out = copy.copy(ans)
         
        
      
             
        

            
       
      
