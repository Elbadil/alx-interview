#!/usr/bin/python3
"""Defining a function minOperations"""


def minOperations(n: int) -> int:
    """returns minimun operations needed to result in exactly n H characters"""
    if n == 1:
        return 0
    # We have to available Operations [CopyAll, Paste]
    hSome = "H"
    counter = 0
    temp = ""
    temp2 = ""

    for i in range(n):
        # First Iteration we will "CopyAll" and "Paste"
        if i == 0:
            hSome += hSome
            # two operations
            counter += 2
            if len(hSome) == n:
                return counter
        # Second Iteration we will define if the number is even or odd
        elif i == 1:
            # if it's an odd number we will only "Paste"
            if n % 2 != 0:
                hSome += "H"
                # one operation
                counter += 1
                if len(hSome) == n:
                    return counter
            # if it's an even number we will "CopyAll" and "Paste"
            else:
                hSome += hSome
                # two operations
                counter += 2
                if len(hSome) == n:
                    return counter
        else:
            # we will keep "CopyingAll and Pasting" until the number
            # of "H"s is equal or larger than "n"
            temp = hSome
            hSome += hSome
            # two operations
            counter += 2
            # if the number of "H"s is eqaul to n we return the counter
            if len(hSome) == n:
                return counter
            elif len(hSome) > n:
                hSome = "H" * len(temp)
                temp2 = len(temp) / 2
                hSome += "H" * int(temp2)
                counter -= 1
                if len(hSome) == n:
                    return counter
                else:
                    return 0
