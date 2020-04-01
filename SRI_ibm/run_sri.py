#!/usr/bin/env python3
# coding: utf-8

from sri import *
from random import randint
import numpy as np
import pandas as pd

tmax = 100
space = 10 # size of the space (sachant que l'espace est ouvert pour le moment)

# Generate n agent at random locations
n = 150

location = [] # empty list
for i in range(n):
    location.append([randint(-space,space),randint(-space,space)]) # random location 
#    location.append([0,0]) # everyone at the center

# print pour test
#print(location)

# creation des agents
agents = Agent(n,location,space)

nb_infect = 2
for i in range(nb_infect):
    infect = randint(0,n-1) # choose a random initially infected agent
    agents.state[infect] = 1

# update des agents until tmax
agent_location = np.zeros(shape=(tmax,n*3)) # for each agent store : x,y,state

for i in range(tmax):
    agents.update_Agent()
    for j in range(n):
        agent_location[i,j*3] = agents.location[j][0]
        agent_location[i,j*3+1] = agents.location[j][1]
        agent_location[i,j*3+2] = agents.state[j]

# print pour test
#print(agent_location)
#print(agents.number)

np.savetxt('location_2D.csv',agent_location, delimiter=",")
