# Folie 3

num = int(input("How many times should I print the character * ? "))
if num == 1:
    print("*")
elif num == 2:
    print("**")
elif num == 3:
    print("***")

# Folie 6

num = 1
while num < 10:
    print(num, end=" ")
    num = num + 1

# Folie 7

num = int(input("How many times should I print the character * ? "))
while num > 0:
    print("*", end="")
    num = num - 1

# Folie 9

secret = 42
guess = int(input("Guess a number in the range 1 to 100: "))
tries = 1
while guess != secret:
    print("You tried to guess", tries, "times")
    guess = int(input("Guess again: "))
    tries += 1
print("You got it! The answer is:", secret)

# Folie 11

num = int(input("How many * ? "))
for i in range(num):
    print("*", end="")

# Folie 16

word = input("Word: ")
for i in range(len(word)):
    print(word[i], end=" ")

# Folie 17

word = input("Word: ")
for c in word:
    print(c, end=" ")

# Folie 20

num = int(input("How many numbers? "))
for i in range(1, num + 1):
    for j in range(1, num + 1):
        print(i * j, end="\t")
    print()

# Folie 21

num = int(input("Number: "))
for i in range(num):
    for j in range(num):
        print("*", end=" ")
    print()

num = int(input("Number: "))
for i in range(num):
    print("* " * num)

# Folie 22

num = int(input("Number: "))
for i in range(num):
    for j in range(num - i):
        print("*", end=" ")
    print()

num = int(input("Number: "))
for i in range(num):
    print("* " * (num - i))

# Folie 23

number = int(input("Number to check: "))
for i in range(2, number):
    if number % i == 0:
        print(number, "==", i, "*", number // i)
        break
if i == number - 1:
    print(number, "is a prime number")

# Folie 24

print("Please enter a number between 1 and 10: ")
while True:
    number = int(input("Number: "))
    if 1 < number < 10:
        break
    else:
        print("Number should be between 1 and 10")
print("Number entered:", number)

# Folie 25

word = input("Word: ")
counter = 0
for c in word:
    if c in "aeiouAEIOU":
        continue
    counter = counter + 1
print("Number of consonants found:", counter)

# Folie 26

print("Please enter a number between 1 and 10: ")
number = int(input("Number: "))
while not (1 < number < 10):
    print("Number should be between 1 and 10")
    number = int(input("Number: "))
print("Number entered:", number)

word = input("Word: ")
counter = 0
for c in word:
    if c not in "aeiouAEIOU":
        counter = counter + 1
print("Number of consonants found:", counter)

# Folie 27

number = int(input("Number to check: "))
for i in range(2, number):
    if number % i == 0:
        print(number, "==", i, "*", number // i)
        break
else:
    print(number, "is a prime number")

# Folie 32

num = int(input('Enter an integer: '))
ans = 0
while ans ** 3 < abs(num):
    ans = ans + 1
if ans ** 3 != abs(num):
    print(num, 'is not a perfect cube')
else:
    if num < 0:
        ans = -ans
    print('Cube root of', num, 'is', ans)

# Folie 34

num = int(input('Enter an integer: '))
for ans in range(0, abs(num) + 1):
    if ans ** 3 >= abs(num):
        break
if ans ** 3 != abs(num):
    print(num, 'is not a perfect cube')
else:
    if num < 0:
        ans = -ans
    print('Cube root of', num, 'is', ans)

# Folie 35

num = float(input('Enter number: '))
epsilon = 0.01
step = epsilon ** 2
num_guesses = 0
ans = 0.0
while abs(ans ** 2 - num) >= epsilon and ans * ans <= num:
    ans += step
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(ans ** 2 - num) >= epsilon:
    print('Failed on square root of', num)
else:
    print(ans, 'is close to square root of', num)

# Folie 40

num = float(input('Enter number: '))
epsilon = 0.001
num_guesses = 0
low = 0.0
high = max(1.0, num)
ans = (high + low) / 2.0
while abs(ans ** 2 - num) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    num_guesses += 1
    if ans ** 2 < num:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print('num_guesses =', num_guesses)
print(ans, 'is close to square root of', num)

# Folie 43

num = float(input('Enter number: '))
epsilon = 0.01
num_guesses = 0
guess = num / 2.0
while abs(guess * guess - num) >= epsilon:
    guess = guess - (((guess ** 2) - num) / (2 * guess))
    num_guesses += 1
print('num_guesses =', num_guesses)
print('Square root of', num, 'is about', guess)
