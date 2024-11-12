def is_leap(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If the year is divisible by 100, check if it is also divisible by 400
        if year % 100 == 0:
            return year % 400 == 0  # Year is leap if divisible by 400
        else:
            return True  # Year is leap if divisible by 4 but not 100
    else:
        return False  # Year is not a leap year if not divisible by 4

# Get the year from user input
# Call the function and print the result
