#Chris Kopacz
#Project Euler
#Problem 17 - Number letter counts
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: DO not count spaces or hyphens. For example, 243 (three hundred and
forty-two) contains 23 letters, and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance with
British usage.
"""

letters = []
count = 0
hundreds = 0
tens = 0
ones = 0
temp = 0

for iter in range(0,100):
    letters.append(0)

letters[0] = 0
letters[1] = 3 #one
letters[2] = 3 #two
letters[3] = 5 #three
letters[4] = 4 #four
letters[5] = 4 #five
letters[6] = 3 #six
letters[7] = 5 #seven
letters[8] = 5 #eight
letters[9] = 4 #nine
letters[10] = 3 #ten
letters[11] = 6 #eleven
letters[12] = 6 #twelve
letters[13] = 8 #thirteen
letters[14] = 8 #fourteen
letters[15] = 7 #fifteen
letters[16] = 7 #sixteen
letters[17] = 9 #seventeen
letters[18] = 8 #eighteen
letters[19] = 8 #nineteen
letters[20] = 6 #twenty
letters[30] = 6 #thirty
letters[40] = 5 #forty
letters[50] = 5 #fifty
letters[60] = 5 #sixty
letters[70] = 7 #seventy
letters[80] = 6 #eighty
letters[90] = 6 #ninety

for iter in range(1,1001):
    #print(iter)

    hundreds = 0
    tens = 0
    ones = 0
    temp = 0

    if iter < 21:
        count += letters[iter]
    elif iter > 20 and iter < 100:
        tens = int(iter/10)*10
        count += letters[tens]

        ones = iter%10
        count += letters[ones]
    elif iter == 1000:
        count += 11 #one thousand
    else:
        if iter % 100 == 0:
            hundreds = int(iter/100)
            count += letters[hundreds]
            count += 7 #hundred
        else:
            hundreds = int(iter/100)
            count += letters[hundreds]
            count += 10 #hundred and

            tens = int(iter/10)%10*10
            if tens != 10:
                count += letters[tens]

                ones = iter%10
                count += letters[ones]
            else:
                temp = tens + iter%10
                count += letters[temp]

    #print(str(count))

print(str(count))

































#end of page space holder
