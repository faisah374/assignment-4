#Write a program which asks the user what their favorite animal is, and then always responds with 
# "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).
#Here's a sample run of the program 
# (user input is in bold italics - note the space between the prompt and the user input!)

def main():
    # Ask the user for their favorite animal in bold italics
    favorite_animal = input("\033[1;3m What is your favorite animal ____?\033[0m ")
    # Respond with the user's favorite animal in bold italics
    print(f"My favorite animal is also {favorite_animal}!")

if __name__ == "__main__":
    main()   