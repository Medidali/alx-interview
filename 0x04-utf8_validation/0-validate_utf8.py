#!/usr/bin/python3
"""
Validate UTF-8
"""


def validation(data, number, bytes):
    tmp_list = []
    try:
        for x in range(bytes):
            tmp_list.append(
                int("{0:b}".format((data[number + (x + 1)] & 255) >> 6)))

        for val in tmp_list:
            if val != 10:
                return(0)
        return(bytes)
    except IndexError:
        return(-1)


def validUTF8(data):
    """
    validate UTF-8
    """
    step = 0
    for number in range(len(data)):
        if step:
            step -= 1
            continue

        tmp_num = data[number] & 255
        tmp = tmp_num >> 7

        if (int("{0:b}".format(tmp)) == 0):
            continue

        tmp = tmp_num >> 5
        if(int("{0:b}".format(tmp)) == 110):
            step = validation(data, number, 1)
            if step == -1 or step == 0:
                return('False')
            continue

        tmp = tmp_num >> 4
        if(int("{0:b}".format(tmp)) == 1110):
            step = validation(data, number, 2)
            if step == -1 or step == 0:
                return('False')
            continue

        tmp = tmp_num >> 3
        if(int("{0:b}".format(tmp)) == 11110):
            step = validation(data, number, 3)
            if step == -1 or step == 0:
                return('False')
            continue
        return('False')
    return('True')