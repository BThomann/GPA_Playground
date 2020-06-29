# Folie 10

def copy(L1, L2):
    """
    Assumes L1 and L2 are lists
    Mutates L2 to be a copy of L1
    """
    while len(L2) > 0:  # remove all elements from L2
        L2.pop()  # remove last element from L2
    for e in L1:  # append L1's elements to initially empty L2
        L2.append(e)


a = [2, 3, 4]
b = [7, 8]
copy(a, b)
print(b)
copy(a, a)
print(a)


# Folie 22

def is_palindrome(x):
    """
    Assumes x is a list
    Returns True if the list is a palindrom; False otherwise """
    temp = x
    temp.reverse
    if temp == x:
        return True
    else:
        return False


def test(n):
    """
    Assumes n is an int > 0
    gets n inputs from user
    Prints 'Yes' if the sequence of inputs forms a palindrome; 'No' otherwise """
    for i in range(n):
        result = []
        elem = input('Enter element: ')
        result.append(elem)
    if is_palindrome(result):
        print('Yes')
    else:
        print('No')


test(5)

# Folie 29

a = int(input("a: "))
b = int(input("b: "))
c = a / b
print("Ratio a/b:", c)
print("Further input: ")

a = int(input("a: "))
b = int(input("b: "))
try:
    c = a / b
    print("Ratio a/b: ", c)
except ZeroDivisionError:
    print("Failure - ratio undefined")
print("Further input: ")

# Folie 31

try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print("a/b = ", a / b)
    print("a+b= ", a + b)
except ValueError:
    print("Could not convert to a number.")
except ZeroDivisionError:
    print("Can't divide by zero.")
except:
    print("Something went very wrong.")

# Folie 32

while True:
    val = input("Enter an integer: ")
    try:
        val = int(val)
        print("The square of", val, "is", val ** 2)
        break
    except ValueError:
        print(val, "is not an integer")


# Folie 33

def read_int():
    while True:
        val = input("Enter an integer: ")
        try:
            return int(val)
        except ValueError:
            print(val, "is not an integer")


print(read_int())


def read_val(val_type, request_msg, error_msg):
    while True:
        val = input(request_msg + " ")
        try:
            return val_type(val)
        except ValueError:
            print(val, error_msg)


print(read_val(int, "Enter an integer:", "is not an integer"))


# Folie 37

def get_ratios(v_1, v_2):
    """
    Assumes v_1 and v_2 are equal length lists of numbers
    Returns a list containing the meaningful values of v_1[i]/v_2[i]
    """
    ratios = []
    for index in range(len(v_1)):
        try:
            ratios.append(v_1[index] / v_2[index])
        except ZeroDivisionError:
            ratios.append(float("nan"))  # nan = Not a Number
        except:
            raise ValueError("get_ratios called with bad arguments")
    return ratios


try:
    print(get_ratios([1.0, 2.0, 7.0, 6.0], [1.0, 2.0, 0.0, 3.0]))
    print(get_ratios([], []))
    print(get_ratios([1.0, 2.0], [3.0]))
except ValueError as msg:
    print(msg)


# Folie 38

def factors(number):
    if number < 0:
        raise ValueError("Number must be >= 0!")
    if type(number) != int:
        raise TypeError("Number must be an int!")
    x = number
    factor_list = []
    factor = 2
    while x > 1:
        while x % factor == 0:
            factor_list.append(factor)
            x /= factor
        factor += 1
    return factor_list


try:
    print(factors(12))
    print(factors(25))
    print(factors(25.5))
except (ValueError, TypeError) as msg:
    print(msg)


# Folie 41

def avg(grades):
    assert len(grades) != 0, "no grades data"
    return sum(grades) / len(grades)


print(avg([80, 75, 90]))
print(avg([]))


# Folie 43

def factors(number):
    x = number
    factor_list = []
    factor = 2
    while x > 1:
        while x % factor == 0:
            factor_list.append(factor)
            x /= factor
        factor += 1
    return factor_list


print(factors(12))
print(factors(25))
print(factors(25.5))


# Folie 44

def factors(number):
    # precondition
    assert (type(number) == int) and (number > 0)
    x = number
    factor_list = []
    factor = 2
    while x > 1:
        while x % factor == 0:
            factor_list.append(factor)
            x /= factor
        factor += 1
    # postcondition
    product = 1
    for i in factor_list:
        product *= i
    assert product == number
    return factor_list


print(factors(12))
print(factors(25))
print(factors(25.5))
