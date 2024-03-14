#!/usr/bin/python3
"""Defining a function isWinner"""


def isWinner(x, nums):
    """Returns the winner of the prime game of numbers"""
    def is_prime(n):
        """Returns true if n is a prime number else False"""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    maria_ws = 0
    ben_ws = 0
    for n in nums:
        # If n is even, Ben wins since Maria can't pick a prime
        if n % 2 == 0:
            ben_ws += 1
        # If n is odd and prime, Maria wins since she picks the
        # only available prime
        elif is_prime(n):
            maria_ws += 1
        # If n is odd but not prime
        # Ben wins since he removes the prime
        # factors and leaves Maria with 1
        else:
            ben_ws += 1

    if maria_ws > ben_ws:
        return "Maria"
    elif ben_ws > maria_ws:
        return "Ben"
    else:
        return None
