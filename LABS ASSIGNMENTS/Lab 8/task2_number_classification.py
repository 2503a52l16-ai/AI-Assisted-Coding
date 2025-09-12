import unittest

# -----------------------------
# Task 2: Number Classification with Loops
# -----------------------------
def classify_number(n):
    # Handle invalid input
    if not isinstance(n, int):
        return "Invalid Input"
    
    # Using loop for classification logic
    for _ in [0]:  # dummy loop (executes once)
        if n > 0:
            return "Positive"
        elif n < 0:
            return "Negative"
        else:
            return "Zero"


class TestNumberClassification(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(classify_number(10), "Positive")
    
    def test_negative_number(self):
        self.assertEqual(classify_number(-5), "Negative")
    
    def test_zero(self):
        self.assertEqual(classify_number(0), "Zero")

    def test_boundary_positive(self):
        self.assertEqual(classify_number(1), "Positive")
    
    def test_boundary_negative(self):
        self.assertEqual(classify_number(-1), "Negative")
    
    def test_invalid_string(self):
        self.assertEqual(classify_number("hello"), "Invalid Input")
    
    def test_invalid_none(self):
        self.assertEqual(classify_number(None), "Invalid Input")


# -----------------------------
# Run all tests with confirmation message
# -----------------------------
if __name__ == "__main__":
    result = unittest.main(exit=False)
    if result.result.wasSuccessful():
        print("\n✅ All Task 2 test cases passed successfully!")
    else:
        print("\n❌ Some Task 2 test cases failed. Please check again.")
