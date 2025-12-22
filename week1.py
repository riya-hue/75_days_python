# Day 1: Hello World + Print formatting
print("Hello World")
name = input("Enter your name: ")
print(f"Hi {name}, welcome to Python!")

# Day 2: Variables, types, type casting
a = 10
b = "20"
print(int(b) + a)

# Day 3: Input/Output + basic operations
num = int(input("Enter a number: "))
print("Double of number:", num * 2)

# Day 4: Strings operations
s = "Python"
print("Reverse:", s[::-1])
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())

# Day 5: Lists operations
l = [1, 2, 3]
l.append(4)
l.remove(2)
print(l)
print("Length:", len(l))
