import unittest
from re import search
from encryption_helpers import *

'''
Unit Testing to test the helper encryption methods used to encrypt a given string

__author__ = "Mohit Kewalramani"
__version__ = 2.0
__published__ = 30 April 2017
'''


class MyTestCase(unittest.TestCase):

    def test_get_zero_index_user_message(self):
        self.assertRaises(TypeError, get_zero_index_user_message, None)
        self.letter_type_list_checker([], get_zero_index_user_message(''))
        self.letter_type_list_checker(['0', '1', '4'], get_zero_index_user_message('014'))
        self.letter_type_list_checker(['2', Letter(0, False)], get_zero_index_user_message('2a'))
        self.letter_type_list_checker([Letter(0, False), Letter(1, False), Letter(2, False)],
                                      get_zero_index_user_message('abc'))
        self.letter_type_list_checker([Letter(0, True), Letter(4, False), Letter(9, True)],
                                      get_zero_index_user_message('AeJ'))
        self.letter_type_list_checker(['/', '/', '/'], get_zero_index_user_message('///'))

    def test_is_uppercase_letter(self):
        self.assertRaises(TypeError, is_uppercase_letter, None)
        self.assertEquals(True, is_uppercase_letter('A'))
        self.assertEquals(False, is_uppercase_letter('f'))
        self.assertEquals(False, is_uppercase_letter('/'))
        self.assertEquals(False, is_uppercase_letter(' '))
        self.assertRaises(TypeError, is_uppercase_letter, 'jo')
        self.assertRaises(TypeError, is_uppercase_letter, 'ggh')

    def test_get_zero_index_encrypted_message(self):
        self.assertRaises(TypeError, get_zero_index_encrypted_message, None)
        self.letter_type_list_checker([Letter(4, False)], get_zero_index_encrypted_message([Letter(0, False)], 4))
        self.letter_type_list_checker([Letter(8, True), Letter(24, False)],
                                      get_zero_index_encrypted_message([Letter(2, True), Letter(4, False)], 6))
        self.letter_type_list_checker(['3', '1', '6', '4'],
                                      get_zero_index_encrypted_message(['3', '1', '6', '4'], 5))
        self.letter_type_list_checker(['/', '/'],
                                      get_zero_index_encrypted_message(['/', '/'], 4))
        self.letter_type_list_checker([Letter(21, True), '/', Letter(5, False), '%'],
                                      get_zero_index_encrypted_message([Letter(18, True), '/', Letter(2, False), '%'], 3))

    def test_construct_encrypted_string_values(self):
        self.assertRaises(TypeError, construct_encrypted_string_values, None)
        self.assertListEqual(['a'], construct_encrypted_string_values([Letter(0, False)]))
        self.assertListEqual(['D', '1'], construct_encrypted_string_values([Letter(3, True), '1']))
        self.assertListEqual(['3', '8', '#', '/', '*'],
                             construct_encrypted_string_values(['3', '8', '#', '/', '*']))

    def test_construct_decryption_key(self):
        self.assertEquals("0x3", search('\d(0x3)\d{4}', construct_decryption_key(1)).group(1))
        self.assertEquals("8y3", search('\d{3}(8y3)\d', construct_decryption_key(2)).group(1))
        self.assertEquals("2e7", search('\d(2e7)\d{4}', construct_decryption_key(3)).group(1))
        self.assertEquals("8z5", search('\d{4}(8z5)\d', construct_decryption_key(4)).group(1))
        self.assertEquals("3c8", search('(3c8)\d{4}', construct_decryption_key(5)).group(1))
        self.assertEquals("5q7", search('\d(5q7)\d{4}', construct_decryption_key(6)).group(1))
        self.assertEquals("8m4", search('\d{5}(8m4)', construct_decryption_key(7)).group(1))


    # Helper method to help compare the contents of a list of a complex (Letter) object
    # Comparisons were originally being done by the memory addresses of the list items
    def letter_type_list_checker(self, expected_list, constructed_list):
        self.assertEquals(len(expected_list), len(constructed_list))
        for i in range(0, len(expected_list)):
            if type(expected_list[i]) is not Letter and not str.isalpha(expected_list[i]):
                self.assertEquals(expected_list[i], constructed_list[i])
                continue
            self.assertEquals(expected_list[i].letter_value, constructed_list[i].letter_value)
            self.assertEquals(expected_list[i].uppercase, constructed_list[i].uppercase)


if __name__ == '__main__':
    unittest.main()
