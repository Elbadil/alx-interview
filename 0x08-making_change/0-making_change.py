#!/usr/bin/python3
"""Defining a function makeChange"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """returns the minimum number of coins to reach the desired total"""
    if total <= 0:
        return 0

    coins_copy = coins.copy()
    max_coin = max(coins)
    total_coins = 0
    total_value = 0

    while total_value != total:
        if total_value + max_coin > total:
            coins.remove(max_coin)
            try:
                max_coin = max(coins)
            except ValueError:
                if len(coins_copy) <= 1:
                    break
                coins_copy.remove(max(coins_copy))
                coins = coins_copy.copy()
                max_coin = max(coins)
        else:
            total_value += max_coin
        if total_value != total:
            total_coins += 1

    return total_coins if total_value == total else -1
