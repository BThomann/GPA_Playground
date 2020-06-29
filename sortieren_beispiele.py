# Folie 5

def insertion_sort(data):
    for i in range(1, len(data)):
        j = i
        while (j > 0) and (data[j] < data[j - 1]):
            data[j - 1], data[j] = data[j], data[j - 1]
            j -= 1


vals = [12, 3, 7, 4, 9, 2, 5, 6, 1]
insertion_sort(vals)
print(vals)


# Folie 8

def insertion_sort_2(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i
        while (j > 0) and (key < data[j - 1]):
            data[j] = data[j - 1]
            j -= 1
        data[j] = key


vals = [12, 3, 7, 4, 9, 2, 5, 6, 1]
insertion_sort(vals)
print(vals)


# Folie 10

def selection_sort(data):
    for i in range(len(data) - 1):
        min_index = i
        for j in range(i, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]


vals = [12, 3, 7, 4, 9, 2, 5, 6, 1]
selection_sort(vals)
print(vals)


# Folie 21

def merge(S1, S2, S):
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i + j] = S1[i]
            i += 1
        else:
            S[i + j] = S2[j]
            j += 1


def merge_sort(S):
    n = len(S)
    if n < 2:
        return
    mid = n // 2
    S1 = S[0:mid]
    S2 = S[mid:n]
    merge_sort(S1)
    merge_sort(S2)
    merge(S1, S2, S)


vals = [12, 3, 7, 4, 9, 2, 5, 6, 1]
merge_sort(vals)
print(vals)


# Folie 27

def merge(a, lo, mid, hi, aux):
    n = hi - lo
    i = lo
    j = mid
    for k in range(n):
        if i == mid:
            aux[k] = a[j]
            j += 1
        elif j == hi:
            aux[k] = a[i]
            i += 1
        elif a[j] < a[i]:
            aux[k] = a[j]
            j += 1
        else:
            aux[k] = a[i]
            i += 1
    a[lo:hi] = aux[0:n]


def sort_helper(a, lo, hi, aux):
    n = hi - lo
    if n <= 1:
        return
    mid = (lo + hi) // 2
    sort_helper(a, lo, mid, aux)
    sort_helper(a, mid, hi, aux)
    merge(a, lo, mid, hi, aux)


def merge_sort(data):
    n = len(data)
    aux = data[:]
    sort_helper(data, 0, n, aux)


vals = [12, 3, 7, 4, 9, 2, 5, 6, 1]
merge_sort(vals)
print(vals)

# Folie 28

import math


def merge(src, result, start, inc):
    end1 = start + inc
    end2 = min(start + 2 * inc, len(src))
    x, y, z = start, start + inc, start
    while x < end1 and y < end2:
        if src[x] < src[y]:
            result[z] = src[x]
            x += 1
        else:
            result[z] = src[y]
            y += 1
        z += 1
    if x < end1:
        result[z:end2] = src[x:end1]
    elif y < end2:
        result[z:end2] = src[y:end2]


def merge_sort(data):
    n = len(data)
    logn = math.ceil(math.log(n, 2))
    src, dest = data, [None] * n
    for i in (2 ** k for k in range(logn)):
        for j in range(0, n, 2 * i):
            merge(src, dest, j, i)
        src, dest = dest, src
    if data is not src:
        data[0:n] = src[0:n]


vals = [12, 3, 7, 4, 9, 2, 5, 6, 1]
merge_sort(vals)
print(vals)
