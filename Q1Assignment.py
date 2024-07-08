# Task 1
# Ask user to input temperature
try:
    temperature = float(input("Please enter the temperature in Fahrenheit: "))
    print(f"The temperature you entered is {temperature}°F.")
except ValueError:
    print("Error: Please enter a valid number for the temperature.")

# Task 2
# Converting fahrenheit to celsius while having an exception in place in case they enter a string instead of float/int
def convert_temperature(fahrenheit):
    try:
        # Convert the Fahrenheit temperature to Celsius
        celsius = (float(fahrenheit) - 32) * 5/9
    except ValueError:
        # Handle the case where the user enters a non-numeric value
        print("Oops! That's not a valid number. Please enter a numeric value.")
        return None
    

# Task 3
# Implement an else block that prints the converted temperature in a user-friendly format
    else:
        print(f"{fahrenheit} degrees Fahrenheit is {round(celsius, 2)} degrees Celsius.")
        return celsius

# Task 4
# Add a finally block that thanks the user for using the weather forecast application

    finally:
        print("Thank you for using the weather forecast application!")

# Call the function with the user's input
convert_temperature(temperature)