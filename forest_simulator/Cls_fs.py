#!/usr/bin/env python

class GroundCell(object):

    """Une GroundCell possède les attributs:
    -
    -
    -
    -
    et les méthodes:
    - grow_tree
    """

    def __init__(self,coord):
        """TODO: to be defined. """
        self.energie = 100
        self.lumiere = 1
        self.etat = 0 # occupé (1) / innocupé (0)
        self.location = coord
        self.tree = Tree(self.location)


    def grow_tree(self):
        """ Un tree grandit/meure si les conditions suivantes sont réunies:
        - son age est inf à l'age max (cas échéant il meurt)
        - de l'énergie est disponible pour sa croissance
        """
        age_max = 50
        energ_thresh = 10
        if self.tree.hauteur<age_max and self.energie>energ_thresh:
            self.tree.hauteur += 1
            # self.update_light_conditions() # à coder


    def update_light_conditions():
        """
        update light conditions when a tree grows
        adj cells
        dans Forest Map plutôt
        """


    def repro_state(self):
        """
        à remplir
        """
        lumiere_thresh = .5




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
        probabilité (à def) que les cellules voisines deviennent occupées
        """
        age_maturite = 5 ;
        if(self.cellmap[location].tree.age >= age_maturite):
            if location != 0 and location != len(self.cellmap):
                self.cellmap[location-1].etat = 1 # introduire rand ici
                self.cellmap[location+1].etat = 1 # introduire rand ici



    def update_Fmap(self):
        """ Update de la forest map"""
        for i in range(len(self.cellmap)):
            if(self.cellmap[i].etat==1):
                self.cellmap[i].tree.age += 1
                self.cellmap[i].grow_tree()
                # self.cellmap[i].tree.hauteur += 1 # à ajouter
                # conditions sur voisins ici après
                # appeler méthode dispersion ici
                self.dispersion(i)
