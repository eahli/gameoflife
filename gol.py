#Conway's game of life
#denna modul tar in en seed-matris och returnerar vem som överlver

import numpy

def wholives(pfield):

    # detta räknar ut storleken på spelfältet
    psize = len(pfield)

    # detta är matrisen där antalet grannar räknas fram, börjar med nollor
    neighbours = numpy.zeros(shape=(psize, psize))

    # räkna grannar i hörnorna
    neighbours[0][0] = pfield[0][1]+pfield[1][0]+pfield[1][1]
    neighbours[0][psize-1] = pfield[0][psize-2] + pfield[1][psize-1] + pfield[1][psize-2]
    neighbours[psize-1][0] = pfield[psize-2][0] + pfield[psize-1][1] + pfield[psize-2][1]
    neighbours[psize-1][psize-1] = pfield[psize-1][psize-2] + pfield[psize-2][psize-1] + pfield[psize-2][psize-2]

    # räkna grannar i första raden
    for x in range(1,psize-1):
        neighbours[0][x] = pfield[0][x-1] + pfield[0][x+1] + pfield[1][x-1] + pfield[1][x] + pfield[1][x+1]

    # räkna grannar i understa raden
    for x in range(1,psize-1):
        neighbours[psize-1][x] = pfield[psize-1][x-1]+pfield[psize-1][x+1]+pfield[psize-2][x-1]+pfield[psize-2][x]+pfield[psize-2][x+1]

    # räkna grannar i första kolumnen
    for x in range(1,psize-1):
        neighbours[x][0]=pfield[x-1][0]+pfield[x+1][0]+pfield[x-1][1]+pfield[x][1]+pfield[x+1][1]

    # räkna grannar i sista kolumnen
    for x in range(1,psize-1):
        neighbours[x][psize-1]=pfield[x+1][psize-1]+pfield[x-1][psize-1]+pfield[x+1][psize-2]+pfield[x][psize-2]+pfield[x-1][psize-2]

    # räkna grannar i centrum
    for x in range(1,psize-1):
        for y in range(1,psize-1):
            neighbours[x][y]=pfield[x-1][y-1]+pfield[x-1][y]+pfield[x-1][y+1]+pfield[x][y-1]+pfield[x][y+1]+pfield[x+1][y-1]+pfield[x+1][y]+pfield[x+1][y+1]

    # Nu bestämmer vi om en cell dör, föds eller lever enligt nedan regler.
    # Any live cell with fewer than two live neighbors dies, as if by loneliness.
    # Any live cell with more than three live neighbors dies, as if by overcrowding.
    # Any live cell with two or three live neighbors lives, unchanged, to the next generation.
    # Any dead cell with exactly three live neighbors comes to life

    for x in range(0,psize):
        for y in range(0,psize):
            if neighbours[x][y] < 2 :
                pfield[x][y]=0
            if neighbours[x][y] > 3 :
                pfield[x][y]=0
            if pfield[x][y] == 0 and neighbours[x][y] == 3:
                pfield[x][y] = 1


    return(pfield)