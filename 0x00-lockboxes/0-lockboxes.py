#!/usr/bin/python3

"""
this function will unlock boxes based on the keys inside of em

"""


def canUnlockAll(boxes):
    unlocked = True
    length = len(boxes) - 1
    unlocked_boxes = []
    for f_keys in boxes[0]:
        if not f_keys in unlocked_boxes and not f_keys > length:
            unlocked_boxes.append(f_keys)
    for x in range(length):
        if x in unlocked_boxes:
            for y in boxes[x]:
                if not y in unlocked_boxes and not y > length:
                    unlocked_boxes.append(y)
    if len(unlocked_boxes) == length:
        return unlocked
    else:
        return False
