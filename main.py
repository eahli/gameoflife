# nu är det på riktigt!
# detta är ändringar från jobdator torsdag
import random as random
import numpy as np

#detta definerar storleken på spelfältet, tänk på att det börjar med 0
pfieldx = 3
pfieldy = 3

pfield = np.matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

print(pfield)

print(' \n och nu lägger vi till random 0 och 1  \n')

for x in range(0,pfieldx):
    for y in range(0,pfieldy):
        pfield[x,y]=random.randint(0,1)

print(pfield)

