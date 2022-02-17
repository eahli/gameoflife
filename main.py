# Conway's game of life

import random
import numpy
import gol
import dplay

psize = input("Hur stort skall spelfältet vara? ")
psize = int(psize)
seedm = numpy.zeros(shape=(psize, psize))

# vi lägger till random 0 och 1 för att använda som seed

for x in range(0, psize):
    for y in range(0, psize):
        seedm[x, y] = random.randint(0, 1)

pfield = gol.wholives(seedm)

next = "y"

while next=="y" or next=="":
    dplay.show(pfield)
    next = input("fortsätta? ")
    pfield = gol.wholives(pfield)