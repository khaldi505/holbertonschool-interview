#!/usr/bin/python3


def makeChange(coins, total):
    """
     determine the fewest number of coins needed to meet a given amount
    """
    if total == 0:
        return 0
    if total < 0:
        return 0
    if len(coins) == 0:
        return 0

    return min(makeChange(coins, total - coin) + 1 for coin in coins)
    # return 1 + makeChange(coins, total - coins[0])

