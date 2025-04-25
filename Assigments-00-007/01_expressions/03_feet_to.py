# Converts feet to inches. Feet is an American unit of measurement. 
# There are 12 inches per foot. Foot is the singular, and feet is the plural.

INcHES_PER_FOOT: int = 12  # The number of inches in a   1 foot
def main():
    # Get the number of feet from the user
    feet: float = float(input("Enter the number of feet: "))

    # Calculate the number of inches
    inches: float = feet * INcHES_PER_FOOT

    # Display the result to the user
    print(str(feet) + " feet is " + str(inches) + " inches.")
    
if __name__ == '__main__':
    main()