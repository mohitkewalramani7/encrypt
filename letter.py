
'''
A class that defines a Letter type used throughout the script.
The type consists of the letter value, along with whether it's uppercase or not

__author__ = "Mohit Kewalramani"
__version__ = 2.0
__published__ = 30 April 2017
'''

class Letter(object):

    def __init__(self, letter_value, uppercase):
        self.letter_value = letter_value
        self.uppercase = uppercase
