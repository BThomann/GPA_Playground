# Folie 11

from stack import Stack


def reverse_file(file_name):
    rev_stack = Stack()
    with open(file_name) as original:
        for line in original:
            rev_stack.push(line.rstrip('\n'))

    with open(file_name, 'w') as output:
        while not rev_stack.is_empty():
            output.write(rev_stack.pop() + '\n')


reverse_file("data.txt")

# Folie 12

from stack import Stack


def is_matched(expr):
    lefty = "({["
    righty = ")}]"
    br_stack = Stack()
    for c in expr:
        if c in lefty:
            br_stack.push(c)
        elif c in righty:
            if br_stack.is_empty():
                return False
            if righty.index(c) != lefty.index(br_stack.pop()):
                return False
    return br_stack.is_empty()


print(is_matched("()"))
print(is_matched("())"))
print(is_matched("[(5+x)-(y+z)]"))
print(is_matched("[(5+x)-(y+z)"))
print(is_matched("[(5+x)-(y+z))]"))

# Folie 15

import math
from stack import Stack


def evaluate(expression):
    ops = Stack()
    values = Stack()

    token_list = expression.split()
    for token in token_list:
        if token in {"+", "-", "*", "sqrt"}:
            ops.push(token)
        elif token == ')':
            op = ops.pop()
            value = values.pop()
            if op == "+":
                value = values.pop() + value
            elif op == "-":
                value = values.pop() - value
            elif op == "*":
                value = values.pop() * value
            elif op == "sqrt":
                value = math.sqrt(value)
            values.push(value)
        elif token != '(':
            values.push(float(token))
    return values.pop()


print(evaluate("( 1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )"))
print(evaluate("( 1 + sqrt ( 5.0 ) ) * 0.5 )"))

# Folie 36

from collections import deque

data = deque()
data.append(4)
print(data)
data.append(6)
data.appendleft(8)
print(data)
print(data.pop())
print(data)
print(data.popleft())
print(data)
data.appendleft(7)
print(data[0], data[-1])
data.append(5)
print(data)
data.rotate(1)
print(data)

# Folie 37

from collections import deque

data = deque([2, 3, 5], 4)
data.append(8)
print(data)
data.append(9)
print(data)
data.appendleft(11)
print(data)
print(data.pop())
print(data)
data.appendleft(15)
print(data)
data.remove(3)
print(data)
data.appendleft(15)
print(data)
print(data.count(15))

# Folie 41

import sys

data = []
for k in range(20):
    a = len(data)
    b = sys.getsizeof(data)
    print("Length: {0:3d}  -> Size in Bytes: {1:4d}".format(a, b))
    data.append(None)
