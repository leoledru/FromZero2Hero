#!/usr/bin/env python3
# coding: utf-8

from sri import *
from random import randint
import numpy as np
import pandas as pd

tmax = 10

# Generate n agent at random locations
n = 2

#location = [[randint(0,5),randint(0,5)]]
location = [[randint(0,5),randint(0,5)],[randint(0,5),randint(0,5)]]

# print pour test
print(location)

# creation des agents
agents = Agent(n,location)

# update des agents until tmax
agent_location = np.zeros(shape=(tmax,n*2))
for i in range(tmax):
    agents.update_Agent()
    for j in range(n):
        agent_location[i,j*2] = agents.location[j][0]
        agent_location[i,j*2+1] = agents.location[j][1]

# print pour test
print(agent_location)
print(agents.number)

np.savetxt('location_2D',agent_location, delimiter=',')
