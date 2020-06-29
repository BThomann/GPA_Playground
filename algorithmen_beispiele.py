# Folie 13

def max_sum_1(data):
    maximum = data[0]
    for left in range(len(data)):
        for right in range(left, len(data)):
            sum = 0
            for k in range(left, right + 1):
                sum += data[k]
            if sum > maximum:
                maximum = sum
    return maximum


# Folie 14

def max_sum_1(data):
    maximum = data[0]
    for left in range(len(data)):
        for right in range(left, len(data)):
            sum = 0
            for k in range(left, right + 1):
                print("left =", left, "right = ", right, "k = ", k)
                sum += data[k]
            if sum > maximum:
                maximum = sum
    return maximum


print(max_sum_1([2, 3, -6, 3]))


# Folie 16

def max_sum_2(data):
    maximum = data[0]
    for left in range(len(data)):
        sum = 0
        for right in range(left, len(data)):
            sum += data[right]
            if sum > maximum:
                maximum = sum
    return maximum


# Folie 17

def max_sum_2(data):
    maximum = data[0]
    for left in range(len(data)):
        sum = 0
        for right in range(left, len(data)):
            print("left =", left, "right = ", right)
            sum += data[right]
            if sum > maximum:
                maximum = sum
    return maximum


print(max_sum_2([2, 3, -6, 3]))


# Folie 20

def max_sum_3(data):
    maximum = data[0]
    max_right = 0
    for pos in range(len(data)):
        max_right = max(max_right + data[pos], data[pos])
        maximum = max(maximum, max_right)
    return maximum


# Folie 21

def max_sum_3(data):
    maximum = data[0]
    max_right = 0
    for pos in range(len(data)):
        print("pos =", pos)
        max_right = max(max_right + data[pos], data[pos])
        maximum = max(maximum, max_right)
    return maximum


print(max_sum_3([2, 3, -6, 3]))


# Folie 33

def search_list(data, e):
    for i in data:
        if i == e:
            return True
    return False


print(search_list([1, 2, 3, 4, 5, 2, 3, 9], 1))
print(search_list([1, 2, 7, 4, 5, 8, 3, 9], 4))
print(search_list([1, 2, 7, 4, 5, 8, 3, 9], 6))


# Folie 50

def int_to_str(n):
    digits = "0123456789"
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = digits[n % 10] + result
        n = n // 10
    return result


# Folie 52

def add_numbers(data):
    val = 0
    for num in data:
        val += num
    return val


# Folie 53

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


# Folie 55

def unique(data):
    for j in range(len(data)):
        for k in range(j + 1, len(data)):
            if data[j] == data[k]:
                return False
    return True


# Folie 56

def disjoint(l1, l2, l3):
    for a in l1:
        for b in l2:
            for c in l3:
                if a == b == c:
                    return False
    return True


# Folie 58

def solve_hanoi(n, origin, spare, to):
    if n > 0:
        solve_hanoi(n - 1, origin, to, spare)
        print("move from " + str(origin) + " to " + str(to))
        solve_hanoi(n - 1, spare, origin, to)
