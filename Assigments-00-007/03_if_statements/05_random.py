"""Print 10 random numbers in the range 1 to 100."""
import random  # Import the random module to generate random numbers
N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100
def main():
    # Generate and print 10 random numbers in the range 1 to 100
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE))  # Print a random number between 1 and 100
if __name__ == "__main__":
    main()  # Call the main function when the script is run
            