#!/usr/bin/env python

# Ref for 3d data to csv to blender   
# https://stackoverflow.com/questions/46852741/python-storing-values-in-a-3d-array-to-csv
# create an example array
#a = np.arange(24).reshape([2,3,4])
## convert it to stacked format using Pandas
#stacked = pd.Panel(a.swapaxes(1,2)).to_frame().stack().reset_index()
#stacked.columns = ['x', 'y', 'z', 'value']
## save to disk
#stacked.to_csv('stacked.csv', index=False)



from ForestSimulator import *
from random import randint
import numpy as np
from numpy import savetxt
import pandas as pd 

# Generate a landscape with of (n*n) (Ground)Cells
n = 20
fmap = ForestMap(n)

# Init : generate an initial tree at a random location
i_init = [randint(0,n-1), randint(0,n-1)]

fmap.create_tree(i_init)

# Run the forest simulator for tmax time steps
tmax = 150
a = np.zeros(shape=(n,n,tmax)) ; 
for i in range(tmax):
    fmap.update_Fmap()
    for j in range(n):
        for k in range(n):
            a[j,k,i] = fmap.cellmap[j][k].tree.hauteur
             

stacked = pd.Panel(a.swapaxes(1,2)).to_frame().stack().reset_index()
stacked.columns = ['x', 'y', 'z', 'height']
# save to disk
stacked.to_csv('data_2D.csv', index=False)

# Then, to load as a list for blender (numpy issue), do 
# (import csv) 
# with open('data.csv',newline='') as csvfile: 
#    data = list(csv.reader(csvfile))  
# # data[0] ... 0:tmax  ...
## >> [t,x,y,height] -> 
# data[t][0] -> t 
# data[t][1] -> x 
# data[t][2] -> y 
# data[t][3] -> z 






# Export  zL to file (csv)
# savetxt('data.csv',zL,delimiter=',')