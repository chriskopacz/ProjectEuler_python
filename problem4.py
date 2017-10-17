#Chris Kopacz
#Project Euler
#Problem 4 - Largest palindrome product
"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit
numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

numProd = 0
tempPal = 0
numPal = 0

def checkPal(num):
    strNum = str(num)

    for iter in range(0,len(strNum)-1):
        if strNum[iter] != strNum[len(strNum)-iter-1]:
            return -1

    return num

for i in range(100,1000):
    for j in range(100,1000):
        #print(str(i) + " " + str(j))
        numProd = i * j
        tempPal = checkPal(numProd)
        if tempPal > numPal:
            numPal = tempPal


print(numPal)






























#end of page space holder
