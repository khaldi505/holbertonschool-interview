#!/usr/bin/python3
"""
Pascal Triangle
"""



def pascal_triangle(n):
    """
    Return a list of lists of integers representing the Pascal
    """
    if n <= 0:
        return []
    result = [[1]]
    for i in range(1, n):
        result.append([1] + [result[i-1][j] + result[i-1][j+1] for j in range(len(result[i-1])-1)] + [1])
    return result
