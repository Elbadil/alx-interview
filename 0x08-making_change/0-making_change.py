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
        # print(f'Before: {total_value}\n-----')
        if total_value + max_coin > total:
            # print(f'Cant double {max_coin}')
            coins.remove(max_coin)
            try:
                max_coin = max(coins)
                # print(f'Max coin is now: {max_coin}')
            except ValueError:
                # print()
                # print('Oops we must refresh the list by removing the old max num')
                # print('because the value we got is higher than total')
                # print()
                if len(coins_copy) <= 1:
                    break
                coins_copy.remove(max(coins_copy))
                coins = coins_copy.copy()
                max_coin = max(coins)
                total_value = 0
        else:
            # print(f'{total_value} += {max_coin}')
            total_value += max_coin
            # print(f'After: {total_value}\n-----')
        if total_value != total:
            total_coins += 1

    return total_coins if total_value == total else -1
