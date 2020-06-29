# Folie 8

file = open("data/testdata.txt", 'w')
text = input("Please enter text: ")
x = file.write(text)
print(x)
file.close()

# Folie 9

file = open("data/testdata.txt", 'r')
text = file.read()
file.close()
print(text)

# Folie 12

file = open("data/testdata.txt", "r+")
print(file.read(2))
print(file.read())
print("Text at the end:", file.read())
print("Current position:", file.tell())
file.seek(0)
print("Whole text:", file.read())
file.write("Two\n")
file.write("Three\n")
file.seek(0)
lines = file.readlines()
print("Textlines as list:", lines)
for i in lines:
    print("From list:", i)
file.seek(0)
for i in file:
    print("From iteration:", i)
file.close()
print("File closed ?", file.closed)

# Folie 14

try:
    file = open("/data/testdata.txt", "r")
    for i in file:
        print(i)
except:
    print("Can not open file!")

# Folie 16

with open("data/testdata.txt", "r") as file:
    for i in file:
        print(i)
print(file.closed)

# Folie 17

with open("data/students.txt", "r") as file:
    marks = {}
    for entry in file:
        list_entry = entry.split()
        marks[list_entry[0]] = list_entry[1]
print(marks)
print("All marks for course 123:")
for i in marks:
    print(i, ":", marks[i], "points")

# Folie 19

file = open("data/testdata.txt", 'w+', encoding="utf-8")
file.write("\u2600" + "\u2601" + "\u2602")
file.seek(0)
print(file.read(1))
print(file.read(2))

# Folie 21

import pickle

file = open("data/obj.dmp", "wb")
friends = [("Alice", 67623298), ("Bob", 66437373)]
pickle.dump(friends, file)
file.close()

import pickle

file = open("data/obj.dmp", "rb")
friends = pickle.load(file)
file.close()
for i in friends:
    print(i[0], i[1])

# Folie 27

s = "Test"
print(s.center(10))
print(s.center(10, "#"))
print(s.ljust(10, "#"))
print(s.rjust(10, "#"))
print(s.zfill(10))
s1 = s.center(10)
print(s1)
print(s1.strip() + "<")
print(s1.lstrip() + "<")
print(s1.rstrip() + "<")
print(s.strip('T'))

# Folie 29

s1 = "12345"
s2 = "\u00b2"
s3 = "3B"
s4 = "\u00bc"
print(s1)
print(s1.startswith("12"))
print(s1.startswith("122"))
print(s1.endswith("45"))
print(s1.endswith("445"))
print(s1.isdigit())
print(s1.isdecimal())
print(s1.isnumeric())
print(s1.isalnum())
print(s2)
print(s2.isdigit())
print(s2.isdecimal())
print(s2.isnumeric())
print(s2.isalnum())
print(s3)
print(s3.isdigit())
print(s3.isdecimal())
print(s3.isnumeric())
print(s3.isalnum())
print(s4)
print(s4.isdigit())
print(s4.isdecimal())
print(s4.isnumeric())
print(s4.isalnum())

s1 = "12345"
s2 = "Hello"
s3 = "1 and 2"
s4 = "  "
print("- isspace -")
print(s1.isspace())
print(s2.isspace())
print(s3.isspace())
print(s4.isspace())
print("- isalpha -")
print(s1.isalpha())
print(s2.isalpha())
print(s3.isalpha())
print(s4.isalpha())
print("- isdigit -")
print(s1.isdigit())
print(s2.isdigit())
print(s3.isdigit())
print(s4.isdigit())
print("- isalnum -")
print(s1.isalnum())
print(s2.isalnum())
print(s3.isalnum())
print(s4.isalnum())

# Folie 31

print("*-*".join(["Hello", "World", "Here"]))
s = "Hello World\n Here"
print(s.splitlines())
s = "Hello World"
print(s.split())
print(s.split("o"))
print(s.split("o", 1))
print(s.rsplit("o", 1))
print(s.partition("o"))
print(s.partition("u"))
print(s.rpartition("o"))

# Folie 33
print("{} had a little {}.".format("Mary", "dog"))
print("{1} had a little {0}.".format("dog", "Mary"))
print("{name} had a little {pet}.".format(pet="dog", name="Mary"))
print("{:20}".format("Welcome"))
print("{:^20}".format("Welcome"))
print("{:-^20}".format("Welcome"))
print("{:5d}".format(46))
print("{:5x}".format(46))
print("{:-<5x}".format(46))
print("First part costs {price:10.2f} Euro".format(price=123.4567))
