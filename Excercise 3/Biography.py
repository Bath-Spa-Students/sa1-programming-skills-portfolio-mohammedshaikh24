#In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.

### Steps:
#1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
#2. Print the values on separate lines using a single `print()` statement.
#3. Use variables with appropriate data types for each piece of information.

#Assigning a variable
person_info = {"name" : "manaar" ,
               "hometown" : "delhi" ,
               "age" : "18"}

#Adding /n to every answer so that it appears in a new line
print(f"Name: {person_info['name']}\nHometown: {person_info['hometown']}\nAge: {person_info['age']}")