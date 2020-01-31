#!/usr/bin/env python
# coding: utf-8


# Version 2D spatiale

# Version adpative 
# Par la suite, nous voudrions/pourrions introduire la taille à maturite 
# comme trait adaptatif, et regarder si une autre espèce arrive avec une taille 
# mat différent, comment elle pourrait prendre le dessus sur une autre, etc. 
# et si un mix d'esp différente peut être envisagé 

from random import random
from fonctions import sig_func
import numpy as np 


lumiere_thresh = .25


class GroundCell(object):

    """Une GroundCell possède les attributs:
    - energie
    - lumiere
    - etat
    - location
    - tree
    et les méthodes:
    - grow_tree
    - repro state
    """

    def __init__(self,coord):
        """Constructeur de GroundCell"""
        self.energie = 100
        self.lumiere = 1
        self.etat = 0 # occupé (1) / innocupé (0)
        self.location = coord
        self.tree = Tree(self.location)


    def grow_tree(self):
        """ Un tree grandit/meurt si les conditions suivantes sont réunies:
        - son age est inf à l'age max (cas échéant il meurt)
        - de l'énergie est disponible pour sa croissance
        - de la lumière est disponible 
        Returns grow_event (0-1), see ForestMap.update_light_conditions
        Also update the hauteur attribut (height) of the three, with a factor which
        depends on his age, and hence to the percentage of the energy allocated to the growth 
        """
        energ_thresh = 10
        age_max = 150 # faire dépendre de l'esp après
        
        grow_event = 0
        if self.energie>energ_thresh and self.lumiere>lumiere_thresh: 
            self.tree.hauteur += (1-self.tree.alloc_repro())*1
            self.energie += -1
            grow_event = 1
            return grow_event
        elif self.tree.age == age_max: # Die event
            self.tree = Tree(self.location) # we reset (see Tree default att) 
            self.energie = 100 # en pratique on voudrait que ce soit un processus continu -> recyclage project, LÉO DEV PART 
            self.lumiere = 1 
            self.etat = 0


    def repro_state(self):
        """
        We consider that a tree reproduces depending on his age
        (see alloc_repro),
        and the available light 
        returns a bool that decides if a tree is able to
        reproduce or not 
        """

        if self.lumiere > lumiere_thresh and self.tree.alloc_repro()>random(): 
            return 1
        else:
            return 0




class Tree(object):

    """Un objet Tree possède 5 attributs et une méthode
    - location
    - hauteur
    - age
    - esp (dict) 
    - repro_condition (0 if non reproductive allowed, 1 otherwise)
    """

    def __init__(self,location):
        """Constructeur d'arbre"""
        self.location = location
        self.hauteur = 0 # arbitrary units for now
        self.age = 0
        self.esp =  dict() 
        self.esp["chene"] = 25
        # ajouter d'autres esp si besoin ...
        # approfondir dict use 
        # self.esp.get("chene") to get the value 
        self.repro_condition = 0 # defined in GroundCell since depends
        # on available light

    def alloc_repro(self): 
        """ Un abre alloue l'énergie disponible 
        à la croissance pendant le début de sa vie
        puis à la reproduction
        returns a float (0-1) that corresponds to the percentage of 
        the energy that is allocated to the reproduction. 
        Hence, at the early stages of life, close to 0, 
        and then around maturity size quickly increasing to 1 
        """
        
        return sig_func(self.age,self.esp.get("chene")) # à changer ici si plusieurs esp



class ForestMap(object):
    """ 
    Carte 2D qui contient les cellules sur lesquelles les 
    arbres pourront grandir, se reproduire, etc. 
    """

    def __init__(self,dimensions=10):
        """Constructeur de ForestMap
        Par default, la grille créé est de dim 10*10
        Une Gc est présente sur chaque cellule: 
        cellmap[i][j].<attributs_de_Gc> (e.g. lumière) 
        """
        self.cellmap = [[] for i in range(dimensions)] 
        for i in range(dimensions):
            for j in range(dimensions): 
                self.cellmap[i].append(GroundCell([i,j])) 

    
    def create_tree(self,location):
        """ Update the etat attribut of GroundCell to 1 
        when a tree is created so when this method is called 
        location [x,y]
        """
        self.cellmap[location[0]][location[1]].etat = 1

    def dispersion(self,location):
        """ Méthode de dispersion
        Quand méthode appelée,
        probabilité que les cellules voisines deviennent occupées
        On considère que cette probabilité de dispersion/repro dépend de l'age de l'arbre. 
        L'hypothèse est qu'un arbre agé sera plus efficace (dispersal_proba) 
        Args:  
        - location [x,y]
        """
        
        dispersal_proba = self.cellmap[location[0]][location[1]].tree.alloc_repro() 
        if (self.cellmap[location[0]][location[1]].repro_state() == 1):
            # à améliorer 
            if location[0] != 0 and location[1] !=0 and location[0]<len(self.cellmap)-1 and location[1]<len(self.cellmap)-1:
                if random() < dispersal_proba: # x - 1, y (left) 
                    self.create_tree([location[0]-1,location[1]])
                if random() < dispersal_proba: # x + 1, y (right) 
                    self.create_tree([location[0]+1,location[1]])
                if random() < dispersal_proba: # x, y - 1(down) 
                    self.create_tree([location[0],location[1]-1])
                if random() < dispersal_proba: # x, y + 1 (up) 
                    self.create_tree([location[0],location[1]+1])




    def update_light_conditions(self,grow_condi,location):
        """
        Update light conditions when a tree grows (grow_condi==1):
        We consider that if a tree grows,
        his neighbors will have access to less light while he still has
        access to as much light as before
        We also consider a minimal quantity of light (a forest is never in the complete dark
        Some tree species would be more tolerant to darkness than others
        Args: 
        - grow_condi -> bool, see GroundCell.grow_tree() 
        - location [x,y] 
        """
        
        lumiere_increment = 0.005*(1-self.cellmap[location[0]][location[1]].tree.alloc_repro()) 
        lumiere_min = 0.05 # some species would be able to grow and reproduce under such conditions  
        
        if grow_condi==1:
            if location[0] != 0 and location[1] !=0 and location[0]<len(self.cellmap)-1 and location[1]<len(self.cellmap)-1: 
                # right  
                self.cellmap[location[0]+1][location[1]].lumiere += -lumiere_increment
                self.cellmap[location[0]+1][location[1]].lumiere = max(self.cellmap[location[0]][location[1]].lumiere,lumiere_min)
                # left 
                self.cellmap[location[0]-1][location[1]].lumiere += -lumiere_increment
                self.cellmap[location[0]-1][location[1]].lumiere = max(self.cellmap[location[0]][location[1]].lumiere,lumiere_min)
                # down 
                self.cellmap[location[0]][location[1]-1].lumiere += -lumiere_increment
                self.cellmap[location[0]][location[1]-1].lumiere = max(self.cellmap[location[0]][location[1]].lumiere,lumiere_min)
                # up 
                self.cellmap[location[0]][location[1]+1].lumiere += -lumiere_increment
                self.cellmap[location[0]][location[1]+1].lumiere = max(self.cellmap[location[0]][location[1]].lumiere,lumiere_min)


               
    def update_Fmap(self):
        """ Update de la forest map"""
        for i in range(len(self.cellmap)):
            for j in range(len(self.cellmap)):
                if(self.cellmap[i][j].etat==1):
                    self.cellmap[i][j].tree.age += 1
                    self.update_light_conditions(self.cellmap[i][j].grow_tree(),[i,j])
                    self.dispersion([i,j])
