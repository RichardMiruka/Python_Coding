import calendar                                        # Import the calendar module to access calendar functionalities

def display_calendar():                                # Define a function to display the calendar
    try:
        year = int(input("Enter the year: "))          # Prompt user for the year and convert input to integer
        if year < 1 or year > 9999:                    # Check if the year is within a valid range
            raise ValueError("Invalid year. Please enter a year between 1 and 9999")

        month = int(input("Enter the month (1-12): ")) # Prompt user for the month and convert input to integer
        if month < 1 or month > 12:                    # Check if the month is within the valid range of 1 to 12
            raise ValueError("Invalid month. Please enter a month between 1 and 12")

        cal = calendar.TextCalendar(calendar.SUNDAY)   # Create a TextCalendar instance, starting the week with Sunday

        month_calendar = cal.formatmonth(year, month)  # Generate a string representation of the specified month
        print(month_calendar)                          # Display the formatted month calendar
    except ValueError as e:                            
        print(f"Invalid input: {e}. Please enter a valid year and month.")  # Display an error message if input is invalid

display_calendar()                                     # Call the function to run the calendar display program
