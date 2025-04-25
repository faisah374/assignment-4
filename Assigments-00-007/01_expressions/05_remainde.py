# Ask the user for two numbers, one at a time, and then print the result 
# of dividing the first number by the second and also the remainder of the division.

# Here's a sample run of the program (user input is in bold italics):
 # Please enter an integer to be divided: 5

# Please enter an integer to divide by: 3


def main():
    # The result of this division is 1 with a remainder of 2
    # Get the first number from the user and cast it to be a number
    first_number: int = int(input("Please enter an integer to be divided: "))
    # Get the second number from the user and cast it to be a number
    second_number: int = int(input("Please enter an integer to divide by: "))
    # Calculate the result of the division and the remainder
    result: int = first_number // second_number
    remainder: int = first_number % second_number
    # Display the result to the user
    print("The result of dividing " + str(first_number) + " by " + str(second_number) + " is: " + str(result) + " with a remainder of: " + str(remainder))

if __name__ == '__main__':
    main()