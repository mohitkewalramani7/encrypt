from click._compat import raw_input
from letter import Letter
from random import randint

'''
Encryption methods to complete the encryption process of a given string

__author__ = "Mohit Kewalramani"
__version__ = 2.0
__published__ = 30 April 2017
'''


def perform_encryption():
    '''
        Computes the encryption of the given string by the user, and provides back the encrypted
        string with a decryption key

        Returns:
            None
    '''

    user_message = raw_input("Please Enter Your Message for Encryption: \n\n")
    user_message = user_message.strip("\n")
    zero_index_user_message = get_zero_index_user_message(user_message)
    random_integer = randint(1, 7)
    zero_index_encrypted_message = get_zero_index_encrypted_message(zero_index_user_message, random_integer)
    encrypted_message_string_values = construct_encrypted_string_values(zero_index_encrypted_message)
    print("\n\n\n")
    print("Your Encrypted Message is: " + "".join(map(str, encrypted_message_string_values)))
    print("Your Decryption Key is: " + construct_decryption_key(random_integer))


def get_zero_index_user_message(user_message):
    '''
        Constructs an array of the ascii values of the given message for encryption

        Args:
            user_message (str) : The message as given by the user

        Returns:
            user_message_zero_index_values (array) : The array of zero-indexed letter values (0 - 25)
                of the given message for encryption
    '''

    user_message_zero_index_values = []
    for letter in user_message:
        if str.isalpha(letter) and is_uppercase_letter(letter):
            user_message_zero_index_values.append(Letter(ord(letter) - 65, True))
        elif str.isalpha(letter) and not is_uppercase_letter(letter):
            user_message_zero_index_values.append(Letter(ord(letter) - 97, False))
        elif not str.isalpha(letter):
            user_message_zero_index_values.append(letter)
    return user_message_zero_index_values


def is_uppercase_letter(letter):
    '''
        Returns true if the given letter is an uppercase letter. False if it isn't.

        Args:
            letter (str) : The letter we are checking its case for

        Returns:
            boolean : True if letter is uppercase, false if not
    '''

    if 65 <= ord(letter) <= 90:
        return True
    if 97 <= ord(letter) <= 122:
        return False
    return False


def get_zero_index_encrypted_message(user_message_zero_index_values, random_integer):
    '''
        Encrypts the previously created array of the user's strings into
        by using the Caesar's Cipher to reposition the index letters from 0 - 25

        Args:
            user_message_zero_index_values (array) : The array of zero index values that contain the
                original user's string to be encrypted
            random_integer : The random integer used for deciding the index by which to
                move the ASCII index values for Caesar's Cipher

        Returns:
            (array) : Array of the encrypted message from the user in encrypted letter index values
                (0 - 25) done using Caesar's Cipher
    '''

    ascii_pointer = 0
    zero_index_encrypted_message = []
    for value in user_message_zero_index_values:
        if ascii_pointer % 2 == 0 and type(value) is Letter:
            new_ascii_value = (value.letter_value + random_integer) % 26
            zero_index_encrypted_message.append(Letter(new_ascii_value, value.uppercase))
            ascii_pointer += 1
            continue
        elif ascii_pointer % 2 != 0 and type(value) is Letter:
            new_ascii_value = (value.letter_value - random_integer) % 26
            zero_index_encrypted_message.append(Letter(new_ascii_value, value.uppercase))
            ascii_pointer += 1
            continue
        else:
            zero_index_encrypted_message.append(value)
            ascii_pointer += 1
            continue
    return zero_index_encrypted_message


def construct_encrypted_string_values(encrypted_message_zero_index):
    '''
        Constructs the string from the encrypted zero-indexed values as previously generated.
        This string is the encrypted result as presented to the user

        Args:
            encrypted_message_zero_index (array) : The array of the encrypted message as given in zero-index (0 - 25) form
        Returns:
            (array) : The array of zero-index values that have been encrypted, now presented as an array of characters
    '''
    encrypted_string_values = []
    for value in encrypted_message_zero_index:
        if type(value) == Letter:
            if value.uppercase:
                encrypted_string_values.append(chr(value.letter_value + 65))
            else:
                encrypted_string_values.append(chr(value.letter_value + 97))
        else:
            encrypted_string_values.append(value)
    return encrypted_string_values


def construct_decryption_key(random_integer):
    '''
        Returns a string of the decryption key that can be used for decryption.
        The decryption key contains a substring that can be used to identify the index
        by which the Casesar's Cipher algorithm was used

        Args:
            random_integer (int) : The random integer which is used to construct
                the decryption key

        Returns:
            (str) : The decryption key in string type
    '''
    if random_integer == 1:
        return "{0}0x3{0}{0}{0}{0}".format(randint(0, 9))
    elif random_integer == 2:
        return "{0}{0}{0}8y3{0}{0}".format(randint(0, 9))
    elif random_integer == 3:
        return "{0}2e7{0}{0}{0}{0}".format(randint(0, 9))
    elif random_integer == 4:
        return "{0}{0}{0}{0}8z5{0}".format(randint(0, 9))
    elif random_integer == 5:
        return "3c8{0}{0}{0}{0}".format(randint(0, 9))
    elif random_integer == 6:
        return "{0}5g7{0}{0}{0}{0}".format(randint(0, 9))
    elif random_integer == 7:
        return "{0}{0}{0}{0}{0}8m4".format(randint(0, 9))
