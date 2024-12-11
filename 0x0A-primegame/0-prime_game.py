#!/usr/bin/python3
"""
The challenge involves determining the winner of a game based
On the strategic removal of prime numbers and their multiples
from a set of consecutive integers.
"""
def primes(n):
    """
    They play x rounds of the game, where n may be different for each round.
    Assuming Maria always goes first and both players play optimally,
    determine who the winner of each game is.
    """
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """
    They play x rounds of the game, where n may be different for each round.
    Assuming Maria always goes first and both players play optimally,
    determine who the winner of each game is.
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
