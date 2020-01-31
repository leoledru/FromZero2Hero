#!/usr/bin/env python3.6

import bpy
import csv


# Load the data 
with open('data_2D.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))


# Get the dimension of the Map through data set 
i=0 
dim = 1 
while i == 0: 
    dim += 1 
    i = float(data[dim][1]) # column x (spatial) 

dim = dim - 1 # 


# Store the line of trees (x dim, cst) and create init cubes 
x=[]
y=[]
coord=[] 
compteur=0 
for i in range(dim):
    x.append(i)
    for j in range(dim):        
        y.append(j)
        coord.append([i,j,compteur])
        currobj = bpy.data.objects 
        # bpy.ops.mesh.primitive_cube_add(location=(x[i],y[j],0.0))
        # add tree by sapling tree generation addon
        bpy.ops.curve.tree_add('INVOKE_DEFAULT',showLeaves=True,location=(x[i],y[j],0.0))
        # set the initial location
        # currobj[i][j].location = (x[i]*5,y[j]*5,0)
        compteur += 1 


# All cubes objects 
cubes = bpy.data.objects 
#
#
#
#
# Cache shortcuts to start and end of scene.
scene = bpy.context.scene
frame_start = scene.frame_start
frame_end = scene.frame_end
#
# Loop through locations list.
loc_len = int((len(data)-1)/(dim*dim))  
i_to_percent = 1.0 / (loc_len - 1)
i_range = range(0, loc_len, 1)
for i in i_range:
    # Convert place in locations list to appropriate frame.
    i_percent = i * i_to_percent
    key_frame = int(frame_start * (1.0 - i_percent) + frame_end * i_percent)
    scene.frame_set(key_frame)
    # Update location for that frame.
    # cubes[15].scale = locations[i]
    for j in range(dim*dim):
        growth = float(data[(dim*dim*i)+j+1][3])/10 #
        # growth in x and y proportional to growth in height
        cubes[j].scale = [1/2*growth,1/2*growth,growth]
        cubes[j].keyframe_insert(data_path='scale')





