while True:#this code is used to loop until the input by the user is written as quit
        user_topping = input("Input a pizza topping of your choice(or enter 'quit' to finish): ")#assigning a message to a variable for the user to input a topping
        
        if user_topping.lower() == 'quit':
            break#code that breaks the loop if answer given is correct 
        print(f"I will add {user_topping} to your custom made pizza.")
#printing this if the user chooses a topping
        