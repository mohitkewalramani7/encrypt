from click._compat import raw_input

'''
Helper methods to complete the decryption process of a given string

__author__ = "Mohit Kewalramani"
__version__ = 2.0
__published__ = 30 April 2017
'''


def perform_decryption():
    '''
        The function that can be used to decrypt a given message, given the message and a
        decryption key. It prints out the decrypted message to the terminal

        Returns:
            None
    '''

    message_for_decryption = raw_input("\n\nPlease Enter Your Message for Decryption: \n\n")
    given_decryption_key = raw_input("\nPlease Enter Your Given Decryption Key\n\n")

    given_decryption_key = given_decryption_key.strip("\n")
    decoded_random_integer = return_decoded_integer(given_decryption_key)
    if decoded_random_integer == 0:
        print("\nDecryption Key Is Incorrect. Please Enter Correct Decryption Key")
        return

    message_for_decryption = message_for_decryption.strip("\n")
    zero_indexed_encrypted_values = get_zero_indexed_encrypted_values(message_for_decryption)
    zero_indexed_decrypted_values = get_zero_indexed_decrypted_values(zero_indexed_encrypted_values,
                                                                      decoded_random_integer)
    decrypted_message_string = get_decrypted_string_message(zero_indexed_decrypted_values, message_for_decryption)
    print("\n\nYour Decrypted Message is: " + "".join(map(str, decrypted_message_string)))


def return_decoded_integer(given_decryption_key):
    '''
        Decodes the Caesar's Cipher shift value that was used for encryption
        by locating the respective substring in the decryption key

        Args:
            given_decryption_key (str) : The decryption key given to the user
        Returns:
            (int) : The integer value used as the index shift for the Caesar's Cipher
                shift
    '''
    if "0x3" in given_decryption_key:
        return 1
    elif "8y3" in given_decryption_key:
        return 2
    elif "2e7" in given_decryption_key:
        return 3
    elif "8z5" in given_decryption_key:
        return 4
    elif "3c8" in given_decryption_key:
        return 5
    elif "5q7" in given_decryption_key:
        return 6
    elif "8m4" in given_decryption_key:
        return 7
    return 0


def get_zero_indexed_encrypted_values(message_for_decryption):
    '''
        Takes in the encrypted message, and each character back to 0 indexed
        letter values (0 - 25) as an Array for the next step in the process

        Args:
            message_for_decryption (str) : The message for decryption

        Returns:
            (array) : The array of letter index values (0 - 25) for the encrypted string
    '''
    zero_indexed_encrypted_values = []
    for letter in message_for_decryption:
        if is_uppercase_letter(letter) and str.isalpha(letter):
            zero_indexed_encrypted_values.append(ord(letter) - 65)
        elif not is_uppercase_letter(letter) and str.isalpha(letter):
            zero_indexed_encrypted_values.append(ord(letter) - 97)
        else:
            zero_indexed_encrypted_values.append(letter)
    return zero_indexed_encrypted_values


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


def get_zero_indexed_decrypted_values(zero_indexed_encrypted_values, decoded_random_integer):
    '''
        Decrypts the values of the encrypted zero-indexed letter values (0 - 25) based on the
        original index shift that was done during the initial Caesar's Cipher application

        Args:
            zero_indexed_encrypted_values (array) : The array of zero-indexed letter values that
                require decryption
            decoded_random_integer (int) : The integer value by which to apply the Caesar's Cipher
                in opposite to what was originally done

        Returns:
            (array) : The array of zero indexed letter values that have now been decrypted
                as a result of oppositely applying the Caesar's Cipher
    '''
    position = 0
    zero_indexed_decrypted_values = []
    for item in zero_indexed_encrypted_values:
        if position % 2 == 0 and type(item) is int:
            zero_indexed_decrypted_values.append((item - decoded_random_integer) % 26)
            position += 1
            continue
        elif position % 2 != 0 and type(item) is int:
            zero_indexed_decrypted_values.append((item + decoded_random_integer) % 26)
            position += 1
            continue
        else:
            zero_indexed_decrypted_values.append(item)
            position += 1
            continue
    return zero_indexed_decrypted_values


def get_decrypted_string_message(zero_indexed_decrypted_values, message_for_decryption):
    '''
        Concatenates the array of zero indexed decrypted characters into the original string message
        that is returned to the user

        Args:
            zero_indexed_decrypted_values : The array containing the zero-indexed letter values (0 - 255)
                that is used for constructing the decrypted string
            message_for_decryption : The original string value used for decryption to assist in the indexing
                and concatenation process

        Returns:
            An array of characters that when combined together re-form the encrypted message
    '''
    position_to_final_decryption = 0
    decrypted_message_array = []
    for char in message_for_decryption:
        try:
            int(char)
            decrypted_message_array.append(char)
            position_to_final_decryption += 1
            continue
        except Exception as e:
            pass
        if not str.isalpha(char):
            decrypted_message_array.append(char)
            position_to_final_decryption += 1
            continue
        if is_uppercase_letter(char):
            final_char_ascii_value = zero_indexed_decrypted_values[position_to_final_decryption] + 65
            final_char_value = chr(final_char_ascii_value)
            decrypted_message_array.append(final_char_value)
            position_to_final_decryption += 1
            continue
        elif not is_uppercase_letter(char):
            final_char_ascii_value = zero_indexed_decrypted_values[position_to_final_decryption] + 97
            final_char_value = chr(final_char_ascii_value)
            decrypted_message_array.append(final_char_value)
            position_to_final_decryption += 1
            continue
        else:
            decrypted_message_array.append(char)
            position_to_final_decryption += 1
    return decrypted_message_array
