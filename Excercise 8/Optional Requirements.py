### Optional Requirements:
#1. Allow the user to input the search term instead of using a predefined value.
#2. Implement the search functionality based on user input.

#Assigning Names to variable called name_list
name_list = ["manaar","mohammed","ali","shaikh","khan"]

#Assigning a question so the user can search for the name they want/need

user_choice = input("Who would you like to find in the list given below?:")

#utilizing an if-else structure to determine whether the name exists in the list
if user_choice.strip().lower() in name_list:
    print(f"You have found {user_choice} in the list.")
else:
     print(f"You have not found {user_choice} in the list.")