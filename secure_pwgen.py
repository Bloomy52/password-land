# Louie Bloomberg
# The Secure Password Generator!

__version__ = "1.0.0"

# Importing Modules: Links for things are mostly here with some other links scattered around.
import random
import string
import secrets
import math


#######BEGIN FUNCTION DEFINITIONS###################
def load_words(file):
    """
    Function loads words into list, words
    Param: file, string - it contains the name of the text file with the words to be used for the password.
    Returns: words, a list containing the words.
    """
    with open(file, "r", encoding="utf8") as infile:
        words = infile.read().split()

    return words


def password_selection():
    """
    This function provides the backbone for creating the user's password as it handles selections
    Params: NONE
    Return Value: an integer corresponding to the password selection they chose.
    """
    print("Welcome to the Secure Password Generator")
    print("To Begin, please select the type of password you would like using a num-pad/num-row on your keyboard.")
    print("Alphanumeric Password: 1")
    print("Alphabetic Password: 2")
    print("Numeric Password: 3")
    print("Completely Random Password: 4")
    select1 = int(input(""))

    if select1 == 1:
        print("This password will contain words, numbers, and punctuation.")
        return 1
    elif select1 == 2:
        print("This password will contain 4 random words ONLY.")
        return 2
    elif select1 == 3:
        print("This password will contain numbers ONLY.")
        return 3
    elif select1 == 4:
        print("This password will consist of all ASCII Characters in a random order.")
        return 4
    else:
        return -1


def get_pw_length(sel):
    """
    Asks user for character length based on their selection from earlier
    Parameter: sel, an integer corresponding to their choice from above.
    Returns: length, an integer instructing the program how many characters are required.
    """
    if sel == 2:  # word only
        length = int(input("How many words should the password be? (Must be 4+ - default = 4)"))
        if length >= 4:
            return length
        else:
            return 4
    elif sel == 3:  # numeric
        length = int(input("How many digits should the passcode be? (Must be 6+ digits - default = 8)"))
        if length >= 6:
            return length
        else:
            return 8
    elif sel == 4:  # random
        length = int(input("How many characters should the password be? (Must be 12+ characters - default = 12)"))
        if length >= 12:
            return length
        else:
            return 12


def create_alphanumeric_password(words):  # 1 (Default Password) - This is the standard alphanumeric password
    """
    This function creates an alphanumeric password by choosing two words from the words list, 4 random numbers, and a punctuation mark.
    Parameter: words, a list containing the English dictionary
    Returns: password, a string containing the alphanumeric password in the following format:
    Word1+word2+4-digit-number+punctuation-mark.
    """
    password = ""
    two_words = ""  # stores the two random words
    for i in range(2):  # add two random words
        two_words += secrets.choice(words)
    # Now numbers
    passcode = create_num_password(4)  # calls the create_number_password function to create 4 digit passcode
    punc_list = string.punctuation
    punc_mark = secrets.choice(punc_list)  # Chooses ASCII punctuation

    password = two_words + str(passcode) + punc_mark  # adds everything together
    password = password.capitalize()  # capitalizes the first letter
    return password  # returns alphanumeric password


def create_word_password(words, num_words=4):  # 2
    """
    Function creates an alphabetic password by choosing four words from the words list and combines them
    Parameter: words, a list containing the words
               num_words, an integer with a default parameter of 4 words; must be greater than 4
    Returns: password, a string containing the password
    """
    password = ""
    for i in range(num_words):
        password += secrets.choice(words)

    return password


def create_num_password(digits=8):  # 3
    """
    Creates a numeric password of a length entered by user. Default = 8, must be greater than 6 digits
    Params: digits, an integer with a default parameter of 8.
    Returns: passcode, an integer containing the passcode

    EXCEPTION: This function is used in the alphanumeric, and it produces a 4 digit number
    """
    seed = secrets.randbits(256)
    random.seed(seed)
    num = random.random()
    tens_place = math.pow(10, digits)
    passcode = num * tens_place
    passcode = math.trunc(passcode)
    return passcode


def create_random_password(ascii_list, chars=12):  # 4
    """
    Uses the 94 possible ascii charater set (uppercase, lowercase, digits, and punctuation) to make a random password
    Parameter: ascii_list, a string containing all possible ascii characters (excluding whitespace).
               chars, an integer with a default parameter of 12 characters for password length; must be greater than 12
    Returns: password, a string containing the password
    """

    password = ""
    for i in range(chars):
        password += secrets.choice(ascii_list)

    return password


####################MAIN######################

# Main

# Load File:
words = load_words(
    "words_alpha.txt")  # You need to download the words_alpha.txt file and place that into the same directory or it won't work
# You can replace words_alpha.txt with any other document that contains the words you would like to use
# Create ASCII list
ascii_list = string.ascii_letters + string.digits + string.punctuation

# Password Selection to determine next steps - calls different functions
pw_sel = False
while pw_sel == False:

    sel = password_selection()  # any more customizations will be done in functions

    if sel == 1:  # alphanumeric
        pw_sel = True
        pw = create_alphanumeric_password(words)
        print(pw)  # print password
    elif sel == 2:  # word only
        pw_sel = True
        num_words = get_pw_length(2)
        pw = create_word_password(words, num_words)
        print(pw)
    elif sel == 3:  # numeric
        pw_sel = True
        digits = get_pw_length(3)
        pw = create_num_password(digits)
        print(pw)
    elif sel == 4:  # random
        pw_sel = True
        chars = get_pw_length(4)
        pw = create_random_password(ascii_list, chars)
        print(pw)

    elif sel == -1:
        pw_sel = False
        print("Invalid Selection. Please select one of the options.\n")

