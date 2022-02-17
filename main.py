# nu är det på riktigt!
# detta är ändringar från jobdator torsdag
import random as random
import numpy as numpy

#detta definerar storleken på spelfältet
pfieldx = 3
pfieldy = 3

pfield = numpy.zeros(shape=(pfieldx,pfieldy))

print(pfield)

print(' \n och nu lägger vi till random 0 och 1  \n')

for x in range(0,pfieldx):
    for y in range(0,pfieldy):
        pfield[x,y]=random.randint(0,1)

print(pfield)

