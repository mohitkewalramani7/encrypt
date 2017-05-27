from encryption_helpers import *
from decryption_helpers import *
from Tools.scripts.treesync import raw_input

'''
The main file where the script starts to run. The initiation methods are located here

__author__ = "Mohit Kewalramani"
__version__ = 2.0
__published__ = 30 April 2017
'''

def main():
    '''
    Starting point or programme from the command line
    '''
    user_person_choice = ask_question()
    while user_person_choice != "1" and user_person_choice != "2":
        user_person_choice = wrong_argument()
    print(user_person_choice)
    if user_person_choice == "1":
        perform_encryption()
    elif user_person_choice == "2":
        perform_decryption()

def ask_question():
    '''
    Asks the user to the user about whether they want to encrypt or decrypt a message

    Returns:
         (str) : The choice the user has made
    '''
    choice_message = "Hello There! \nWhat would you like to do today:\n\n1.Encrypt My Message\n2.Decrypt My Message" \
                     "\n\nChoose 1 or 2\n\n"
    user_choice = raw_input(choice_message)
    return user_choice.strip("\n")


def wrong_argument():
    '''
    A function to re-ask the user if they initially select the wrong option

    Returns:
        (str) : The new option the user has selected
    '''
    error_message = "Please Select 1 or 2\n"
    new_choice = raw_input(error_message)
    return new_choice.strip("\n")


if __name__ == '__main__':
    main()
