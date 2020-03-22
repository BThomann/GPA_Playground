# Folie 5

num = int(input("Enter a number: "))
if num > 0:
    print("num is positive")
print("Finished comparing num to 0")

# Folie 7

num = int(input("Pick a number: "))
if num > 0:
    print("Your number is positive")
if num < 0:
    print("Your number is negative")
if num == 0:
    print("Your number is zero")
print("Finished!")

# Folie 8

x = int(input("Enter a number for x: "))
y = int(input("Enter a number for y: "))
if x == y:
    print("x and y are equal")
    if y != 0:
        print("x/y is", x / y)
print("Finished!")

# Folie 10

a = int(input("Enter a number for a: "))
b = int(input("Enter a number for b: "))
c = int(input("Enter a number for c: "))
maximum = a
if b > maximum:
    maximum = b
if c > maximum:
    maximum = c
print("Maximum is:", maximum)

# Folie 12

user_input = input("Input: ")
if user_input:
    print("Your input:", user_input)

# Folie 17

number_a = int(input("Enter first number: "))
number_b = int(input("Enter second number: "))
if (number_a < 0) and (number_b < 0):
    print("Both numbers are negative!")
print("Finished!")

# Folie 18

number_a = int(input("Enter first number: "))
number_b = int(input("Enter second number: "))
if (number_a < 0) or (number_b < 0):
    print("At least one number is negative!")
print("Finished!")

# Folie 23

number = int(input("Enter a number for x: "))
if number % 2 == 0:
    print("number is even")
else:
    print("number is odd")
print("Finished!")

# Folie 24

age = int(input("Your age: "))
if (age <= 12) or (age >= 65):
    admission_fee = 10
else:
    admission_fee = 20
print("Your admission fee:", admission_fee)

# Folie 25

a = int(input("Number a: "))
b = int(input("Number b: "))
if a > b:
    maximum = a
else:  # !(a > b), i.e. a <= b
    maximum = b
print("Maximum of a and b is", maximum)

# Folie 26

a = int(input("Number a: "))
b = int(input("Number b: "))
c = int(input("Number c: "))
if a > b:  # a > b
    if a > c:  # a > b and a > c
        maximum = a
    else:  # a > b and a <= c
        maximum = c
else:  # a <= b
    if b > c:  # a <= b and b > c
        maximum = b
    else:  # a <= b and b <= c
        maximum = c
print("Maximum:", maximum)

# Folie 28

a = int(input("Number a: "))
b = int(input("Number b: "))
maximum = a if a > b else b
print("Maximum of a and b is", maximum)

# Folie 30

points = int(input("Please enter points (0 - 100): "))
if points >= 91:
    text = "excellent"
elif points >= 81:
    text = "good"
elif points >= 72:
    text = "satisfactory"
elif points >= 65:
    text = "sufficient"
else:
    text = "insufficient"
print(text)

# Folie 31

grade = int(input("Please enter number: "))
text = "no grade"
if grade == 1:
    text = "with distinction"
elif (grade == 2) or (grade == 3) or (grade == 4):
    text = "passed"
elif grade == 5:
    text = "not passed"
print(text)

# Folie 33

year = int(input("Year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leapyear")
        else:
            print(year, "is not a leapyear")
    else:
        print(year, "is a leapyear")
else:
    print(year, "is not a leapyear")

# Folie 34

year = int(input("Year: "))
if year % 400 == 0:
    print(year, "is a leapyear")
elif year % 100 == 0:
    print(year, "is not a leapyear")
elif year % 4 == 0:
    print(year, "is a leapyear")
else:
    print(year, "is not a leapyear")

# Folie 35

year = int(input("Year: "))
if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
    print(year, "is a leapyear")
else:
    print(year, "is not a leapyear")
