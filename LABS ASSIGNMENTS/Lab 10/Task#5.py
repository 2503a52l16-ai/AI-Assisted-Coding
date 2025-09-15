# Find squares of numbers using list comprehension
squares = [n ** 2 for n in range(1, 1_000_000)]
print("Total squares generated:", len(squares))
print("First 10 squares are:", squares[:10])  # Print first 10 squares for verification