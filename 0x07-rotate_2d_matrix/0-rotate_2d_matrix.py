#!/usr/bin/python3
"""Defining a function rotate_2d_matrix"""


def rotate_2d_matrix(matrix):
    """rotates 2d matrix in-place"""
    temp = [[]]
    N = len(matrix) # = 3

    # Transposing the matrix changing the columns with th rows
    for i in range(N):  # i = 0 # i = 1 # i = 2
        for j in range(i, N):  # j = 0 | = 1 | = 2 // j = 1 | j = 2 // j = 2
            temp = matrix[i][j]  # 1 # = 2 # = 3 // = 5 | = 6 // = 9
    # 1) 1 will be changing position with 1
    # 2) 2 will be changing position with 4 first element in the second list
    # 3) 3 will be changing position with 7 first element in the third list
    # ------------------------- i = 1 ----------------------------------------
    # 1) 5 will be changing position with 5 second element in the second list
    # 2) 6 will be changing position with 8 second element in the third list
    # ------------------------- i = 2 ----------------------------------------
    # 1) 9 will be changing position with 9
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    # reverse the elements in the matrix
    for i in range(N):  # i = 0 # i = 1
        for j in range(i + 1 if i == 0 else i, N):  
            # j = 0 # j = 1 # j = 2 // # j = 1
            temp = matrix[i][j]
            # 1 # 4 # 7 // # 5
            matrix[i][j] = matrix[i][N - 1 - j]  
            # 7 # 4 # 1 // # 5 
            matrix[i][N - 1 - j] = temp  
            # 1 # 4 # 7 #
