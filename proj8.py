#File Name: proj8.py
#Name: Gloria Silva
#Date: Dec. 3, 2025
#Description: This program asks the user to choose a password based on 5 rules. It then checks the password against the 5 rules, and asks the user again for a password if it does not pass the rules, or it says password set if it does.

def password_rules(): #This function is what prints out the message asking the user for a password, and the 5 rules. 
    print('Choose a password according to these rules:')
    print('The password must be at least 8 characters long')
    print('The password must contain both uppercase and lowercase letters')
    print('The password must contain at least one digit')
    print('The password must contain at least one of the following special characters: !, #, $, &')
    print('The password may not contain any of the following characters: @, %, ^, *')

def validate_pw(passwd): #This function is what checks the password against the 5 rules. 
    has_upper = False #These set the variables, so that we can check them.
    has_lower = False
    has_digit = False
    has_special = False
    has_invalid = True
    special_ch = "!#$&" #The special characters and the invalid ones (the ones not allowed).  
    invalid_ch = "@%^*"
    for ch in passwd: #This is a for loop that checks the password for 4 rules, the uppercase and lowercase rule being on different lines. 
        if ch.isupper(): #This checks it for uppercase letters.
            has_upper = True
        if ch.islower(): #This checks it for lowercase letters.
            has_lower = True
        if ch.isdigit(): #This checks it for a digit.
            has_digit = True
        if ch in special_ch: #This checks it for the special characters. 
            has_special = True
        if ch in invalid_ch: #This checks it for the invalid characters, the ones not allowed. 
            has_invalid = False
    validation = True #Password passes the 5 rules. 
    if len(passwd) < 8: #This checks the length of the password, if it is less than 8 characters. 
        print('The password must be at least 8 characters long')
        validation = False
    if not has_upper and has_lower: #Prints out the rule again if it has no upper and lower case letters. 
        print('The password must contain both uppercase and lowercase letters')
        validation = False
    if not has_digit: #Prints out the rule again if it has no digits. 
        print('The password must contain at least one digit')
        validation = False
    if not has_special: #Prints out the rule again if it has no special characters.
        print('The password must contain at least one of the following special characters: !, #, $, &')
        validation = False
    if not has_invalid: #This prints out the rule again if it has any characters that are not allowed. 
        print('The password may not contain any of the following characters: @, %, ^, *')
        validation = False
    return validation

def main(): #This is the main function. It has the password_rules and the validate_pw(passwd) functions.
    password_rules()
    print()
    passwd = input('Enter password:') #This asks the user for the password, and stores it in a variable.
    passwd_validated = validate_pw(passwd) #The password is validated. 
    while not passwd_validated: #This is a while loop if the password was not validated. (Validation loop). 
        passwd = input('Enter password:') #It asks the user again for a password until it is a valid one. 
        passwd_validated = validate_pw(passwd)
    print('Password set.') #Lets the user know the password is set once the user enters a valid one. 

main() #This calls the main function. 