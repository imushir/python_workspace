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
import copy
#from gnuradio import gr
import gras

class expo(gras.Block):
    """
    docstring for block expo
    """
    def __init__(self):
        gras.Block.__init__(self,
            name="expo",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])

    def set_parameters(self,g,a,b):
        self.gama = g
        self.alpha = a
        self.beta = b
        
    """def yield_times(self):
        from datetime import date, time, datetime, timedelta
        start = datetime.combine(date.today(), time(0, 0))
        yield start.strftime("%S")
        while True:
            start += timedelta(seconds=0.5)
            yield start.strftime("%S")"""
               
    
    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        #tmrg = []
        o1 = []
        o2 = []
        o3 = []
        ans = []
        final_output = []
        
        """gen = self.yield_times()
        for ii in range(20):
            tmrg.append(gen.next())
        # print "tmrg :",tmrg"""
        
        """for i1 in range(0,10):
            o1.append((self.gama)/(self.alpha*self.beta))
            print "o1 : ", o1
        for i2 in range(0,10):
            o2.append(((self.gama)*(-numpy.exp(self.alpha)))/(self.alpha*(self.beta-self.alpha)))
            print "o2 : ",o2
        for i3 in range(0,10):
            o3.append(((self.gama)*(-numpy.exp(self.beta)))/(self.beta*(self.alpha-self.beta)))
            print "o3 : ",o3
        #ans.append(o1+o2+o3)
        for i in range(0,10):
            ans.append(list(numpy.array(o1[i])+numpy.array(o2[i])+numpy.array(o3[i])))
    
        print "Final Ans : ",ans
        print "Type out : ",type(out)
        print "Type ans :",type(ans)
        
        
        out = copy.copy(ans)
        
        #out[0:1] =  ans
        print "Output is : " ,out
        self.consume(0,1)
        self.produce(0,1)"""
       
        for i in range(0,30):
            o1.append((self.gama)/(self.alpha*self.beta))
            print "o1 : ", o1[i]

            o2.append(((self.gama)*(-numpy.exp((-self.alpha*i)))/(self.alpha*(self.beta-self.alpha))))
            print "o2 : ",o2[i]   
            
            o3.append(((self.gama)*(-numpy.exp((-self.beta*i)))/(self.beta*(self.alpha-self.beta))))
            print "o3 : ",o3[i]
            ans.append(o1[i]+o2[i]+o3[i])
            print "Final Ans : ",ans
            print "Lenght of Ans :",len(ans)
            
        """for i in range(0,len(ans)):
            #out = copy.copy(ans[i])
            #out[0:1] =  ans
            #print "Output is : " ,out"""
        """for i1 in range(0,len(ans)):
            final_output.append(o1+ans[i1])
            print "Final OutPut : ", final_output"""
        #for i1 in range(0,len(ans)):
         #   output_items[0][:1] = ans[i1]
        
        for i1 in range(0,len(ans)):
            out[:] += ans[i1]
            #out[:] = ans[i1]
        
        self.consume(0,1)
        self.produce(0,1)
        
            
        """ans = o1-(mul/o4)
        #ans.append(o1-((numpy.exp(-in0[0:1]*self.sigma)*(numpy.sin((self.freq*in0[0:1])+(self.sigma))))/numpy.sqrt(o1-numpy.square(self.zita))))
        print("Final Value : ",ans)
        out[0:1] = ans"""
        
       
        #out[0:1] = ans
        #out = copy.copy(ans)
         
        
      
             
        

            
       
      
