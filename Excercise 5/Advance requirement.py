### Advanced Requirement:
#Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly.

# Assigning all the months to the variable `days_months`
days_months = {
    1: 31,  # January has 31 days
    2: 28,  # February usually has 28 days
    3: 31,  # March has 31 days
    4: 30,  # April has 30 days
    5: 31,  # May has 31 days
    6: 30,  # June has 30 days
    7: 31,  # July has 31 days
    8: 31,  # August has 31 days
    9: 30,  # September has 30 days
    10: 31, # October has 31 days
    11: 30, # November has 30 days
    12: 31  # December has 31 days
}

# Allow the user to input an integer for the month
month_integer = int(input("Enter the number of the month (1-12): "))

# Check if the month number is valid
if 1 <= month_integer <= 12:
    if month_integer == 2:
        # Asking if it's a leap year
        leap_year = input("Is it a leap year? (yes/no): ").strip().lower()
        if leap_year == 'yes':
            # Adjust the days for February in a leap year
            print("The number of days in the month February (leap year) is 29.")
        else:
            # Print the normal number of days for February
            print("The number of days in February (not a leap year) is 28.")
    else:
        # Print the number of days for other months
        print(f"The number of days in the month {month_integer} is {days_months[month_integer]}.")
else:
    # Print an error message if the input is invalid
    print("Invalid month number. Please enter a number between 1 and 12.")