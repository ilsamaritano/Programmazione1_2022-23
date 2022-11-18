from biblio import *
from testMy import *


def concatenaprova(cat1, cat2):
    nuovo = [] #togliere?
    for elemento in cat1:
        if len(elemento)==4:
            if elemento in cat2:  # NON VA BENE PERCHE' FA L'INTERSEZIONE PD
                nuovo = cat1+elemento

            if len(elemento) == 5:
                nuovo.append(elemento)
                #nuovo = cat1 + elemento?
            else:
                index = cat2.index(elemento)
                # nuovo.append(elemento)
                # for tupla in elemento:
                nota = cat2[index][5]
                notacombinata = elemento[5]+', ' + nota
                elemento = list(elemento)
                elemento[5] = notacombinata
                elemento = tuple(elemento)
                print(elemento)
    nuovo.sort()
    return nuovo






