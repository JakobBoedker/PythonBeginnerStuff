import sys
import random

def GuessingGame():
    print ("Welcome to guess the number!\n")

    number = random.randrange(1,71)
    print("Guess a number between 1 - 70")
    while True:
        UserInput = input()

        if number == UserInput:
            print("YOU GUESSED RIGHT!")
            exit()

        if number < UserInput:
            print("Guess lower")
            UserInput

        if number > UserInput:
            print("Guess higher")
            UserInput

GuessingGame()
