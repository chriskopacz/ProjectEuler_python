#Chris Kopacz
#Project Euler
#Problem 5 - Smallest multiple
"""
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
2*2*3*3*5*7*11*13*17*19*20 = 1163962800
931170240
698377680
465585120
232792560 -> answer
"""

n = 465585120
i = 0

while True:
    if i == 20 or n < 0:
        print(str(n) + " " + str(i))
        break
    else:
        n -= 20
        i = 0
        for iter in range(1,21):
            i = iter
            if (n % iter != 0):
                break



#end of page space holder
