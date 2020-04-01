#!/usr/bin/env python3
# coding: utf-8

# Individual-based explicit-space model of a SRI dynamics

import random
from random import randint
from random import randrange
import numpy as np

class Agent(object):
    """"Un agent possède 2 attributs et 5 méthodes
    - location : couple de coordonnées
    - state : 0=susceptible ; 1=infected ; 2=recovered ; 3=death
    - number : the identity of the agent

    - init : create an agent at random location
    - move : move randomly
    - die : proba to die if infected
    - recover : proba to recover if infected
    - be infected : proba to be infected by an agent at the same location"""

    #agent_created = 0 # initially counter is set at 0
    def __init__(self,number,location,space):
        """Constructeur d'agent"""
 
        self.space = space
        #Agent.agent_created += 1 # count the number of agents created
        #for i in range(number):
        self.location = location
        self.state = [0]*number # initially agents are suceptible
        self.number = number

    def move(self,location):
        """Marche aléatoire de l'agent vers une cellule voisine"""
        space = self.space

#        right_left = randint(-1,1)
#        up_down = randint(-1,1)
#        new_location = [location[0]+right_left,location[1]+up_down]

        if location[0]!=space and location[0]!=-space and location[1]!=-space and location[1]!=space:
            right_left = randint(-1,1)
            up_down = randint(-1,1)
            new_location = [location[0]+right_left,location[1]+up_down]

        elif location[0]==-space and location[1]==-space:
            right_left = randint(0,1)
            up_down = randint(0,1)
            new_location = [location[0]+right_left,location[1]+up_down]

        elif location[0]==space and location[1]==space:
            right_left = randint(-1,0)
            up_down = randint(-1,0)
            new_location = [location[0]+right_left,location[1]+up_down]

        elif location[0]==-space and location[1]==space:
            right_left = randint(0,1)
            up_down = randint(-1,0)
            new_location = [location[0]+right_left,location[1]+up_down]

        elif location[0]==space and location[1]==-space:
            right_left = randint(-1,0)
            up_down = randint(0,1)
            new_location = [location[0]+right_left,location[1]+up_down]

        elif location[0]==-space and (location[1]!=space and location[1]!=-space):
            right_left = randint(0,1)
            up_down = randint(-1,1)
            new_location = [location[0]+right_left,location[1]+up_down]

        elif location[0]==space and (location[1]!=space and location[1]!=-space):
            right_left = randint(-1,0)
            up_down = randint(-1,1)
            new_location = [location[0]+right_left,location[1]+up_down]

        elif location[1]==space and (location[0]!=space and location[0]!=-space):
            right_left = randint(-1,1)
            up_down = randint(-1,0)
            new_location = [location[0]+right_left,location[1]+up_down]


        elif location[1]==-space and (location[0]!=space and location[0]!=-space):
            right_left = randint(-1,1)
            up_down = randint(0,1)
            new_location = [location[0]+right_left,location[1]+up_down]

        else:
        #location[1]!=space &  (location[0]!=space & location[0]!=-space):
            right_left = randint(-1,1)
            up_down = randint(-1,1)
            new_location = [location[0]+right_left,location[1]+up_down]

        return new_location

    def die(self,state):
        """Probabilité d'un agent de mourir lorsqu'il est infecté
        Un agent qui meurt passe en state=3, cet état fait que plus fonction
        ne le considère.""" # j'ai trouvé ça plus simple de faire un state pour mort que
        # de supprimer l'agent (notamment pour les outputs)

        proba_to_death = 0.001
        death = 0
        if state==1:
            death = random.random() < proba_to_death

        return death

    def recover(self,state):
        """Probablité d'un agent infecté de guérir, il passe au state=2
        ce qui fait qu'il ne peut plus être infecté de nouveau"""

        proba_to_recover = 0.005
        recover = 0
        if state==1:
            recover = random.random() < proba_to_recover

        return recover

    def infect(self,state,location):
        """Probabilité d'être infecté lorsqu'un agent infecté se trouve
        à la même position"""

        proba_to_infect = 1
        infect = 0
        if state==0: # only susceptible could be infect
            coloc = [i for i,x in enumerate(self.location) if x==location]
            # check if there are other agents at the same location
            if coloc: # = if coloc is not empty
                coloc_state = [self.state[i] for i in coloc] # extract states of coloc
            if 1 in coloc_state: # if there is an infected agent among the coloc
                infect = random.random() < proba_to_infect

        return infect

    def update_Agent(self):
        """Update the situation of each agent"""

        for i in range(self.number):
            if self.state[i] != 3: # if the agent is not dead, it moves
                self.location[i] = self.move(self.location[i])
            if self.die(self.state[i])==1: # infected agent could die
                self.state[i] = 3
            if self.recover(self.state[i])==1: # infected agent could recover
                self.state[i] = 2
            if self.infect(self.state[i],self.location[i])==1: # susceptible agent could
                                                               # be infect
                self.state[i] = 1

