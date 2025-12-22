# Day 6: Tuples
t = (1, 2, 3)
print(t[0], t[1])
# Tuple is immutable
# t[0] = 10 -> Error

# Day 7: Dictionaries
d = {"a": 1, "b": 2}
d["c"] = 3
print(d)
print(d.get("a"))
d.pop("b")
print(d)

# Day 8: Sets
s = {1, 2, 2, 3}
s.add(4)
s.remove(1)
print(s)

# Day 9: Conditional statements
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is 5")
else:
    print("x is less than 5")

# Day 10: Loops: for
for i in range(5):
    print(i)
