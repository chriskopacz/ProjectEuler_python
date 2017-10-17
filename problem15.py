#Chris Kopacz
#Project Euler
#Problem 15 - Lattice Paths
"""
Starting in the top left corner of a 2x2 grid, and only being able to move
to the right and down, there are exactly 6 routes to the bottom right corner.

(see image)

Ho many such routes are there through a 20x20 grid?
"""

'''
#recursion -> took too long
def checkPath(n):

    maxRight = 20
    maxDown = 20
    #last case
    if n == [maxRight,maxDown]:
        return 1

    path = 0

    #go right
    if n[0] < maxRight:
        path += checkPath([n[0]+1,n[1]])

    #go down
    if n[1] < maxDown:
        path += checkPath([n[0],n[1]+1])

    return path


#starting postion is top left corner
aGrid = [0,0]
numPaths = 0

numPaths = checkPath(aGrid)

print(str(numPaths))
'''


w,h = 20,20
grid = [[0 for x in range(w)] for y in range(h)]

for iter in range(0,w):
    grid[0][iter] = iter+2
    grid[iter][0] = iter+2


for iter in range(1,h):
    for jter in range(1,w):
        grid[iter][jter] = grid[iter][jter-1] + grid[iter-1][jter]


print(grid[19][19])























#end of page space holder
