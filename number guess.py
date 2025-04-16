#!/usr/bin/ env/python
import random

def main():
    """start a number guessing game between 1 - 100."""
    print("Guess the number!")

    x = random.randint(1 , 100)
    guess = None

    while x != guess:

        guess = int(input("pivk a number between 1 to 100: "))
         
        if x == guess:
           print("you genius!")
        elif x > guess:
            print("Try a biggest number.")
        elif x < guess:
            print("try a smaller number.")
main()