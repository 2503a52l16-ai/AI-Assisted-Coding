# Program to print the multiplication table of 5

number = 5

print(f"Multiplication Table of {number}:")

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
