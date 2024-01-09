#!/usr/bin/python3
"""Defining a function called canUnlockAll"""


def appendKeys(availableKeys, box):
    """appends box keys to the available keys list"""
    for key in box:
        availableKeys.append(key)
    return availableKeys


def canUnlockAll(boxes):
    """returns True if all boxes can be opened else
    False"""
    availableKeys = boxes[0]
    openedBoxes = []
    lastRemainig = []
    currentBox = []
    for i, box in enumerate(boxes):
        if i == 0:
            continue
        elif len(box) == 0:
            for key in availableKeys:
                if key == i:
                    currentBox = boxes[i]
                    appendKeys(availableKeys, currentBox)
                    openedBoxes.append(currentBox)
                    break
        elif len(box) == 1:
            if box[0] == i:
                currentBox = boxes[i]
                appendKeys(availableKeys, currentBox)
                openedBoxes.append(currentBox)
            else:
                for key in availableKeys:
                    if key == i:
                        currentBox = boxes[i]
                        appendKeys(availableKeys, currentBox)
                        openedBoxes.append(currentBox)
                        break
        elif len(box) > 1:
            for key in availableKeys:
                if key == i:
                    currentBox = boxes[i]
                    appendKeys(availableKeys, currentBox)
                    openedBoxes.append(currentBox)
                    break

    # Cleaning up the boxes we opened from the boxes List
    for box in openedBoxes:
        boxes.remove(box)

    # Appending the last boxes that can be opened
    if len(boxes) > 1:
        for i, box in enumerate(boxes):
            if i == 0:
                continue
            for key in box:
                if key in availableKeys:
                    currentBox = boxes[i]
                    lastRemainig.append(currentBox)
                    break

    # Cleaning up the last remaining opened boxes we opened from the boxes List
    for box in lastRemainig:
        boxes.remove(box)

    if len(boxes) == 1:
        return True
    return False
