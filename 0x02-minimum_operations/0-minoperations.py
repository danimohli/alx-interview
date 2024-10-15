#!/usr/bin/python3
"""
The optimal strategy to minimize operations revolves around
"""


def minOperations(n):
    """
    The optimal strategy to minimize operations revolves around
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
