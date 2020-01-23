#!/usr/bin/env python

# A régler dans Cls
# Conditions au bord à prendre en compte
# lumière et énergie values negatives -> do we care ?

# Leo t'es là ?
# cette aprem je laiserai ce programme en stand by je passerai sur
# blender à regarder tes codes et mettre en input mes coord
# pour faire grandir des arbres :)

# tu peux push un coup le code que je le prenne à jour pour checker comment ça tourne



from Cls_fs import *
from random import randint
import numpy as np
from numpy import savetxt

# Generate a landscape with n GroundCells
n = 100
fmap = ForestMap(n) # 1D for now

# Init : generate an initial tree at a random location
i_init = randint(0,n-1)
# print(i_init)
fmap.create_tree(i_init)


# Run the forest simulator for tmax time steps
tmax = 50
zL=np.zeros(shape=(tmax,n)) ; # (time in rows, grid cells in col)
for i in range(tmax):
    fmap.update_Fmap()
    # Verifs
    print('ini {0}, third {1}'.format(fmap.cellmap[i_init].tree.hauteur,
    fmap.cellmap[i_init-2].tree.hauteur))
    print('lumiere adj ini {0}'.format(fmap.cellmap[i_init-1].lumiere))
    for j in range(n):
        zL[i,j] = fmap.cellmap[j].tree.hauteur
    # stocker x,y,z des arbres sur la grid

# Export  zL to file (csv)
savetxt('data.csv',zL,delimiter=',')
