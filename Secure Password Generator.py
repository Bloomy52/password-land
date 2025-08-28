#Louie Bloomberg
#Password Land
#The Secure Password Generator! & Password Checker!
#Version 1.0

import random 
import string 
import secrets 
import math 
import hashlib 
import requests 

#######BEGIN FUNCTION DEFINITIONS###################
def load_words(file): 
    """
    Function loads words into list, words
    Param: file, string - it contains the name of the text file with the words to be used for the password.
    Returns: words, a list containing the words.
    """
    with open(file,"r", encoding="utf8") as infile:
        words = infile.read().split()
        
    return words

def password_selection():
    """
    This function provides the backbone for creating the user's password. It will go through a series of questions
    using if statements to go through the selection process. It might be long...
    Params: NONE
    Return Value: an integer corresponding to the password selection they chose.
    """
    print("Welcome to the Secure Password Generator & Password Checker")
    print("To Begin, please select the type of password you would like using a num-pad/num-row on your keyboard.")
    print("Alphanumeric Password: 1")
    print("Alphabetic Password: 2") 
    print("Numeric Password: 3") 
    print("Completely Random Password: 4")
    print("Check Your Password?: 5")
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
    elif select1 == 5:
        print("This will check your password against the Pwned Passwords database.")
        return 5
    else:
        return -1


def get_pw_length(sel):
    """
    Asks user for character length based on their selection from earlier
    Parameter: sel, an integer corresponding to their choice from above.
    Returns: length, an integer instructing the program how many characters are required.
    """
    if sel == 2: #word only
        length = int(input("How many words should the password be? (Must be 4+ - default = 4)"))
        if length >= 4:
            return length
        else:
            return 4
    elif sel == 3: #numeric
        length = int(input("How many digits should the passcode be? (Must be 6+ digits - default = 8)"))
        if length >= 6:
            return length
        else:
            return 8
    elif sel == 4: #random
        length = int(input("How many characters should the password be? (Must be 12+ characters - default = 12)"))
        if length >= 12:
            return length
        else:
            return 12


def create_alphanumeric_password(words): #1 (Default Password) - This is the standard alphanumeric password
    """
    This function creates an alphanumeric password by choosing two words from the words list, 4 random numbers, and a punctuation mark.
    Parameter: words, a list containing the English dictionary
    Returns: password, a string containing the alphanumeric password in the following format:
    Word1+word2+4-digit-number+punctuation-mark.

    Lots of things have similar credits so, I am not going to continuously type the same things over for the same exact things.
    I am just being lazy. Sorry. 
    P.S. This was coded out of order so references will be out of order.
    """
    password = "" 
    two_words = "" #stores the two random words
    for i in range(2): #add two random words
        two_words+=secrets.choice(words)
    #Now numbers
    passcode = create_num_password(4)    #calls the create_number_password function to create 4 digit passcode
    punc_list = string.punctuation       #I was lazy and didn't feel like creating the number generator over again.
    punc_mark = secrets.choice(punc_list)#Chooses ASCII punctuation

    password = two_words + str(passcode) + punc_mark #adds everything together
    password = password.capitalize() #capitalizes the first letter
    return password #returns alphanumeric password

def create_word_password(words, num_words=4): #2
    """
    Function creates an alphabetic password by choosing four words from the words list and combines them
    Parameter: words, a list containing the words 
               num_words, an integer with a default parameter of 4 words; must be greater than 4
    Returns: password, a string containing the password
    """
    password = ""
    for i in range(num_words):
        password+=secrets.choice(words) #Information about secrets.choice is in the import information
        
    return password


def create_num_password(digits=8):#3
    """ 
    Creates a numeric password of a length entered by user. Default = 8, must be greater than 6 digits
    Params: digits, an integer with a default parameter of 8.
    Returns: passcode, an integer containing the passcode

    EXCEPTION: This function is used in the alphanumeric, and it produces a 4 digit number

    GeeksForGeeks helped me with the random.seed() function and implimenting it.
    Link: https://www.geeksforgeeks.org/random-seed-in-python/#
    Also, credit to datagy.io for help with truncation of decimals
    Link: https://datagy.io/python-truncate-float/
    """
    seed = secrets.randbits(256) #Python docs links for secrets and random are above - both helped me lots
    random.seed(seed)
    num = random.random()
    tens_place = math.pow(10, digits) #Python math libraries are above. Credit to docs for help
    passcode = num*tens_place
    passcode = math.trunc(passcode)
    return passcode


def create_random_password(ascii_list, chars=12): #4
    """
    Uses the 94 possible ascii charater set (uppercase, lowercase, digits, and punctuation) to make a random password
    Parameter: ascii_list, a string containing all possible ascii characters (excluding whitespace).
               chars, an integer with a default parameter of 12 characters for password length; must be greater than 12
    Returns: password, a string containing the password

    Python Secrets Module Docs was a big help in this. (link in import information above)
    """
    
    password = ""
    for i in range(chars):
        password += secrets.choice(ascii_list) #especially secrets.choice
    
    return password


def check_password(): #5
    """ 
    This function checks against a database which has lots of breached passwords.
    Params: None. All params and such are taken care of through function.
    Returns: A boolean: True, if found in breach ; False, if not found in breach.
    """
    #Explains a little bit. Sorry about the code nonsense.
    """
    So this is just an explaination on how this check password system should
    work and how I will do it...
    So I am going to import requests (the api calling module) and then I will
    follow the guidance from the rapidapi.com website for the explaination
    on how to use the request module. Also the module docs docs.python-requests.org
    After the user inputs their password, I will use the hashlib module to create
    an SHA-1 hash with guidance from the Geeks For Geeks website.
    I will then use the 'Have I Been Pwned' API and the range system to help me
    get the hash range to check if it even exists.
    *https://haveibeenpwned.com/API/v3#PwnedPasswords*
    If it does, then search the rest of the range to see if the hash exists in the
    breach. If not, then report it wasn't found.
    Hopefully this makes sense. If it doesn't, please let me know. -LB
    """
    #To test out the system using the Testing PwnedPasswords API, you must have JupyterLabs installed. 
    #(There are online versions such as Google Collabs) if you want to try it out. -LB
    
    #Potential that I might break this into more functions.
    #Depends on how I feel about typing more docstrings.

    #Comments are there to help explain code since this is really weird.
    
    user_pw = input("Please enter your password: ")
    password_hash = hashlib.sha1(user_pw.encode()) #SHA-1 Hash word
    password_hash = password_hash.hexdigest() #Set as a hexdigest
    password_hash = password_hash.upper() #Make Uppercase.
    
    hash_range = password_hash[:5] #First five indicies in string --> hash_range
    
    url = "https://api.pwnedpasswords.com/range/" #Sets URL for API
    url+=hash_range #Adds the hash range
    response = requests.get(url) #Sends the request using the requests.get() function
    #https://docs.python-requests.org/en/latest/user/quickstart/#make-a-request

    if response.status_code == 200:
        #Continues on with the rest of this code.
        data = response.text #Helpful website: https://www.geeksforgeeks.org/response-text-python-requests/
        data_list = data.split("\r\n") #splits into list using delineators \r\n
        
        #https://docs.python.org/3/library/stdtypes.html#str.removeprefix
        #Used for removing the range from the rest of the hash
        check_hash = password_hash.removeprefix(hash_range) #removes hash_range
        
        hashes = [] #creates empty list
        for i in range(len(data_list)): #for loop for adding the hashes to list
            str = "" #start new string
            for j in range(len(data_list[i])): #cycle through hash
                if data_list[i][j] == ":":
                    break #move onto next hash
                else:
                    str+= data_list[i][j] #adds hexdigest to str
            hashes.append(str) #adds the hash to the list
            
        #check if hash in breach
        for i in hashes:
            if check_hash == i:
                return True #NOT SAFE!! PASSWORD FOUND IN BREACH
        return False #not found in breach (therefore 'safe'(maybe))

    else:
        return False
    ###This uses an API reference, this is mainly credited to the links in the module above.
    #I have attached a Jupyter Notebook in this.


####################MAIN######################

#Main

#Load File:
words = load_words("words_alpha.txt") #This is only placed this way so someone could use their own dictionary

#Create ASCII list -- Credit Python Doc for usage on String Module (link above)
ascii_list = string.ascii_letters + string.digits + string.punctuation #94 characters.


#Password Selection to determine next steps - calls different functions
pw_sel = False
while pw_sel == False:
    
    sel = password_selection() #any more customizations will be done in functions
    
    if sel == 1: #alphanumeric
        pw_sel = True
        pw = create_alphanumeric_password(words)
        print(pw) #print password
    elif sel == 2: #word only
        pw_sel = True
        num_words = get_pw_length(2)
        pw = create_word_password(words, num_words)
        print(pw)
    elif sel == 3: #numeric
        pw_sel = True
        digits = get_pw_length(3)
        pw = create_num_password(digits)
        print(pw)
    elif sel == 4: #random
        pw_sel = True
        chars = get_pw_length(4)
        pw = create_random_password(ascii_list, chars)
        print(pw)
    elif sel == 5: #check pw if breached
        pw_sel = True
        pw = check_password() #will ask for input in function
        if pw == True:
            print("Password was found in data breach! DO NOT USE THIS PASSWORD!!!!")
        else:
            print("Password has not been found in a data breach. Just because it wasn't found in a data breach DOES NOT mean it is a SECURE password.")
    elif sel == -1:
        pw_sel = False
        print("Invalid Selection. Please select one of the options.\n")


