"""Write a program to solve this age-related riddle!

Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

Anton is 21 years old.

Beth is 6 years older than Anton.

Chen is 20 years older than Beth.

Drew is as old as Chen's age plus Anton's age.

Ethan is the same age as Chen.

Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up
 -- your solution should have the correct values!)"""

def main():
    # Define Anton's age
    anton_age = 21

    # Calculate Beth's age
    beth_age = anton_age + 6

    # Calculate Chen's age
    chen_age = beth_age + 20

    # Calculate Drew's age
    drew_age = chen_age + anton_age

    # Ethan is the same age as Chen
    ethan_age = chen_age

    # Print the ages of each person
    print(f"Anton is {anton_age} years old.")
    print(f"Beth is {beth_age} years old.")
    print(f"Chen is {chen_age} years old.")
    print(f"Drew is {drew_age} years old.")
    print(f"Ethan is {ethan_age} years old.")

if __name__ == "__main__":
    main()