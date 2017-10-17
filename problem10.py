#Chris Kopacz
#Project Euler
#Problem 10 - Summation of primes
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million (2000000).
"""
import math

def isPrime(val):
    stop = math.ceil(math.sqrt(val))
    for iter in range(2,stop+1):
        if val % iter == 0:
            return False

    return True


primeList = []
primeList.append(2)
n = 3
primeSum = 0

while n <= 2000000:
    if isPrime(n) == True:
        #print(str(n))
        primeList.append(n)
        n += 2
    else:
        n += 2


primeSum = sum(primeList)
print(str(primeSum))

































#end of page holder
