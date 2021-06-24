# Using a function rand5() that returns an integer from 1 to 5 (inclusive)
# with uniform probability, implement a function rand7() that returns an integer
# from 1 to 7 (inclusive).

import random


def rand5():
    return int(random.randint(1,5))


def rand7():
    r = 21
    while r > 20:
        r = 5 * (rand5() - 1) + rand5() - 1
    return int(r / 3) + 1


n = [0] * 7

for i in range(10000):
    n[rand7()-1] += 1

for i,v in enumerate(n,start=1):
    print("{} => {}".format(i,v))

