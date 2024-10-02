#!/usr/bin/python3
"""
Module for Pascal's Triangle Implementation
"""

def pascal_triangle(n):

    """
    Returns a list of lists representing Pascal's triangle of n rows.
        - Returns an empty list if n <= 0
        - Assumes n is always an integer
    """
    if n <= 0:
        return []

    triangle = []

    for row_num in range(n):
        # Start each row with a '1'
        row = [1] * (row_num + 1)

        # Compute the inner values of the row
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

        # Append the row to the triangle
        triangle.append(row)

    return triangle
