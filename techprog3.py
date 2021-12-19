import math
import re


def reading(n):
    f = open(n, 'r')
    line = ''
    for i in f:
        line = line + i + ' '
    line.strip()
    line = re.sub(r'\s+', ' ', line)
    line = re.sub(r'(\n|\t)', ' ', line)
    line = line.split(' ')
    if line[0] == '':
        down = 1
    else:
        down = 0
    if line[-1] == '':
        up = len(line) - 1
    else:
        up = len(line)
    line = line[down:up]
    for i in line:
        try:
            value = float(i)
        except Exception:
            return "InvalidFile"
    for i in range(len(line)):
        if '.' in line[i]:
            line[i] = float(line[i])
        else:
            line[i] = int(line[i])
    return line


def minimum(arr):
    if arr != "InvalidFile":
        min_ = arr[0]
        for ele in arr:
            if ele < min_:
                min_ = ele
        return min_
    else:
        return "InvalidFile"


def large(arr):
    if arr != "InvalidFile":
        max_ = arr[0]
        for ele in arr:
            if ele > max_:
                max_ = ele
        return max_
    else:
        return "InvalidFile"


def summarize(arr):
    if arr != "InvalidFile":
        sum_number = 0
        for chislo in arr:
            sum_number += chislo
        return sum_number
    else:
        return "InvalidFile"


def prod(arr):
    if arr != "InvalidFile":
        try:
            answ = math.prod(arr)
            return answ
        except OverflowError:
            return "OverflowError"
    else:
        return "InvalidFile"
