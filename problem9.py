#Chris Kopacz
#Project Euler
#Problem 9 - Special Pythagorean triplet
"""
A Pythagorean triplet is a set of three natural numbers, a < b < b, such that:
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25

There exists exactly one Pythagorean triplet for which a + b + c = 1000-digit
Find the product a*b*c
"""

a = 0
b = 0
c = 0
check = 0
prod = 0

for iter in range(1,1001):
    a = iter
    for j in range(1,1001-iter):
        b = j
        c = 1000 - (a+b)

        if (a*a + b*b) == (c*c):
            check = 1
            break

    if check == 1:
        break

prod = a*b*c
print("a " + str(a))
print("b " + str(b))
print("c " + str(c))
print("a*b*c " + str(prod))
































#end of page space holder
