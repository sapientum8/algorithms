# Given a array of numbers representing the stock prices of a company in chronological
# order, write a function that calculates the maximum profit you could have made from
# buying and selling that stock once. You must buy before you can sell it.
# For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at
# 5 dollars and sell it at 10 dollars.

def brute(prices):
    """ brute force @ O(n^2) """
    m = 0
    for i,p in enumerate(prices):
        for j in range(i,len(prices)):
            m = max(m,prices[j] - p)
    return m


def max_profit(prices):
    """ linear O(N) spacetime algorithm """
    cmax, m = 0, 0
    for p in reversed(prices):
        cmax = max(cmax,p)
        m = max(m,cmax - p)
    return m


print(brute([9, 11, 8, 5, 7, 10]))

print(max_profit([9, 11, 8, 5, 7, 10]))
