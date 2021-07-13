#!/usr/bin/python3
"""ti hao 9alek Module for validUtf8 method wala dra chnowa"""


def to_bits(bytes):
    for byte in bytes:
        num = []
        exp = 1 << NUMBER_OF_BITS_PER_BLOCK
        while exp:
            exp >>= 1
            num.append(bool(byte & exp))
        yield num


"""ti hao 9alek Module for validUtf8 method wala dra chnowa"""


def validUTF8(data):
    bpc = 8
    mno = 4
    index = 0
    while index < len(data):
        number = data[index] & (2 ** 7)
        number >>= (bpc - 1)
        if number == 0:
            index += 1
            continue
        number_of_ones = 0
        while True:
            number = data[index] & (2 ** (7 - number_of_ones))
            number >>= (bpc - number_of_ones - 1)
            if number == 1:
                number_of_ones += 1
            else:
                break
            if number_of_ones > mno:
                return False
        if number_of_ones == 1:
            return False
        index += 1
        if index >= len(data) or index >= (index + number_of_ones - 1):
            return False
        for i in range(index, index + number_of_ones - 1):
            number = data[i]

            number >>= (bpc - 1)
            if number != 1:
                return False
            number >>= (bpc - 1)
            if number != 0:
                return False

            index += 1
    return True
