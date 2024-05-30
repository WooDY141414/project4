import unittest

from app import checkLoginAndPassword


class MyTestCase(unittest.TestCase):
    def test_login_invalid(self):
        result = checkLoginAndPassword('12312','true')
        self.assertEqual(result, 'Неверно')  # add assertion here

    def test_login_valid(self):
        result = checkLoginAndPassword('vladnaimkin1@mail.ru','16587')
        self.assertEqual(result, 'Верно')  # add assertion here

    def test_login_has_whitespace_login_is_valid(self):
        result = checkLoginAndPassword('  vladnaimkin1@mail.ru',' 16587')
        self.assertEqual(result, 'Верно')  # add assertion here

    def test_login_has_non_printable_characters_login_is_valid(self):
        result = checkLoginAndPassword('  vladnaimkin1@mail.ru\n\t\x01',' 16587')
        self.assertEqual(result, 'Верно')

if __name__ == '__main__':
    unittest.main()
