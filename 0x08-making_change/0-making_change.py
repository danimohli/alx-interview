#!/usr/bin/python3
"""
a pile of coins of different values,
determine the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Edge case: if total is less than or equal to 0, return 0
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)

    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    return dp[total]