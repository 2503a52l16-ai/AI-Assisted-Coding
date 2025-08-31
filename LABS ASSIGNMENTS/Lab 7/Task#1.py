def factr(n):
    if n < 0:
        raise ValueError("Negative input not allowed")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factr(n - 1)  # FIXED: Correct recursion!
print(factr(5))
# This function calculates the factorial of a number n