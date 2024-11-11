#Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

### Instructions:
#1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
#2. Input Handling: Ask the user to input the month number.
#3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.

#Assigning all the months to the variable months
days_months = {
    1: 31,  # January has 31 days
    2: 28,   # February tusually has 28 days 
    3: 31,   # March has 31 days
    4: 30,   # April has 30 days
    5: 31,   # May has 31 days
    6: 30,   # June has 30 days
    7: 31,   # July has 31 days
    8: 31,   # August has 31 days
    9: 30,   # September has 30 days
    10: 31,  # October has 31 days
    11: 30,  # November has 30 days
    12: 31   # December has 31 days
}

#Allow the user to input an integer they would like
month_integer = int(input("Enter the number of the month (1-12): "))

#If the integer given by the user is in the system then this will be printed
if 1 <= month_integer <= 12:
    print(f"The number of days in the month {month_integer} is {days_months[month_integer]}.")
else:
    print("Invalid month number. Please enter a number you would like to choose between 1 and 12.")#If the integer given by the user is not in the system then this will be printed