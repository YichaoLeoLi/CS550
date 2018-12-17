#''' 14. 
#  Write a loop that will print out all the letters of the alphabet.
#'''
import string

letters = list(string.ascii_lowercase)
for i in range(0, 26):
    print (letters[i])
 
# ''' 15. 
#    Now write a loop that will print out "A is a vowel." "B is a consonant." "C is a consonant." and so on. 
# '''
 
letterss = list(string.ascii_uppercase)
for i in range(len(letterss)):
    if (i==0 or i==4 or i==8 or i==14 or i==20):
        print(letterss[i], "is a "+"vowel")
    else:
        print(letterss[i], "is a "+"consonant")

# ''' 16. 
#    Write code that will produce the following output: 
#    122333444455555666666777777788888888999999999
# '''

numbers = []
for i in range(1, 10):
    for j in range(i):
        numbers.append(i)
a = "".join(map(str, numbers))
print(a)



# ''' 17. 
#    Write a loop that will print out the decimal equivalents of 1/2, 1/3, 1/4, 1/5, 1/6, ... 1/20. The output for each iteration should look like:
#    "1/2 = .5" "1/3 = .666666666667" etc.
# '''
 
for i in range(2, 21):
    print("1/"+str(i)+" = "+str(1/i))
 
# ''' 18. 
#    Write a loop that determines the sum of all the numbers from 1-100, as well as the average. Store the sum in variable total (int) and the average in variable avg (float).
# '''
total = 0
for i in range(0, 101):
    total+=i
avg = total/i
print(total, avg)

# ''' 19. 
#    A friend tells you that PI can be computed with the following equation:
#    PI = 4 + 4*(1-1/3+1/5-1/7+1/9-1/11+1/13-1/15...)
#    Write a loop that will calculate this output for n-iterations of the pattern (n being an int), that could help you determine if your friend is right or wrong.
# '''

for i in range(10000):
    PI = 4
    PI += 4*(-1**i*1/(2*(i+1)-1))
    print(PI)

# ''' 20. 
#    A mother rabbit can have a litter of rabbits every month. In the litter, the number of rabbits can vary from 1 to 14 babies per litter, half of which are females. Rabbits can start reproducing at 6 months, so let's add all the new rabbits from the year to the reproductive pool at the end of each year (when their average age is 6 months). Write a simulation that will show how many rabbits will exist at the end of 5 years, starting with just one mother rabbit. 
# '''

import random

 
# ''' 21. 
#    Write some code that will run the rabbit simulation above 1000 times, to help determine what we can expect on average.
# '''



# ''' 22. 
#    Write a loop which prints the numbers 1 to 110, 11 numbers per line. The program shall print "Coza" in place of the numbers which are multiples of 3, "Loza" for multiples of 5, "Woza" for multiples of 7, "CozaLoza" for multiples of 3 and 5, and so on. Sample output:
#    1 2 Coza 4 Loza Coza Woza 8 Coza Loza 11 
#    Coza 13 Woza CozaLoza 16 17 Coza 19 Loza CozaWoza 22 
#    23 Coza Loza 26 Coza Woza 29 CozaLoza 31 32 Coza
#    ......
# '''
numberes = []
numberss = []
for i in range(10):
    numberss = []
    numberes.append(numberss)
    for j in range(1, 12):
        if i == 0:
            numberss.append(j)
        if i == 1:
            numberss.append(11+j)
        if i == 2:
            numberss.append(22+j)
        if i == 3:
            numberss.append(33+j)
        if i == 4:
            numberss.append(44+j)
        if i == 5:
            numberss.append(55+j)
        if i == 6:
            numberss.append(66+j)
        if i == 7:
            numberss.append(77+j)
        if i == 8:
            numberss.append(88+j)
        if i == 9:
            numberss.append(99+j)

for i in range(10):
    for j in range(11):
        print(numberes[i][j])
        print(numberes[i][j]%3 == 0)
        if numberes[i][j]%3 == 0 and numberes[i][j]%5 == 0 and numberes[i][j]%7 == 0:
            numberes[i][j] = "CozaLozaWoza"
        elif numberes[i][j]%3 == 0 and numberes[i][j]%5 == 0:
            numberes[i][j] = "CozaLoza"
        elif numberes[i][j]%3 == 0 and numberes[i][j]%7 == 0:
            numberes[i][j] = "CozaWoza"
        elif numberes[i][j]%5 == 0 and numberes[i][j]%7 == 0:
            numberes[i][j] = "LozaWoza"
        elif numberes[i][j]%3 == 0:
            numberes[i][j] = "Coza"
        elif numberes[i][j]%5 == 0:
            numberes[i][j] = "Loza"
        elif numberes[i][j]%7 == 0:
            numberes[i][j] = "Woza"

for row in numberes:
    for elem in row:
        print(elem, end = ' ')
    print()

# ''' 23.
#    Write code that will print out a times-table for practice and reference. It should look like this:
#     * |  1  2  3  4  5  6  7  8  9
#     -------------------------------
#     1 |  1  2  3  4  5  6  7  8  9
#     2 |  2  4  6  8 10 12 14 16 18
#     3 |  3  6  9 12 15 18 21 24 27
#     4 |  4  8 12 16 20 24 28 32 36
#     5 |  5 10 15 20 25 30 35 40 45
#     6 |  6 12 18 24 30 36 42 48 54
#     7 |  7 14 21 28 35 42 49 56 63
#     8 |  8 16 24 32 40 48 56 64 72
#     9 |  9 18 27 36 45 54 63 72 81
# '''



# ''' 24. 
#    Write code that will produce each of these visual outputs:
#    # # # # # # #    # # # # # # #    # # # # # # #
#    #           #      #       #      # #       # #
#    #           #        #   #        #   #   #   #
#    #           #          #          #     #     #
#    #           #        #   #        #   #   #   #
#    #           #      #       #      # #       # #
#    # # # # # # #    # # # # # # #    # # # # # # #
'''


 
# ''' #25. 
#    Write code that will extract each digit from an int, in the reverse order. For example, if the int is 15423, the output shall be "3 2 4 5 1", with a space separating the digits.
#    Hint: Use n % 10 to extract the least-significant digit; and n = n / 10 to discard the least-significant digit.
# '''