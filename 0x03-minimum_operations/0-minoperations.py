#!/usr/bin/python3

"""
few ops calculator go brerererere
"""


def minOperations(n):
    op = 0
    x = 2
    while n > 1:
        while n % x == 0:
            op += x
            n = int(n / x)
        x += 1
    return op
