#!/usr/bin/env python3.6

import bpy
import csv


# Load the data 
with open('data.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

# Store the line of trees (x dim, cst) and create init cubes 
x=[]
for i in range(len(data[0])):
    x.append(i)
     # set the list of current objects for each new object
    currobj = bpy.data.objects 
    #bpy.ops.mesh.primitive_cube_add(radius=0.25, location=(x[i],0.0,0.0))
    # add tree by sapling tree generation addon
    bpy.ops.curve.tree_add('INVOKE_DEFAULT',showLeaves=True)
    # set the initial location
    currobj[i].location = (x[i]*5,0,0)

# All cubes objects 
cubes = bpy.data.objects 




# Cache shortcuts to start and end of scene.
scene = bpy.context.scene
frame_start = scene.frame_start
frame_end = scene.frame_end

# Loop through locations list.
loc_len = len(data)
i_to_percent = 1.0 / (loc_len - 1)
i_range = range(0, loc_len, 1)
for i in i_range:

    # Convert place in locations list to appropriate frame.
    i_percent = i * i_to_percent
    key_frame = int(frame_start * (1.0 - i_percent) + frame_end * i_percent)
    scene.frame_set(key_frame)

    # Update location for that frame.
    # cubes[15].scale = locations[i]
    for j in range(len(x)-1):
        growth = float(data[i][j])/10 
        # growth in x and y proportional to growth in height
        cubes[j].scale = [1/2*growth,1/2*growth,growth]
        cubes[j].keyframe_insert(data_path='scale')





