# Folie 6

def linear_search(data, elem):
    for i in range(len(data)):
        if elem == data[i]:
            return True
    return False


def linear_search_2(data, elem):
    for i in data:
        if elem == i:
            return True
    return False


print(linear_search([3, 2, 1, 4, 2, 5, 3, 8], 8))
print(linear_search([3, 2, 1, 4, 2, 5, 3, 8], 7))
print(linear_search_2([3, 2, 1, 4, 2, 5, 3, 8], 8))
print(linear_search_2([3, 2, 1, 4, 2, 5, 3, 8], 7))


# Folie 9

def linear_search(data, elem):
    for i in range(len(data)):
        if elem == data[i]:
            return i
    return -1


def linear_search_2(data, elem):
    for i, item in enumerate(data):
        if elem == item:
            return i
    return -1


print(linear_search([3, 2, 1, 4, 2, 5, 3, 8], 8))
print(linear_search([3, 2, 1, 4, 2, 5, 3, 8], 7))
print(linear_search_2([3, 2, 1, 4, 2, 5, 3, 8], 8))
print(linear_search_2([3, 2, 1, 4, 2, 5, 3, 8], 7))


# Folie 10

def linear_search(data, elem):
    for i in data:
        if i == elem:
            return True
        if i > elem:
            return False
    return False


print(linear_search([1, 2, 3, 4, 5, 6, 7, 8], 5))
print(linear_search([1, 2, 3, 4, 5, 6, 7, 8], 0))
print(linear_search([1, 2, 3, 4, 5, 6, 7, 8], 9))


# Folie 15


def binary_search(data, elem):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if elem == data[mid]:
            return True
        elif elem < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


vals = [1, 4, 6, 7, 9, 11, 12, 13, 15, 17, 18, 20, 22, 24, 25]
print(binary_search(vals, 9))
print(binary_search(vals, 1))
print(binary_search(vals, 25))
print(binary_search(vals, 2))
print(binary_search(vals, 30))


# Folie 21

def binary_search(data, elem):
    def binary_search_helper(data, elem, low, high):
        if low > high:
            return False
        else:
            mid = (low + high) // 2
            if elem == data[mid]:
                return True
            elif elem < data[mid]:
                return binary_search_helper(data, elem, low, mid - 1)
            else:
                return binary_search_helper(data, elem, mid + 1, high)

    return binary_search_helper(data, elem, 0, len(data) - 1)


vals = [1, 4, 6, 7, 9, 11, 12, 13, 15, 17, 18, 20, 22, 24, 25]
print(binary_search(vals, 9))
print(binary_search(vals, 1))
print(binary_search(vals, 25))
print(binary_search(vals, 2))
print(binary_search(vals, 30))


# Folie 33, 34


class IntTable:

    def __init__(self, num_buckets):
        self.buckets = []
        self.num_buckets = num_buckets
        for i in range(num_buckets):
            self.buckets.append([])

    def add_entry(self, key):
        hash_bucket = self.buckets[key % self.num_buckets]
        if key not in hash_bucket:
            hash_bucket.append(key)

    def __contains__(self, key):
        hash_bucket = self.buckets[key % self.num_buckets]
        return key in hash_bucket

    def __str__(self):
        return "\n".join([str(b) for b in self.buckets])


import random

d = IntTable(13)
for i in range(20):
    k = random.choice(range(10 ** 4))
    d.add_entry(k)
d.add_entry(12)
d.add_entry(12)
print(12 in d)
print(123456 in d)
print('Content of the table:')
print(d)


# Folie 35, 36

class IntTable:

    def __init__(self, num_buckets):
        self.buckets = []
        self.num_buckets = num_buckets
        for i in range(num_buckets):
            self.buckets.append([])

    def add_entry(self, key, val):
        hash_bucket = self.buckets[key % self.num_buckets]
        for i in range(len(hash_bucket)):
            if hash_bucket[i][0] == key:
                hash_bucket[i] = (key, val)
                return
        hash_bucket.append((key, val))

    def get_val(self, key):
        hash_bucket = self.buckets[key % self.num_buckets]
        for e in hash_bucket:
            if e[0] == key:
                return e[1]
        return None

    def __str__(self):
        return "{" + ", ".join([":".join(map(str, e)) for b in self.buckets for e in b]) + "}"


import random

d = IntTable(13)
for i in range(20):
    k = random.choice(range(10 ** 4))
    d.add_entry(k, i)
print('The value of the intDict is:')
print(d)
print('\n', 'The buckets are:')
for hash_bucket in d.buckets:
    print('  ', hash_bucket)
