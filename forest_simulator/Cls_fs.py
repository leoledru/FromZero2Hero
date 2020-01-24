#!/usr/bin/env python

# Version adpative 
# Par la suite, nous voudrions/pourrions introduire la taille à maturite 
# comme trait adaptatif, et regarder si une autre espèce arrive avec une taille 
# mat différent, comment elle pourrait prendre le dessus sur une autre, etc. 
# et si un mix d'esp différente peut être envisagé 

from random import random
from fonctions import sig_func


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
        age_max = 150 # faire dépendre de l'esp après
        grow_event = 0

        if self.tree.age<age_max and self.energie>energ_thresh:
            self.tree.hauteur += (1-self.tree.alloc_repro())*1
            self.energie += -1
            grow_event = 1
            return grow_event
        elif self.tree.age == age_max: # die event
            self.tree = Tree(self.location) # we reset (see Tree default att) 
            self.energie = 100 # en pratique on voudrait que ce soit un processus continu  
            self.lumiere = 1 
            self.etat = 0


    def repro_state(self):
        """
        We consider that a tree reproduces depending on his age
        (see alloc_repro),
        and the available light (discutable)
        returns a bool that decides if a tree is able to
        reproduce or not 
        """
        lumiere_thresh = .25 
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
    - dispersion (méthode)
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
        puis à la reproduction """
        
        return sig_func(self.age,self.esp.get("chene")) # à changer ici si plusieurs esp



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
            if location != 0 and location < len(self.cellmap)-1:
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
        lumiere_increment = 0.005*(1-self.cellmap[location].tree.alloc_repro()) 
        
        if grow_condi==1:
            if location != 0 and location < len(self.cellmap)-1:    
                self.cellmap[location-1].lumiere += -lumiere_increment
                self.cellmap[location+1].lumiere += -lumiere_increment



    def update_Fmap(self):
        """ Update de la forest map"""
        for i in range(len(self.cellmap)):
            if(self.cellmap[i].etat==1):
                self.cellmap[i].tree.age += 1
                # self.cellmap[i].tree.hauteur += 1 # à ajouter
                self.update_light_conditions(self.cellmap[i].grow_tree(),i)
                self.dispersion(i)
