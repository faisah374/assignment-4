#Ask the user for a number and print its square (the product of the number times itself).

#Here's a sample run of the program (user input is in bold italics):

#Type a number to see its square: 4

#4.0 squared is 16.0

def main():
    # Ask the user for a number in bold italics
    number = float(input("\033[1;3m Type a number to see its square: \033[0m "))
    # Calculate the square of the number
    square = number ** 2
    # Print the result in bold italics
    print(f"\033[1;3m {number} squared is {square}\033[0m")
if __name__ == "__main__":
    main()    
