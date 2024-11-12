real_password = "12345"# The right password for user verification

# Maximum number of attempts
attempt_limit = 5


attempts = 0

#this code is used to loop until the password input by the user is correct or if the user has not gone over 5 tries
while attempts < attempt_limit:
    # Ask the user to enter the password
    user_password = input("Enter the password that is required: ")#assigning a question to a variable for the user to input a password
    
    if user_password == real_password:
            print("Entry granted. Password confirmed.!")#these words are print,if the answer given is correct.
            break#code that breaks the loop if answer given is correct 
    else:
        attempts += 1#everytime the password is wrong, the attempts goes up by 1.
        attempts_left = attempt_limit - attempts#prompt to check how many attempts remain.
        if attempts_left > 0:#and if there are attempts remaining, let the user know.
            print(f"Wrong password. The amount of try(ies) remaining are {attempts_left}.")
        else: #if tries reach zero, let the user know and contact the law enforcement
            print("Wrong password. You have used all your attempts.")
            print("A security breach has been reported and Law enforcement has been contacted.")
            break#code that breaks the loop if attempts have finished 