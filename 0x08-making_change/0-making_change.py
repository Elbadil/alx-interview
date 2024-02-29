#!/usr/bin/python3
"""Defining a function makeChange"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """returns the minimum number of coins to reach the desired total"""
    if total <= 0:
        return 0

    coins.sort()
    i = len(coins) - 1
    total_coins = 0

    while i >= 0:
        while total >= coins[i]:
            total -= coins[i]
            total_coins += 1
        i -= 1

    return total_coins if total == 0 else -1
