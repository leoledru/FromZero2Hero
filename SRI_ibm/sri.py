#!/usr/bin/env python3
# coding: utf-8

# Individual-based explicit-space model of a SRI dynamics

from random import random
from random import randrange
from random import randint
import numpy as np

class Agent(object):
    """"Un agent possède 2 attributs et 5 méthodes
    - location : couple de coordonnées
    - state : 0=safe ; 1=infected ; 2=recovered
    - number : the identity of the agent

    - init : create an agent at random location
    - move : move randomly
    - die : proba to die if infected
    - recover : proba to recover if infected
    - be infected : proba to be infected by an agent at the same location"""

    #agent_created = 0 # initially counter is set at 0
    def __init__(self,number,location):
        """Constructeur d'agent"""

        #Agent.agent_created += 1 # count the number of agents created
        #for i in range(number):
        self.location = location
        self.state = [0]*number # initially agents are safe
        self.number = number

    def move(self,location):
        """Marche aléatoire de l'agent vers une cellule voisine"""

        right_left = randint(-1,1)
        up_down = randint(-1,1)
        new_location = [location[0]+right_left,location[1]+up_down] # random move (the agent can
                                                                # stay at the same location)
        return new_location

    def update_Agent(self):
        """Update the situation of each agent"""

        for i in range(self.number):
            self.location[i] = self.move(self.location[i])
