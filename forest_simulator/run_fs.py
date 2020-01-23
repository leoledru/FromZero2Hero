#!/usr/bin/env python


# t'es là ?
# Re, sorry j'suis en pleine invasion de pyrale

# est-ce qu'il a un regain d'énergie pour la GroundCell qqpart ?
# non pas pour le moment
# yes ^^
# oh mollo hein  haha non non mais c pour être sur de comprendre
# ahah yes, tu peux t'en charger par contre ^^
# ni de perte d'ailleurs ?
# j'ai fais un repo sur mon git
# tu veux que j'update ? tu clones le truc
# C un autre repo que celui du tuto openclass ?
# oui mais si t'as cloné FromZero2Hero tu auras, c'est dedans
# ok je fais ça, deux sec  
# ok bah oui j'ai juste a pull alors !




from Cls_fs import *
from random import randint

# Generate a landscape with n GroundCells
n = 100
fmap = ForestMap(n) # 1D for now

# Init : generate a tree at a random location
i_init = randint(0,n-1)
print(i_init)
fmap.create_tree(i_init)

for i in range(15):
    fmap.update_Fmap()
    # Verif
    # print('ini {0}, third {1}'.format(fmap.cellmap[i_init].tree.hauteur,
    # fmap.cellmap[i_init-2].tree.hauteur))




# for ...
# fmap.update_Fmap()
# stocker x,y,z des arbres sur la grid
