# Folie 8

def print_hello():
    print("Hello!")


print_hello()
for i in range(3):
    print_hello()


# Folie 11

def print_line(number):
    print("*" * number)


print_line(3)
print_line(8)


# Folie 12

def print_lines(symbol, line_length, num_lines):
    for i in range(num_lines):
        print(symbol * line_length)


print_lines("-", 3, 1)
print_lines("#", 8, 2)
print_lines("*-*", 5, 3)


# Folie 13

def print_text(text, step):
    for i in text[::step]:
        print(i, end=" ")


print_text("Hello World!", 2)


# print_text(2, "Hello World!") TypeError!

# Folie 14

def print_text(text, space):
    print("*" + " " * space + text + " " * space + "*")


def print_line(number):
    print("-" * number)


def print_pattern(text, space):
    line_width = space * 2 + len(text) + 2
    print_line(line_width)
    print_text(text, space)
    print_line(line_width)


print_pattern("Hello", 5)
print_pattern("World", 4)
print_pattern("GPA", 1)


# Folie 15

def calc(value_1, value_2):
    return value_1 + value_2


x = calc(10, 20)
print(x)
y = calc(x, x + x)
print(y)


# Folie 16

def hello():
    print("Hello")


def give_answer():
    return 42


x = hello()
print(x)
y = give_answer()
print(y)


# Folie 17

def maximum(a, b):
    if a > b:
        return a
    else:
        return b


x = maximum(10, 20)
print(x)
print(maximum(x, maximum(-40, 50)))


# Folie 18

def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                return False
        return True


print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(15))
print(is_prime(997))


# Folie 21

def print_table(number=5, step=0.5):
    x = 0.0
    print("Table of values")
    for i in range(number):
        print(x, " ", x * x)
        x += step


print_table()
print_table(3)
print_table(3, 2)


# Folie 23

def report(name, first_name, diagnose):
    print("examination report")
    print("------------------")
    print("patient:", first_name, name)
    print("diagnose:", diagnose)
    print("------------------")


report("Doe", "John", "cold")
report("John", "Doe", "headache")


# Folie 24

def report(name, first_name, diagnose):
    print("examination report")
    print("------------------")
    print("patient:", first_name, name)
    print("diagnose:", diagnose)
    print("------------------")


report(first_name="John", name="Doe", diagnose="cold")


# Folie 26

def my_sum(*numbers):
    sum = 0
    for x in numbers:
        sum += x
    return sum


print(my_sum())
print(my_sum(1))
print(my_sum(1, 2))
print(my_sum(1, 2, 3, 4))
print(my_sum(10, 3, 7, 20, 10, 15))


# Folie 27

def my_sum(first, *numbers):
    sum = first
    for x in numbers:
        sum += x
    return sum


# print(my_sum()) TypeError
print(my_sum(1))
print(my_sum(1, 2))
print(my_sum(1, 2, 3, 4))
print(my_sum(10, 3, 7, 20, 10, 15))


# Folie 28

def calc(x, y):
    def prod(x, y):
        return x * y

    return prod(x, y) * prod(x, y)


print(calc(2, 3))


# print(prod(2, 3))

# Folie 29

def calc(func, x, y):
    return func(x, y)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


print(calc(add, 2, 3))
print(calc(sub, 2, 3))


# Folie 30

def f():
    def g(n):
        print("-" * n)

    return g


f()(5)
f()(7)


# Folie 31

def calc(func, x, y):
    return func(x, y)


print(calc(lambda x, y: x + y, 2, 3))
print(calc(lambda x, y: x - y, 2, 3))


# Folie 36

def f(x):
    x = x + 1
    print('in f(x): x =', x)
    return x


x = 3
z = f(x)
print('in main: x =', x)
print('in main: z =', z)


# Folie 42

def e():
    print(v)


v = 1
e()


def e():
    print(v + x)


v = 1
x = 2
e()


def f(y):
    return x + y


x = 3
print(f(1))
x = 2
print(f(1))
x = 3
print(f(1))


# Folie 43

def e():
    v += 5


v = 1
e()


# Folie 44

def calc():
    global x
    x = x * 2


x = 10
calc()
print(x)
