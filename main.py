# Conway's game of life

import random
import numpy
import gol

psize = 5

seedm = numpy.zeros(shape=(psize, psize))

# ('vi lägger till random 0 och 1 för att använda som seed \n')

for x in range(0, psize):
    for y in range(0, psize):
        seedm[x, y] = random.randint(0, 1)

while next=="y":
    print(gol.wholives(seedm))
    next = input("fortsätta? ")