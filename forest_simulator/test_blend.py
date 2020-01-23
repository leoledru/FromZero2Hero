#!/usr/bin/env python3.6

import bpy
import csv
# import numpy as np




with open('data.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

x=[]
for i in range(len(data[0])):
    x.append(i)

for i in range(len(x)):
    # Create cube.
    bpy.ops.mesh.primitive_cube_add(radius=0.25, location=(x[i], 0.0, 0.0))
    # cube = bpy.context.active_object

all_cube_data = bpy.data.objects

frame_number = 0
# Temporal Loop
for i in range(len(data)-1):
    for j in range(len(data[0])-1):
        all_cube_data[j].dimensions = (0.25, 0.25, float(data[j][i]))

        bpy.context.scene.frame_set(frame_number)
        all_cube_data[j].keyframe_insert(data_path="scale",index=-1)

    frame_number += 5
