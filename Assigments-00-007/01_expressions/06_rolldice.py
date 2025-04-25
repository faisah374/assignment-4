
# Simulate rolling two dice, and prints results of each roll as well as the total.
# The program will continue to roll the dice until the user decides to stop.
# The user is prompted to enter 'y' or 'n' to continue or stop the program.
# The program uses the random module to generate random numbers for the dice rolls.

import random

NUMBER_OF_SIDES: int = 6  # The number of sides on the dice
def main():
    # Initialize the variable to control the loop
    continue_rolling: str = 'y'

    # Continue rolling the dice until the user decides to stop
    while continue_rolling.lower() == 'y':
        # Roll the dice and store the results in variables
        die1: int = random.randint(1, NUMBER_OF_SIDES)
        die2: int = random.randint(1, NUMBER_OF_SIDES)

        # Calculate the total of the two dice rolls
        total: int = die1 + die2

        # Display the results to the user
        print("Die 1: " + str(die1) + ", Die 2: " + str(die2) + ", Total: " + str(total))

        # Ask the user if they want to roll again
        continue_rolling = input("Do you want to roll again? (y/n): ")

if __name__ == '__main__':
    main()
 
