#Chris Kopacz
#Project Euler
#Problem 18 - Maximum path sum I
"""
By starting at the top of the triangle below and moving to adjacent numbers
on the row below, the maximum total from top to bottom is 23.
   3
  7 4
 2 4 6
8 5 9 3
3 + 7 + 4 + 9 = 3

Find the maximum total from top to bottom of the triangle below:

                            75
                          95 64
                        17 47 82
                      18 35 87 10
                    20 04 82 47 65
                  19 01 23 75 03 34
                88 02 77 73 07 63 67
              99 65 04 28 06 16 70 92
            41 41 26 56 83 40 80 70 33
          41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
      70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by
trying every route. However, Problem 67 is the same hallenge with a triangle
containing one-hundred rows; it cannot be solved by brute force, and
requires a clever method.
"""

def goRight(iteration):
    return iteration+1

def goLeft(iteration):
    return iteration

w,h = 15,15
grid = [[0 for x in range(w)] for y in range(h)]
grid[0] = [75,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
grid[1] = [95,64,0,0,0,0,0,0,0,0,0,0,0,0,0]
grid[2] = [17,47,82,0,0,0,0,0,0,0,0,0,0,0,0]
grid[3] = [18,35,87,10,0,0,0,0,0,0,0,0,0,0,0]
grid[4] = [20,4,82,47,65,0,0,0,0,0,0,0,0,0,0]
grid[5] = [19,1,23,75,3,34,0,0,0,0,0,0,0,0,0]
grid[6] = [88,2,77,73,7,63,67,0,0,0,0,0,0,0,0]
grid[7] = [99,65,4,28,6,16,70,92,0,0,0,0,0,0,0]
grid[8] = [41,41,26,56,83,40,80,70,33,0,0,0,0,0,0]
grid[9] = [41,48,72,33,47,32,37,16,94,29,0,0,0,0,0]
grid[10] = [53,71,44,65,25,43,91,52,97,51,14,0,0,0,0]
grid[11] = [70,11,33,28,77,73,17,78,39,68,17,57,0,0,0]
grid[12] = [91,71,52,38,17,14,91,43,58,50,27,29,48,0,0]
grid[13] = [63,66,4,68,89,53,67,30,73,16,69,87,40,31,0]
grid[14] = [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]

"""
didn't work, nice try

level = 0
node = 0
total = grid[0][0] #starting value is set to the root node
nextNode = 0

while level < 14:
    if grid[level+1][node] > grid[level+1][node+1]:
        nextNode = goLeft(node)
        total = total + grid[level+1][node]
        node = nextNode
    elif grid[level+1][node] < grid[level+1][node+1]:
        nextNode = goRight(node)
        total = total + grid[level+1][node+1]
        node = nextNode
    else:
        #if the two adjacent nodes are equal, go right by default
        nextNode = goRight(node)
        total = total + grid[level+1][node]
        node = nextNode
    level += 1

print(str(total))
"""

#need to work from bottom up remaking a tree of partial sums

level = 13
node = 0
nextNode = 0
grid2 = grid

for iter in range(0,level+1):
    if grid[level+1][iter] > grid[level+1][iter+1]:
        grid2[]




































#end of page space holder
