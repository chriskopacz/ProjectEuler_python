#Chris Kopacz
#Project Euler
#Problem 16 - Power digit sum
"""
2^15 = 32768 and the sum of its digits is 3+2+7+6+8 = 26

what is the sum of the digits of the number 2^1000?
"""

import math

'''
didnt work -> should have
x = pow(2,1000)
sumOfDigits = 0
leastSB = 0


while x > 0:
    print(str(leastSB) + " " + str(sumOfDigits))
    leastSB = x % 10
    sumOfDigits = sumOfDigits + leastSB

    x = int((x/10))
'''

stringX = str(pow(2,1000))
listIntX = []
temp = 0
sumOfDigits = 0

for iter in range(0,len(stringX)):
    temp = int(stringX[iter])
    listIntX.append(temp)

sumOfDigits = sum(listIntX)

print(str(sumOfDigits))






































#end of page space holder
