#!/usr/bin/python3

"""
this function will unlock boxes based on the keys inside of em

"""


def canUnlockAll(boxes):

    length = len(boxes) - 1
    unlocked_boxes = []
    for f_keys in boxes[0]:
        if f_keys not in unlocked_boxes and f_keys <= length:
            unlocked_boxes.append(f_keys)
    for x in range(length + 1):
        if x in unlocked_boxes:
            for y in boxes[x]:
                if y not in unlocked_boxes and y <= length:
                    unlocked_boxes.append(y)
    if (len(unlocked_boxes) == length) or\
            (length == 0 and len(unlocked_boxes) == 1):
        return True
    else:
        return False
