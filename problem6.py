#Chris Kopacz
#Project Euler
#Problem - Sum square difference
"""
The sum of the squares of the first ten natural numbers is:
1^2 + 2^2 +...+10^2 = 385
The square of the sum of the first ten natural numbers is:
(1+2+...+10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

sum_of_squares = 0
square_of_sum = 0
diff = 0

for iter in range(1,101):
    sum_of_squares = sum_of_squares + (iter*iter)

for iter in range(1,101):
    square_of_sum = square_of_sum + iter

square_of_sum = (square_of_sum*square_of_sum)

diff = square_of_sum - sum_of_squares

print(str(diff))









#end of page space holder