"""
This module provides unit testing for the spell_check module
"""

import unittest

from spell_check.src import spell_checker


class TestSpellChecker(unittest.TestCase):
    """Testing class for the unit tests"""

    def test_when_spelling_is_good(self):
        """Test case: When string param contains a valid string"""
        responce = spell_checker.spell_check("string")
        self.assertEqual(responce["answer"], 0)
        self.assertEqual(
            responce["string"], "There are no misspelled words in this text."
        )
        self.assertEqual(responce["error"], False)

    def test_when_int_is_passed(self):
        """Test case: When int is passed as param"""
        responce = spell_checker.spell_check(0)
        self.assertEqual(responce["error"], True)
        self.assertEqual(responce["string"], "Invalid Type - Text is not a string")
        self.assertEqual(responce["answer"], 0)

    def test_when_string_is_empty(self):
        """Test case: When param is empty string"""
        responce = spell_checker.spell_check("")
        self.assertEqual(responce["error"], False)
        self.assertEqual(responce["string"], "Empty parameters - Text is not a string")
        self.assertEqual(responce["answer"], 1)

    def test_when_string_contain_spelling_mistake(self):
        """Test case: When param contains a spelling mistake"""
        responce = spell_checker.spell_check("hlep")
        self.assertEqual(responce["error"], False)
        self.assertEqual(
            responce["string"], "spelling mistake hlep on line 0 did you mean help"
        )
        self.assertEqual(responce["answer"], 1)


if __name__ == "__main__":
    unittest.main()
