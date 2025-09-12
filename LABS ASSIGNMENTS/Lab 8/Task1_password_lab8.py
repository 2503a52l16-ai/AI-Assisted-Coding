import re
import unittest

def is_strong_password(password: str) -> bool:
    if len(password) < 8:
        return False
    if " " in password:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

class TestPasswordStrength(unittest.TestCase):
    def test_valid_password(self):
        self.assertTrue(is_strong_password("Abcd@123"))  
    
    def test_missing_uppercase(self):
        self.assertFalse(is_strong_password("abcd@123"))  
    
    def test_missing_digit(self):
        self.assertFalse(is_strong_password("Abcd@xyz"))  
    
    def test_missing_special_char(self):
        self.assertFalse(is_strong_password("Abcd1234"))  
    
    def test_contains_space(self):
        self.assertFalse(is_strong_password("Abcd@ 123"))  
    
    def test_too_short(self):
        self.assertFalse(is_strong_password("A@1a"))  

if __name__ == "__main__":
    unittest.main()
