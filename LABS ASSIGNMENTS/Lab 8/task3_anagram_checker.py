import re
import unittest

# -----------------------------
# Task 3: Anagram Checker
# -----------------------------
def is_anagram(str1, str2):
    # Remove spaces, punctuation, and make lowercase
    clean_str1 = re.sub(r"[^a-zA-Z]", "", str1).lower()
    clean_str2 = re.sub(r"[^a-zA-Z]", "", str2).lower()
    
    # Compare sorted characters
    return sorted(clean_str1) == sorted(clean_str2)


class TestAnagramChecker(unittest.TestCase):
    def test_valid_anagram(self):
        self.assertTrue(is_anagram("listen", "silent"))

    def test_not_anagram(self):
        self.assertFalse(is_anagram("hello", "world"))

    def test_anagram_with_spaces(self):
        self.assertTrue(is_anagram("Dormitory", "Dirty Room"))

    def test_anagram_with_punctuation(self):
        self.assertTrue(is_anagram("A gentleman!!", "Elegant man"))

    def test_empty_strings(self):
        self.assertTrue(is_anagram("", ""))

    def test_identical_words(self):
        self.assertTrue(is_anagram("Python", "Python"))


# -----------------------------
# Run all tests with confirmation message
# -----------------------------
if __name__ == "__main__":
    result = unittest.main(exit=False)
    if result.result.wasSuccessful():
        print("\n✅ All Task 3 test cases passed successfully!")
    else:
        print("\n❌ Some Task 3 test cases failed. Please check again.")
