# https://www.hackerrank.com/challenges/s10-mcq-1/problemhttps://www.hackerrank.com/challenges/s10-mcq-1/problem

from itertools import product
from fractions import Fraction

P = list(product([1, 2, 3, 4, 5, 6], repeat=2))

N = sum(1 for x in P if sum(x) <= 9)

print(Fraction(N, len(P)))

# >>> 5/6

########## SECOND WAY ############

# Set data
dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]
total = len(dice1) * len(dice2)
total_possibilities = 0

# Verify possibilities
for i in range(len(dice1)):
    for j in range(len(dice2)):
        if (dice1[j] + dice1[i]) <= 9:
            total_possibilities = total_possibilities + 1
            print("{0} + {1} = {2}".format(dice1[i], dice2[j], (dice1[j] + dice1[i])))

# Get probability
probability = total_possibilities / total
print("Probability: {0}/{1} = {2}".format(total_possibilities,total,probability))
