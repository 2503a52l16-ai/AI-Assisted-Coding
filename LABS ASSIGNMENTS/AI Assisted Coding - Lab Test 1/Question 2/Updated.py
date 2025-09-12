# Program to print the multiplication table of a user-input number

# Ask the user to enter a number greater than 0
number = int(input("Enter a number greater than 0: "))

if number <= 0:
    print("Please enter a number greater than 0.")
else:
    print(f"\nMultiplication Table of {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")
