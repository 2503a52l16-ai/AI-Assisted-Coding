# refactored_calculator.py

def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y): return x / y if y != 0 else "Error: Division by zero"

operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}

def calculator():
    print("AI-Refactored Calculator")
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Enter operation (+, -, *, /): ")
        result = operations.get(op, lambda x, y: "Invalid operation")(a, b)
        print("Result:", result)
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    calculator()
