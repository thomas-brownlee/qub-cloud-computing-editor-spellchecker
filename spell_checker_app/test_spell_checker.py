import unittest
import spell_checker 

class TestCalculator(unittest.TestCase):

  def test_when_spelling_is_good(self):
        '''Test case function for addition'''
        count, list_of_string = spell_checker.spell_check("string")
        self.assertEqual(count, 0)
        self.assertEqual(list_of_string, [])

  def test_when_int_is_passed(self):
        '''Test case function for addition'''
        count, list_of_string= spell_checker.spell_check(0)
        self.assertEqual(count, -1)
        self.assertEqual(list_of_string, [])

  def test_when_string_is_empty(self):
        '''Test case function for addition'''
        count, list_of_string = spell_checker.spell_check("")
        self.assertEqual(count, -2)
        self.assertEqual(list_of_string, [])

  def test_when_string_contain_spelling_mistake(self):
        '''Test case function for addition'''
        count, list_of_string = spell_checker.spell_check("hlep")
        self.assertEqual(count, 1)
        self.assertEqual(list_of_string, ["spelling mistake hlep on line 0 did you mean help"])

if __name__ == "__main__":
    unittest.main()