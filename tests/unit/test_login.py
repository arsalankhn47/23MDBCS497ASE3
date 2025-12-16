import unittest
from src.login import login

class TestLogin(unittest.TestCase):

    def test_valid_login(self):
        self.assertEqual(login("admin", "1234"), "Login Successful")

    def test_invalid_password(self):
        self.assertEqual(login("admin", "1111"), "Invalid credentials")

    def test_empty_username(self):
        self.assertEqual(login("", "1234"), "Fields cannot be empty")

    def test_empty_password(self):
        self.assertEqual(login("admin", ""), "Fields cannot be empty")

    def test_both_empty(self):
        self.assertEqual(login("", ""), "Fields cannot be empty")

    def test_wrong_username(self):
        self.assertEqual(login("user", "1234"), "Invalid credentials")

if __name__ == "__main__":
    unittest.main()

