import unittest
import our_functions

class test_is_valid_date(unittest.TestCase):
    def test_correct_date_format(self):
        date_str = "2023-01-01"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, True)

    def test_incorrect_date_format(self):
        date_str = "03-12-2023"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)
    
    def test_empty_string(self):
        date_str = ""
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)

    def test_invalid_length(self):
        date_str = "2023-1-1"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)

    def test_invalid_year(self):
        date_str = "0999-01-01"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)

    def test_invalid_month(self):
        date_str = "2023-13-01"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)

    def test_invalid_day(self):
        date_str = "2023-01-32"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)

    def test_leap_year(self):
        date_str = "2024-02-29"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, True)

    def test_non_leap_year(self):
        date_str = "2023-02-29"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)

    def test_date_with_invalid_characters(self):
        date_str = "2023-01-0a"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)

    def test_date_with_special_characters(self):
        date_str = "2023-01-01!"
        res = our_functions.is_valid_date(date_str)
        self.assertEqual(res, False)

    def test_date_with_extra_spaces(self):
        date_str = " 2023-01-01 "
        res = our_functions.is_valid_date(date_str.strip())
        self.assertEqual(res, True)

class test_is_valid_username(unittest.TestCase):
    def test_username_more_than_min(self):
        username_str = "myname"
        min_username_chars = 5
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, True)

    def test_username_equal_min(self):
        username_str = "myname"
        min_username_chars = 6
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, True)
    
    def test_username_less_than_min(self):
        username_str = "name"
        min_username_chars = 5
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, False)
    
    def test_username_with_invalid_characters(self):
        username_str = "my@name"
        min_username_chars = 5
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, False)

    def test_username_starting_with_number(self):
        username_str = "1myname"
        min_username_chars = 5
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, False)

    def test_username_with_valid_characters(self):
        username_str = "my.name_123"
        min_username_chars = 5
        res = our_functions.is_valid_username(username_str, min_username_chars)
        self.assertEqual(res, True)

    def test_username_type_error(self):
        username_str = 123456
        min_username_chars = 5
        with self.assertRaises(TypeError):
            our_functions.is_valid_username(username_str, min_username_chars)

    def test_minlen_value_error(self):
        username_str = "myname"
        min_username_chars = 0
        with self.assertRaises(ValueError):
            our_functions.is_valid_username(username_str, min_username_chars)

if __name__ == "__main__":
    unittest.main()
