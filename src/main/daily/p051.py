# Given a function that generates perfectly random numbers between 1 and k (inclusive), where k
# is an input, write a function that shuffles a deck of cards represented as an array using only swaps.
# It should run in O(N) time.
# Hint: Make sure each one of the 52! permutations of the deck is equally likely.

import random


def rand(k):
    return random.randint(1, k)


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]


def shuffle(a):
    for i in range(1, len(a)):
        swap(a, i, rand(i+1) - 1)


arr = [x for x in range(20)]
print(arr)
shuffle(arr)
print(arr)
