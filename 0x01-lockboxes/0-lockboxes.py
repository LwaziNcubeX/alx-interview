#!/usr/bin/python3
"""A method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened."""
    key_count = [0] * len(boxes)
    key_count[0] = 1  # Set the first box as unlocked

    for i in range(len(boxes)):
        for key in boxes[i]:
            if key < len(boxes) and key != i:  # Exclude key to itself
                key_count[key] += 1

    return all(key_count[i] > 0 for i in range(1, len(boxes)))
