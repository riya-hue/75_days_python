# Day 16: File handling
with open("sample.txt", "w") as f:
    f.write("Hello Python\nLine2")
with open("sample.txt", "r") as f:
    print(f.read())

# Day 17: Exception handling
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Execution finished")

# Day 18: Modules & import
import math
print("Square root of 16:", math.sqrt(16))

# Day 19: Classes & Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p = Person("Riya", 22)
print(p.name, p.age)

# Day 20: Methods & self
class Calc:
    def add(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
c = Calc()
print("Add:", c.add(5, 3))
print("Sub:", c.sub(5, 3))
