#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Personne():
    """Classe définissant une personne caractérisée par:"""


    personnes_presentes = 0 # attribut de classe
    def __init__(self, nom, prenom):
        """ docstring pour le constructeur """
        self.prenom = prenom
        self.nom = nom
        self.age = 30
        self._lieu_residence = "Paris" # on ne peut pas y accéder en dehors de
        # la classe (ni le modifier)
        Personne.personnes_presentes += 1

    def _get_lieu_residence(self):
        """Méthode qui sera appelée quand on souhaitera accéder en lecture
        à l'attribut lieu_residence"""

        # print("On accède à l'attribut lieu_residence !")
        return self._lieu_residence

    def _set_lieu_residence(self, nouvelle_residence):
        """Méthode appelée quand on souhaite modifier le lieu de résidence"""
        print("Attention, il semble que {} déménage à {}.".format( \
        self.prenom, nouvelle_residence))
        self._lieu_residence = nouvelle_residence


    # On va dire à Python que notre attribut lieu_residence pointe vers une
    # propriété
    lieu_residence = property(_get_lieu_residence, _set_lieu_residence)

class TableauNoir():
    """docstring for TableauNoir, qui définit une surface (attribut)
    laquelle on veut écrire, lire, etc. Par jeu de méthodes"""
    def __init__(self):
        """Par défaut, notre surface est vide"""
        self.surface = ""

    def ecrire(self, message_a_ecrire):
        """Méthode permettant d'écrire sur la surface du tableau.
        Si la surface n'est pas vide, on saute une ligne avant de rajouter le message
        à écrire"""

        if self.surface !="":
            self.surface += "\n"
        self.surface += message_a_ecrire

    def lire(self):
        """ Méthode permettant de lire ce qu'il y a sur la surface"""
        print(self.surface)
