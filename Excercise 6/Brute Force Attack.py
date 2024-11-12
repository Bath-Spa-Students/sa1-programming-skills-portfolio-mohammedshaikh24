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
