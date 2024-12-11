#!/usr/bin/python3
"""
The challenge involves determining the winner of a game based
On the strategic removal of prime numbers and their multiples
from a set of consecutive integers.
"""

def isWinner(x, nums):
    """
    They play x rounds of the game, where n may be different for each round.
    Assuming Maria always goes first and both players play optimally,
    determine who the winner of each game is.
    """

    def sieve(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return primes

    max_n = max(nums)
    primes = sieve(max_n)

    def simulate_game(n):
        remaining = [True] * (n + 1)
        remaining[0] = remaining[1] = False
        count = 0
        
        while True:
            move_made = False
            for p in range(2, n + 1):
                if remaining[p] and primes[p]:
                    move_made = True
                    for multiple in range(p, n + 1, p):
                        remaining[multiple] = False
                    break
            
            if not move_made:
                if count % 2 == 0:
                    return "Ben"
                else:
                    return "Maria"
            count += 1
