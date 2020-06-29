# Folie 13

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


position = Coordinate(2, 3)
origin = Coordinate(0, 0)
print(position.x, position.y)
print(origin.x, origin.y)


# Folie 15

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5


my_position = Coordinate(2, 3)
target_position = Coordinate(5, 7)
print(my_position.distance(target_position))
print(target_position.distance(my_position))


# Folie 18

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"


my_position = Coordinate(2, 3)
print(my_position)


# Folie 21

class Coordinate:
    counter = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Coordinate.counter += 1

    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"


my_position = Coordinate(2, 3)
print("Number of instances: " + str(Coordinate.counter))
coord = []
for i in range(5):
    coord.append(Coordinate(i, i))
print("Number of instances: " + str(Coordinate.counter))
for i in coord:
    print(i)


# Folie 23

class Coordinate:
    counter = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Coordinate.counter += 1


a = Coordinate(4, 5)
b = Coordinate(2, 3)
print("a:", a.x, a.y)
print("b:", b.x, b.y)
print(a.counter, b.counter, Coordinate.counter)
a.x = 10
Coordinate.counter = 10
print("a:", a.x, a.y)
print("b:", b.x, b.y)
print(a.counter, b.counter, Coordinate.counter)


# Folie 25

class Coordinate:
    _counter = 0

    def __init__(self, x, y):
        self._x = x
        self._y = y
        Coordinate._counter += 1


a = Coordinate(4, 5)
print("a:", a._x, a._y)
print(a._counter, Coordinate._counter)
a._x = 10
Coordinate._counter = 10
print("a:", a._x, a._y)
print(a._counter, Coordinate._counter)


class Coordinate:
    __counter = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        Coordinate.__counter += 1


a = Coordinate(4, 5)
# print("a:", a.__x, a.__y)
print("a:", a._Coordinate__x, a._Coordinate__y)


# Folie 27

class Coordinate:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_X(self):
        return self.__x

    def get_Y(self):
        return self.__y

    def set_X(self, value):
        self.__x = abs(value)

    x = property(get_X, set_X)
    y = property(get_Y)


a = Coordinate(4, 5)
print("a:", a.x, a.y)
a.x = -10
print("a:", a.x, a.y)
a.y = 10


# Folie 30

class Coordinate:
    def __init__(self, xval, yval):
        self.xval = xval
        self.yval = yval


a = Coordinate(4, 5)
b = Coordinate(2, 3)
print("a:", a.xval, a.yval)
print("Attributes of a", a.__dict__)
print("b:", b.xval, b.yval)
a.xvals = 7
print("a:", a.xval, a.yval)
print("b:", b.xval, b.yval)
print(a.xvals)
print("Attributes of a", a.__dict__)
print("Attributes of b", b.__dict__)


# Folie 31

class Coordinate:
    __slots__ = ["xval", "yval"]

    def __init__(self, xval, yval):
        self.xval = xval
        self.yval = yval


a = Coordinate(4, 5)
b = Coordinate(2, 3)
print("a:", a.xval, a.yval)
print("b:", b.xval, b.yval)
a.xvals = 7
print("a:", a.xval, a.yval)
print("b:", b.xval, b.yval)


# Folie 37

class Length:
    __metric = {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000, "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.344}

    def __init__(self, value, unit="m"):
        self.value = value
        self.unit = unit

    def convert_to_meters(self):
        return self.value * Length.__metric[self.unit]

    def __add__(self, other):
        result = self.convert_to_meters() + other.convert_to_meters()
        return Length(result / Length.__metric[self.unit], self.unit)

    def __str__(self):
        return str(self.convert_to_meters())

    def __repr__(self):
        return str((self.value, self.unit))


x = Length(1)
print("x in meters:", x)
y = Length(1, "yd") + x
print("y in meters:", y)
print("Internal representation of y:", repr(y))


# Folie 41

class Statistics:
    def mean_value(s):
        if s:
            return float(sum(s)) / len(s)

    def range_value(s):
        if s:
            return max(s) - min(s)

    def median_value(s):
        if s:
            s1 = sorted(s)
            if len(s) % 2 == 0:
                return (s1[len(s) // 2 - 1] + s1[len(s) // 2]) / 2.0
            else:
                return s1[(len(s) - 1) // 2]

    mean_value = staticmethod(mean_value)
    range_value = staticmethod(range_value)
    median_value = staticmethod(median_value)


num = [3, 5, 2, 6, 4, 1, 7]
print(Statistics.mean_value(num))
print(Statistics.range_value(num))
print(Statistics.median_value(num))


# Folie 48

class Person:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def __str__(self):
        return self.name + ", " + self.date_of_birth


class Employee():
    def __init__(self, name, date_of_birth, personnel_number):
        self.name = name
        self.date_of_birth = date_of_birth
        self.personnel_number = personnel_number

    def __str__(self):
        return self.name + ", " + self.date_of_birth + ", " + str(self.personnel_number)


p1 = Person("Homer Simpson", "12.05.1956")
e1 = Employee("Bruce Wayne", "19.02.1963", 123)
print(p1)
print(e1)


# Folie 49

class Person:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def __str__(self):
        return self.name + ", " + self.date_of_birth


class Employee(Person):
    def __init__(self, name, date_of_birth, personnel_number):
        super().__init__(name, date_of_birth)
        self.personnel_number = personnel_number


p1 = Person("Homer Simpson", "12.05.1956")
e1 = Employee("Bruce Wayne", "19.02.1963", 123)
print(p1)
print(e1)


# Folie 50

class Person:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def __str__(self):
        return self.name + ", " + self.date_of_birth


class Employee(Person):
    def __init__(self, name, date_of_birth, personnel_number):
        super().__init__(name, date_of_birth)
        self.personnel_number = personnel_number

    def __str__(self):
        return super().__str__() + ", " + str(self.personnel_number)


p1 = Person("Homer Simpson", "12.05.1956")
e1 = Employee("Bruce Wayne", "19.02.1963", 123)
print(p1)
print(e1)


# Folie 51

class Person:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def __str__(self):
        return self.name + ", " + self.date_of_birth


class Employee(Person):
    def __init__(self, name, date_of_birth, personnel_number):
        super().__init__(name, date_of_birth)
        self.personnel_number = personnel_number

    def get_id(self):
        if self.personnel_number != 7:
            return self.personnel_number
        else:
            return 42


p1 = Person("Homer Simpson", "12.05.1956")
e1 = Employee("Bruce Wayne", "19.02.1963", 123)
e2 = Employee("James Bond", "11.11.1960", 7)
print(p1)
print(e1)
print(e2)
print(e1.get_id())
print(e2.get_id())
# print(p1.get_id())    Nicht möglich
