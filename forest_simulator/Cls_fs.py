#!/usr/bin/env python

from random import random

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
        """TODO: to be defined. """
        self.energie = 100
        self.lumiere = 1
        self.etat = 0 # occupé (1) / innocupé (0)
        self.location = coord
        self.tree = Tree(self.location)


    def grow_tree(self):
        """ Un tree grandit/meurt si les conditions suivantes sont réunies:
        - son age est inf à l'age max (cas échéant il meurt)
        - de l'énergie est disponible pour sa croissance
        returns grow_event (0-1), see ForestMap.update_light_conditions
        """
        energ_thresh = 10
        age_max = 50
        grow_event = 0

        if self.tree.age<age_max and self.energie>energ_thresh:
            self.tree.hauteur += 1
            self.energie += -1
            grow_event = 1
            return grow_event
        elif self.tree.age == age_max: # die event
            self.tree = Tree(self.location) # we reset >> reset quoi ?
            self.etat = 0


    def repro_state(self):
        """
        We consider that a tree reproduces depending on his age,
        and the available light (discutable)
        returns a bool that decides if a tree is able to
        reproduce or not
        """
        age_maturite = 5
        lumiere_thresh = .25
        if self.lumiere > lumiere_thresh and self.tree.age >= age_maturite:
            return 1
        else:
            return 0




class Tree(object):

    """Un objet tree possède 3 attributs et une méthode
    - location
    - hauteur
    - age
    - repro_condition (0 if non reproductive allowed, 1 otherwise)
    - espece
    - dispersion (méthode)"""

    def __init__(self,location):
        """Constructeur d'arbre"""
        self.location = location
        self.hauteur = 0 # arbitrary units for now
        self.age = 0
        self.esp = 'chene'
        self.repro_condition = 0 # defined in GroundCell since depends
        # on available light

class ForestMap(object):

    """ Pour l'instant on créer une ligne d'abre qui vont grandir
    - cellmap (att): grid des cellules de notre ForestMap
    quand on update (méthode, à définir) l'objet.
    -
    """

    def __init__(self,dimensions):
        """TODO: to be defined. """
        self.cellmap = list()
        for i in range(dimensions):
            self.cellmap.append(GroundCell(i))

    def create_tree(self,location):
        """ créer un arbe"""
        self.cellmap[location].etat = 1

    def dispersion(self,location):
        """ Méthode de dispersion
        Quand méthode appelée,
        probabilité (À FAIRE) que les cellules voisines deviennent occupées
        """

        dispersal_proba = 0.5
        if (self.cellmap[location].repro_state() == 1):
        # if(self.cellmap[location].tree.age >= age_maturite):
            if location != 0 and location != len(self.cellmap):
                # J'ai reformulé comme ça #leo
                # proba_right = random.())
                # proba_left = random.()
                if random() > dispersal_proba:
                    self.cellmap[location-1].etat = 1
                if random() > dispersal_proba:
                    self.cellmap[location+1].etat = 1


    def update_light_conditions(self,grow_condi,location):
        """
        update light conditions when a tree grows (grow_condi==1):
        We consider that if a tree grows,
        his neighbors will have access to less light while he still has
        access to as much light as before
        """
        lumiere_increment = 0.025
        if grow_condi==1:
            if location != 0 and location != len(self.cellmap):
                self.cellmap[location-1].lumiere += -lumiere_increment
                self.cellmap[location+1].lumiere += -lumiere_increment
            # print("light event")


    def update_Fmap(self):
        """ Update de la forest map"""
        for i in range(len(self.cellmap)):
            if(self.cellmap[i].etat==1):
                self.cellmap[i].tree.age += 1
                # self.cellmap[i].tree.hauteur += 1 # à ajouter
                self.update_light_conditions(self.cellmap[i].grow_tree(),i)
                self.dispersion(i)
