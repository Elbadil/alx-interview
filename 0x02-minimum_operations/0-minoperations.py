#!/usr/bin/python3
"""Defining a function minOperations"""


def minOperations(n: int) -> int:
    """returns minimun operations needed to result in exactly n H characters"""
    # If "n" is "1" there are no operations (0) to take
    if n == 1:
        return 0

    # Extracting prime factors from "n"
    num = 2
    operations = []
    while num <= n:
        if n % num == 0:
            operations.append(num)
            n /= num
        else:
            num += 1
    if n > 1:
        operations.append(n)

    # if it's a prime number return 0
    if len(operations) == 1:
        return 0

    # else return the sum of the prime factors "operations"
    return sum(operations)
