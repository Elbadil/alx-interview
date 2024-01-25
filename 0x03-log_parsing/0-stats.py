#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""
import sys


status_codes = {}
file_size = 0
counter = 10
i = 0

for line in sys.stdin:
    elements = line.split(' ')
    size = int(elements[8])
    stat_code = elements[7]
    # print(line)
    # Checking the format of the line
    if len(elements) != 9:
        continue
    if i < counter:
        # setting status codes to the their counter value
        if stat_code not in status_codes:
            if stat_code and stat_code.isdigit():
                status_codes[stat_code] = 1
            else:
                continue
        else:
            status_codes[stat_code] += 1
        file_size += size
        counter -= 1
    else:
        print(f'File size: {file_size}')
        # Sorting the status_codes dictionary in ascending order
        stts_code_sorted = {
            key: val for key, val in sorted(status_codes.items(),
                                            key=lambda ele: ele[0])}
        for key in stts_code_sorted.keys():
            print(f'{key}: {stts_code_sorted[key]}')
        counter = 10
