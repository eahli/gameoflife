#Any live cell with fewer than two live neighbors dies, as if by loneliness.
#Any live cell with more than three live neighbors dies, as if by overcrowding.
#Any live cell with two or three live neighbors lives, unchanged, to the next generation.
#Any dead cell with exactly three live neighbors comes to life

import random as random
import numpy as numpy

#detta definerar storleken på spelfältet
pfieldx = 5
pfieldy = 5

pfield = numpy.zeros(shape=(pfieldx,pfieldy))

print('vi lägger till random 0 och 1 för att använda som seed \n')

for x in range(0,pfieldx):
    for y in range(0,pfieldy):
        pfield[x,y]=random.randint(0,99)

print(pfield)

print(' \n och nu skall vi räkna ut antalet grannar i varje cell  \n')

# först en tom matris att skriva in antalet grannar i
neighbours = numpy.zeros(shape=(pfieldx,pfieldy))

#räkna grannar i hörnorna
neighbours[0][0]=pfield[0][1]+pfield[1][0]+pfield[1][1]
neighbours[0][pfieldy-1] = 3

print(pfield[0][0])
print(pfield[0][pfieldy-1])
