"""Write a program which asks the user how tall they are and prints 
whether or not they're taller than a pre-specified minimum height."""
MINIMUM_HEIGHT = 1.5  # Minimum height in meters
def main():
    # Get the user's height in meters
    user_height = float(input("How tall are you in meters? "))

    # Check if the user is taller than the minimum height
    if user_height >= MINIMUM_HEIGHT:
        print("You are taller than " + str(MINIMUM_HEIGHT) + " meters.")
    else:
        print("You are shorter than " + str(MINIMUM_HEIGHT) + " meters.")
        
if __name__ == '__main__':
    main()        
