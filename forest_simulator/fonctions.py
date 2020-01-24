#!/usr/bin/env python

import numpy as np 
import math 
import matplotlib.pyplot as plt 




def sig_func(x,x_thresh): 
    y = x-x_thresh
    return 1/(1+np.exp(-y))


#xmax = 150
#xmin = 0 
#x = np.linspace(xmin,xmax,100)
#xmat = 25  
#y = (x-xmat)*0.25
#
#z = 1/(1+np.exp(-y)) 
#
#plt.plot(x,z)
#plt.show() 


