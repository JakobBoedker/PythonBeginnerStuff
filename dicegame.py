import sys
import random
import time

def DiceGame():
    print ("Welcome")
    print("Ready to roll the dice?")
    print("Yes/no")
    Ready = raw_input()
    if Ready == "yes":
        RandomDice = random.randrange(1,7)
        print RandomDice
    else:
        exit()

while True:
    DiceGame()
    print("Do you want to play agian?")
    print("yes/no")
    Agian = raw_input()
    if Agian == "yes":
        DiceGame()
    elif Agian == "no":
        break
        


