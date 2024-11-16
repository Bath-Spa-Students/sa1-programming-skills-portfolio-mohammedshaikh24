#Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.

### Basic Requirements:
#1. Define the correct password.
#2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
#3. Output an appropriate message when the correct password is entered.


def password_for_user_verification_system():#asks the user for a password and checks if it is the right password
    real_password = "12345"# The right password for user verification
    
    while True:#this code is used to loop until the password input by the user is correct
        user_password = input("Please input the password that is required: ")#assigning a question to a variable for the user to input a password
        
        if user_password == real_password:
            print("Entry granted. Password confirmed.!")#these words are print,if the answer given is correct.
            break#code that breaks the loop if answer given is correct 
        else:
            print("Wrong password. Retry.")#these words are print,if the answer given is wrong.

password_for_user_verification_system()
