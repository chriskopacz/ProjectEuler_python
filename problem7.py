#Chris Kopacz
#Project Euler
#Problem 7 - 10001st prime
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, 13
we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

import math

def isPrime(val):
    stop = math.ceil(math.sqrt(val))
    for iter in range(2,stop+1):
        if val % iter == 0:
            return False

    return True



n = 3
counter = 2

while counter <= 10001:
    if isPrime(n) == True:
        print(str(counter) + " " + str(n))
        counter += 1
        n += 2
    else:
        n += 2


































#end of page space holder
