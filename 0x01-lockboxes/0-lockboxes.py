#!/usr/bin/python3

"""
A method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Box:
      -  boxes is a list of lists
      -  A key with the same number as a box opens that box
      -  You can assume all keys will be positive integers
      -  There can be keys that do not have boxes
      -  The first box boxes[0] is unlocked
      -  Return True if all boxes can be opened, else return False
    """

    ln = len(boxes)
    unlocked = [False] * ln
    unlocked[0] = True  # Box 0 is already unlocked

    keys = [0]

    while keys:
        current_box = keys.pop()

        for key in boxes[current_box]:
            if key < ln and not unlocked[key]:

                unlocked[key] = True
                keys.append(key)

    return all(unlocked)
