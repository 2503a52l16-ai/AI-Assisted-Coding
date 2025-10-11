# refactored_scientific.py

import math

def compute_value(x):
    """Compute sin(x) + log(x) for a given x."""
    return math.sin(x) + math.log(x)

def main():
    """Process a list of values and display the computed results."""
    data = [1, 2, 3, 4, 5]
    results = [compute_value(value) for value in data]
    print("Computed results:", results)

if __name__ == "__main__":
    main()
# refactored_student_db.py