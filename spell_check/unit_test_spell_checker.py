"""
This module provides unit testing for the spell_check module
"""

import unittest

from src import spell_checker


class TestSpellChecker(unittest.TestCase):
    """Testing class for the unit tests"""

    def test_when_spelling_is_good(self):
        """Test case: When string param contains a valid string"""
        count, list_of_string = spell_checker.spell_check("string")
        self.assertEqual(count, 0)
        self.assertEqual(list_of_string, [])

    def test_when_int_is_passed(self):
        """Test case: When int is passed as param"""
        count, list_of_string = spell_checker.spell_check(0)
        self.assertEqual(count, -1)
        self.assertEqual(list_of_string, [])

    def test_when_string_is_empty(self):
        """Test case: When param is empty string"""
        count, list_of_string = spell_checker.spell_check("")
        self.assertEqual(count, -2)
        self.assertEqual(list_of_string, [])

    def test_when_string_contain_spelling_mistake(self):
        """Test case: When param contains a spelling mistake"""
        count, list_of_string = spell_checker.spell_check("hlep")
        self.assertEqual(count, 1)
        self.assertEqual(
            list_of_string, ["spelling mistake hlep on line 0 did you mean help"]
        )


if __name__ == "__main__":
    unittest.main()
