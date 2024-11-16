#Write a program that tests if a value is even or odd. Follow the instructions outlined below:

### Instructions:
#* The program should ask the user for a number from within the main function.
#* The entered number should be passed to a function that determines if the value is even or odd.
#* The function should return a message indicating whether the number is even or odd.
#* The message returned by the function should be printed from within the main function.

def verify_odd_even(integer):
    #it verifies if the integer is odd or even and provides the user with a correct response
    if integer % 2 == 0:
        return "This integer is even."
    else:
        return "This integer is odd."

def main():
    #provide the user with a question in which they can input their integer
    user_choice = int(input("Please enter an integer: "))
    
    #this prompt prints the function verify_odd_even and shows the output
    output = verify_odd_even(user_choice)
    print(output)

#this prompt makes sure it runs main() only when the you run the file
if __name__ == "__main__":
    main()
