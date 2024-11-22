#!/usr/bin/python3
"""
Implementing an in-place algorithm to rotate an n x n 2D matrix
by 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.
    :param matrix: List[List[int]], the n x n 2D matrix to rotate
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
