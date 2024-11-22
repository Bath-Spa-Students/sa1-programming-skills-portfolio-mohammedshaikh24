### Advanced Requirements:
#Have the user input their name, hometown, and age instead of hardcoding the values.
#Try giving both your first and second name when asked for your name. What happens? How can you handle multiple words in Python?
#Test the program by entering a string value for age (e.g., "twenty"). What happens? How can you prevent this issue?

#Assigning questions to variables
user_name = input("Enter your name (first and last): ")
user_hometown = input("Enter your hometown: ")

#set up a prompt so that the user can only put in integer in age
while True:
    try:#this prompt is used to make sure the user uses only integers
        user_age = int(input("Enter your age: "))
        break  #code that breaks the loop if answer given is correct 
    except ValueError:#otherwise if the user uses a string then it will show error
        print("That's not a valid number. Enter your age using digits only.")

#prompt to store all the information  given by the user
user_info = {
    "M": user_name,
    "N": user_hometown,
    "R": user_age
}

#adding /n to every answer so that it appears in a new line
print(f"Name: {user_info['M']}\nHometown: {user_info['N']}\nAge: {user_info['R']}")
