""""Write a program that prints out the calls for a spaceship that is about to launch.
 Countdown from 10 to 1 and then output Liftoff!"""

import time
def countdown(n):
    # Print the countdown from n to 1
    for i in range(n, 0, -1):
        print(i)
        time.sleep(1)  # Pause for 1 second between counts
    print("Liftoff!")
def main():
    print (countdown(10))
if __name__ == '__main__':
    main()      


