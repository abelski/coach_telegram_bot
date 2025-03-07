import unittest
from services.user_service import is_whitelisted_user, is_black_listed_user


class TestUserService(unittest.TestCase):
    def test_is_whitelisted_user_returns_true_for_whitelisted_user(self):
        self.assertTrue(is_whitelisted_user("473372343"))

    def test_is_whitelisted_user_returns_false_for_non_whitelisted_user(self):
        self.assertFalse(is_whitelisted_user("-1"))

    def test_is_black_listed_user_returns_true_for_non_whitelisted_user(self):
        self.assertTrue(is_black_listed_user("-1"))

    def test_is_black_listed_user_returns_false_for_whitelisted_user(self):
        self.assertFalse(is_black_listed_user("473372343"))


if __name__ == '__main__':
    unittest.main()
