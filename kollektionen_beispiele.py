# Folie 13

a = (1, 2, 3)
b = ("Hello", "World")
c = (1, 2, (3, 4, (5, 6)))
d = (1, "Test", ("Here", (2, 3), "And"), 5)
print(len(a), len(b), len(c), len(d))
print(a[1], b[1])
print(c[2], c[2][2], c[2][2][0])
print(d[2][0:2])
print(a + b)
print(a * 3)
a, b = b, a
print(a)
print(b)


# Folie 14

def read_input():
    name = input("Name: ")
    year_of_birth = 0
    while not (1900 < year_of_birth < 2020):
        year_of_birth = int(input("Year of birth: "))
    return name, year_of_birth


n, y = read_input()
print(n, y)

# Folie 18

a = [1, 2, 3]
b = ["Hello", "World"]
c = [1, 2, [3, 4, [5, 6]]]
d = [1, "Test", ["Here", [2, 3], "And"], 5]
print(len(a), len(b), len(c), len(d))
print(a[1], b[1])
print(c[2], c[2][2], c[2][2][0])
print(d[2][0:2])
print(a + b)
print(a * 3)
a, b = b, a
print(a)
print(b)

# Folie 22

s = [8, 7, 6, 5, 1, 2, 3, 4]
print("s =", s)
s[1] = 10
print("s[1] = 10 ->", s)
s[3:5] = [10, 20, 30, 40]
print("s[3:5] = [10, 20, 30, 40] ->", s)
s.append(33)
print("s.append(33) ->", s)
del s[0]
print("del s[0] ->", s)
s.extend([77, 88, 99])
print("s.extend([77, 88, 99]) ->", s)
print("s.count(10) =", s.count(10))
print("s.index(77) =", s.index(77))
item = s.pop()
print("item = s.pop() ->", s, " removed element =", item)
s.insert(1, 1000)
print("s.insert(1, 1000) ->", s)
s.remove(10)
print("s.remove(10) ->", s)
s.reverse()
print("s.reverse() ->", s)
s.sort()
print("s.sort() ->", s)

# Folie 29

import copy

a = [[1, 2], [3, 4]]
b = a.copy()
c = copy.deepcopy(a)
print(a, b, c, sep="\n")
a[0][0] = 9
print(a, b, c, sep="\n")
a[0] = [4, 5]
print(a, b, c, sep="\n")


# Folie 37

def squares(numbers):
    for i in numbers:
        numbers[i] = numbers[i] * numbers[i]


def init(bound):
    result = []
    for i in range(bound):
        result.append(i)
    return result


numbers = init(5)
print(numbers)
squares(numbers)
print(numbers)


# Folie 38

def my_sum(numbers):
    if (len(numbers) == 0):
        return 0
    else:
        return numbers[0] + my_sum(numbers[1:])


print(my_sum([]))
print(my_sum([2]))
print(my_sum([2, 4, 5, 6]))


# Folie 39

def search(numbers, code):
    if len(numbers) == 1:
        if numbers[0][:len(code)] == code:
            return numbers
        else:
            return []
    else:
        return search(numbers[:len(numbers) // 2], code) + \
               search(numbers[len(numbers) // 2:], code)


friends = ["0123 123456",
           "0123 456789",
           "0222 334455",
           "0122 556677",
           "0222 887766"]
print(search(friends, "0222"))
print(search(friends, "0111"))
print(search(friends, "0123"))


# Folie 41

def gen_matrix(rows, columns, value=None):
    a = [None] * rows
    for row in range(rows):
        a[row] = [value] * columns
    return a


def print_matrix(matrix):
    for row in matrix:
        for i in row:
            print(i, end=" ")
        print()


r = 4
c = 3
m1 = gen_matrix(r, c, 0)
print(m1)
print("----")
print_matrix(m1)
print("----")
m1[1] = [(i + 1) ** i for i in range(0, c)]
m1[r - 1][0] = 3
print_matrix(m1)

# Folie 42

import random


def gen_matrix(rows, columns, value=None):
    return [[value] * columns for _ in range(rows)]


def print_matrix(matrix):
    for row in matrix:
        print(*row)


r = 4
c = 3
m1 = gen_matrix(r, c, 1)
print(m1)
print("----")
print_matrix(m1)
print("----")
m1[0][0] = random.randrange(0, 10, 1)
m1[1] = [random.randrange(1, 10, 1) for i in range(0, c)]
print_matrix(m1)


# Folie 46

def generate(n):
    for i in range(n):
        yield i * i


g = generate(10)
print(g)
for i in g:
    print(i, end=" ")


# Folie 49

def generate(n):
    for i in range(n):
        yield i * i


g = generate(10)
print(g)
print(next(g))
print(next(g))


# Folie 50

def generate():
    i = 1
    while True:
        yield i * i
        i += 1


g = generate()
print(next(g))
print(next(g))
print(next(g))

# Folie 53

g = (i * i for i in range(10))
for i in g:
    print(i, end=" ")
print("\n---")
for i in g:
    print(i, end=" ")
g = (i * i for i in range(10))
print(max(g))
print(max(g))

# Folie 56

a = set([3, 1, 3, 1, 2])
b = {"World", "Hello", "Hello"}
c = frozenset([1, 2, 1, 3, 1])
d = set("This is a test!")
print(a)
print(b)
print(c)
print(d)

# Folie 59

a = {3, 5, 2, 3, 2, 5, 7}
b = {3, 1, 2}
print("a:", a)
print("b:", b)
print("len(a) =", len(a))
print("max(a) =", max(a))
print("min(a) =", min(a))
print("2 in a =", 2 in a)
print("2 not in a =", 2 not in a)
c = a.copy()
print("c:", c)
print("a - b =", a - b)
print("a & b =", a & b)
d = {3, 1, 2, 4}
print("d:", d)
print("b <= d =", b <= d)
print("a <= b =", a <= b)
print("d >= b =", d >= b)
print("a >= b =", a >= b)
print("a | b =", a | b)

# Folie 61

a = {4, 1, 2}
print("a = {4, 1, 2} ->", a)
a.add(3)
print("a.add(3) ->", a)
a.add(1)
print("a.add(1) ->", a)
a.clear()
print("a.clear() ->", a)
a = {4, 1, 2}
print("a = {4, 1, 2} ->", a)
a.discard(4)
print("a.discard(4) ->", a)
x = a.pop()
print("a.pop() ->", a, " removed element =", x)
a.remove(2)
print("a.remove(2) ->", a)

# Folie 63

triangles = {frozenset((a, b, c))
             for a in range(1, 20)
             for b in range(1, 20)
             for c in range(1, 20)
             if a ** 2 + b ** 2 == c ** 2}
for t in triangles:
    print(tuple(t))

# Folie 71

d = {"A": 10, "B": 20, "C": 30}
print("d = ", d)
print("d[\"A\"] =", d["A"])
d["A"] = 40
print("d[\"A\"] = 40 ->", d)
e = d.copy()
print("e = d.copy() -> e =", e)
del d["B"]
print("del d[\"B\"] ->", d)
item = d.get("D", 50)
print("item = d.get(\"D\", 50) -> item =", item)
print("\"A\" in d =", "A" in d)
print("\"E\" in d =", "E" in d)
item = d.setdefault("E", 70)
print("item = d.setdefault(\"E\", 70) -> item =", item)
print("item = d.setdefault(\"E\", 70) -> d =", d)
new_d = {"A": 10, "B": 20, "C": 30}
print("new_d =", new_d)
d.update(new_d)
print("d.update(new_d) ->", d)

# Folie 73

d = {"A": 10, "B": 20, "C": 30}
di = d.items()
dk = d.keys()
dv = d.values()
print("d.items() ->", di)
print("d.keys() ->", dk)
print("d.values() ->", dv)
d["A"] = 40
d["E"] = 70
print("items ->", di)
print("keys ->", dk)
print("values ->", dv)

# Folie 75

s1 = "Hello"
s2 = "Hello"
s3 = "elloH"
print(s1 == s2, s1 == s3)
l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 4]
l3 = [4, 1, 2, 3]
print(l1 == l2, l1 == l3)
st1 = {2, 3, 4, 5, 4, 2}
st2 = {2, 5, 3, 4}
st3 = {2, 3, 4}
print(st1 == st2, st1 == st3)
d1 = {"A": 10, "B": 20, "C": 30}
d2 = {"C": 30, "A": 10, "B": 20}
d3 = {"A": 10, "B": 20}
print(d1 == d2, d1 == d3)
