# Sample program demonstrating Python operators

# Arithmetic Operators
print("Arithmetic Operators:")
a = 10
b = 3
print(f"a + b = {a + b}")  # Addition
print(f"a - b = {a - b}")  # Subtraction
print(f"a * b = {a * b}")  # Multiplication
print(f"a / b = {a / b}")  # Division
print(f"a % b = {a % b}")  # Modulus
print(f"a ** b = {a ** b}")  # Exponentiation
print(f"a // b = {a // b}")  # Floor Division
print()

# Assignment Operators
print("Assignment Operators:")
x = 5
print(f"Initial x = {x}")
x += 2  # x = x + 2
print(f"x += 2: {x}")
x -= 1  # x = x - 1
print(f"x -= 1: {x}")
x *= 3  # x = x * 3
print(f"x *= 3: {x}")
x /= 2  # x = x / 2
print(f"x /= 2: {x}")
x %= 2  # x = x % 2
print(f"x %= 2: {x}")
x **= 2  # x = x ** 2
print(f"x **= 2: {x}")
x //= 2  # x = x // 2
print(f"x //= 2: {x}")
print()

# Relational (Comparison) Operators
print("Relational Operators:")
p = 10
q = 5
print(f"p == q: {p == q}")  # Equal to
print(f"p != q: {p != q}")  # Not equal to
print(f"p > q: {p > q}")    # Greater than
print(f"p < q: {p < q}")    # Less than
print(f"p >= q: {p >= q}")  # Greater than or equal to
print(f"p <= q: {p <= q}")  # Less than or equal to
print()

# Logical Operators
print("Logical Operators:")
x = True
y = False
print(f"x and y: {x and y}")  # Logical AND
print(f"x or y: {x or y}")    # Logical OR
print(f"not x: {not x}")      # Logical NOT
print()

# Identity Operators
print("Identity Operators:")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(f"list1 is list2: {list1 is list2}")      # False (different objects)
print(f"list1 is list3: {list1 is list3}")      # True (same object)
print(f"list1 is not list2: {list1 is not list2}")  # True
print()

# Additional: Membership Operators (commonly used with operators)
print("Membership Operators (bonus):")
my_list = [1, 2, 3, 4, 5]
print(f"3 in my_list: {3 in my_list}")
print(f"6 not in my_list: {6 not in my_list}")
