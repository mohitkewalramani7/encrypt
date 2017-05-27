import unittest
from decryption_helpers import *

'''
Unit Testing to test the helper decryption methods used to decrypt a given string

__author__ = "Mohit Kewalramani"
__version__ = 2.0
__published__ = 30 April 2017
'''


class MyTestCase(unittest.TestCase):

    def test_return_decoded_integer(self):
        self.assertRaises(TypeError, return_decoded_integer, None)
        self.assertEquals(0, return_decoded_integer(""))
        self.assertEquals(1, return_decoded_integer("320x3242"))
        self.assertEquals(2, return_decoded_integer("8y3232344"))
        self.assertEquals(3, return_decoded_integer("2e72e7"))
        self.assertEquals(4, return_decoded_integer("328z5324"))
        self.assertEquals(5, return_decoded_integer("24423c83242"))
        self.assertEquals(6, return_decoded_integer("5q7314242"))
        self.assertEquals(7, return_decoded_integer("324258m4"))

    def test_get_zero_indexed_encrypted_values(self):
        self.assertRaises(TypeError, get_zero_indexed_encrypted_values, None)
        self.assertEquals([0], get_zero_indexed_encrypted_values("a"))
        self.assertEquals([11, 7], get_zero_indexed_encrypted_values("lh"))
        self.assertEquals(["4"], get_zero_indexed_encrypted_values("4"))
        self.assertEquals([3, "9"], get_zero_indexed_encrypted_values("d9"))
        self.assertEquals([4, 6, "9", 25, "/"], get_zero_indexed_encrypted_values("eg9z/"))

    def test_is_uppercase_letter(self):
        self.assertRaises(TypeError, is_uppercase_letter, None)
        self.assertEquals(True, is_uppercase_letter('A'))
        self.assertEquals(False, is_uppercase_letter('f'))
        self.assertEquals(False, is_uppercase_letter('/'))
        self.assertEquals(False, is_uppercase_letter(' '))
        self.assertRaises(TypeError, is_uppercase_letter, 'jo')
        self.assertRaises(TypeError, is_uppercase_letter, 'ggh')

    def test_get_zero_indexed_decrypted_values(self):
        self.assertRaises(TypeError, get_zero_indexed_decrypted_values, None, 4)
        self.assertEquals([], get_zero_indexed_decrypted_values([], 5))
        self.assertEquals([23, 7, 2], get_zero_indexed_decrypted_values([0, 4, 5], 3))
        self.assertEquals([14, 'f'], get_zero_indexed_decrypted_values([16, 'f'], 2))
        self.assertEquals([15, 'f', ':'], get_zero_indexed_decrypted_values([16, 'f', ':'], 1))

    def test_get_decrypted_string_message(self):
        self.assertRaises(TypeError, get_decrypted_string_message, None, None)
        self.assertEquals([], get_decrypted_string_message([], ""))
        self.assertEquals(['a', 'b'], get_decrypted_string_message([0, 1], "ab"))
        self.assertEquals(['a', 'b', 'c', '/'], get_decrypted_string_message([0, 1, 2, '/'], "abc/"))
        self.assertEquals(['3', '4', 'a', '/', 'b'], get_decrypted_string_message(['3', '4', 0, '/', 1], "34a/b"))


if __name__ == '__main__':
    unittest.main()
