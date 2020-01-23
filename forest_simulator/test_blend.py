#!/usr/bin/env python3.6

import bpy 
import csv
import numpy as np 




with open('data.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

D = np.array(data) # str 
D = D.astype(float)  












# Create cube.
#bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0.0, 0.0, 0.0))
#cube = bpy.context.active_object
#
## Cache shortcuts to start and end of scene.
#scene = bpy.context.scene
#frame_start = scene.frame_start
#frame_end = scene.frame_end
#
## Loop through locations list.
#loc_len = len(list_of_x)
#i_to_percent = 1.0 / (loc_len - 1)
#i_range = range(0, loc_len, 1)
#for i in i_range:
#
## Convert place in locations list to appropriate frame.
#i_percent = i * i_to_percent
#key_frame = int(frame_start * (1.0 - i_percent) + frame_end * i_percent)
#scene.frame_set(key_frame)
#
## Update location for that frame.
#cube.location = (list_of_x[i],list_of_y[i],list_of_z[i])
#cube.keyframe_insert(data_path='location')
