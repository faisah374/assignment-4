#Write a program which prompts the user for a temperature in Fahrenheit 
# (this can be a number with decimal places!) and outputs the temperature converted to Celsius.
# The formula for converting Fahrenheit to Celsius is: C = (F - 32) * 5/9.
# Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!)

def main():
    # Ask the user for a temperature in Fahrenheit in bold italics
    fahrenheit = float(input("\033[1;3m What is the temperature in Fahrenheit ____?\033[0m "))
    # Convert the temperature to Celsius using the formula C = (F - 32) * 5/9
    celsius = (fahrenheit - 32) * 5 / 9
    # Output the temperature in Celsius in bold italics
    print(f"\033[1;3m The temperature in Celsius is: {celsius:.2f}°C\033[0m")
if __name__ == "__main__":
    main()    