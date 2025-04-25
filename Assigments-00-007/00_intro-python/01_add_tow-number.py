def main():
    # This is a simple program to add two numbers
    # Get the first number from the user
    num1 = input("Enter first number: ")
    num1=int(num1)

    # Get the second number from the user
    num2 = input("Enter second number: ")
    num2=int(num2)
    # Add the two numbers
    sum = num1 + num2
    # Print the result
    print("The sum of the number is", num1, "and", num2, "is", sum)
if __name__ == "__main__":
   main()