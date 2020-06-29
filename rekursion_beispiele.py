# Folie 7

def sum_iterative(n):
    sum = 0;
    for i in range(1, n + 1):
        sum += i
    return sum


def sum_recursive(n):
    if n == 1:
        return 1
    else:
        return sum_recursive(n - 1) + n


print(sum_iterative(10))
print(sum_iterative(50))
print(sum_recursive(10))
print(sum_recursive(50))


# Folie 9

def output_call_path(n):
    if n < 1:
        print("Numbers", end=" ")
    else:
        print(n, end=" ")
        output_call_path(n - 1)


def output_return_path(n):
    if n < 1:
        print("Numbers", end=" ")
    else:
        output_return_path(n - 1)
        print(n, end=" ")


output_call_path(5)
print()
output_return_path(5)


# Folie 10

def sum_recursive(n, indent):
    new_indent = indent + "   "
    print(new_indent + "sum called with argument", n)
    if n == 1:
        print(new_indent + "Returning 1")
        return 1
    else:
        help = sum_recursive(n - 1, new_indent)
        print(new_indent + "Returning ", n, "+", help, "(sum(" + str(n - 1) + "))")
        return help + n


print(sum_recursive(4, ""))


# Folie 11

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


# Folie 15

def fact_iter(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product


# Folie 17

def is_palindrome(text):
    if len(text) <= 1:
        return True
    else:
        return text[0] == text[-1] and is_palindrome(text[1:-1])


print(is_palindrome("racecar"))
print(is_palindrome("step on no pets"))
print(is_palindrome("Never odd or even"))


# Folie 18

def is_palindrome(text):
    def is_pal(new_text):
        if len(new_text) <= 1:
            return True
        else:
            return new_text[0] == new_text[-1] and is_pal(new_text[1:-1])

    help = text.replace(" ", "").lower()
    return is_pal(help)


print(is_palindrome("racecar"))
print(is_palindrome("step on no pets"))
print(is_palindrome("Never odd or even"))


# Folie 20

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
print(fibonacci(10))


# print(fibonacci(40))

# Folie 22

def fib_alternative(n, a, b):
    if n < 1:
        return a
    else:
        return fib_alternative(n - 1, b, a + b)


print(fib_alternative(10, 0, 1))
print(fib_alternative(50, 0, 1))


# Folie 23

def fib_alternative(n):
    def fib_helper(n, a, b):
        if n < 1:
            return a
        else:
            return fib_helper(n - 1, b, a + b)

    return fib_helper(n, 0, 1)


print(fib_alternative(10))
print(fib_alternative(50))


# Folie 24

def fib_short(n, a=0, b=1):
    return fib_short(n - 1, b, a + b) if n > 0 else a


print(fib_short(10))
print(fib_short(50))


# Folie 27

def solve_hanoi(n, origin, spare, to):
    if n > 0:
        solve_hanoi(n - 1, origin, to, spare)
        print("move from " + str(origin) + " to " + str(to))
        solve_hanoi(n - 1, spare, origin, to)


solve_hanoi(3, 1, 2, 3)

# Folie 29

import turtle

turtle.forward(200)
turtle.left(90)
turtle.forward(100)
turtle.exitonclick()

# Folie 30

import turtle


def spiral(n):
    while n >= 10:
        turtle.forward(n)
        turtle.right(90)
        n = n * 0.9


spiral(200)
turtle.exitonclick()

# Folie 31

import turtle


def spiral(n):
    if n >= 10:
        turtle.forward(n)
        turtle.right(90)
        spiral(n * 0.9)


spiral(200)
turtle.exitonclick()

# Folie 32

import turtle


def tree(n):
    if n >= 5:
        turtle.forward(n)
        turtle.left(30)
        tree(n * 0.5)
        turtle.right(60)
        tree(n * 0.5)
        turtle.left(30)
        turtle.backward(n)


turtle.speed(10)
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.left(90)
tree(150)
turtle.exitonclick()
