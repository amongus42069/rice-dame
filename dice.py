#Josh Park, Februrary 2022, Rolling dice program
from random import randint

from time import sleep

#Import the functions randint and sleep


budget = 100

def roll_dice(wager, budget): #The actual game
    user_num = int(input("Pick a numbah between 2-12 you fool >:) "))
    print(user_num)
    first_roll = randint(1,6)
    second_roll = randint(1,6) #Randomizes roll and gets total
    total = first_roll + second_roll
    sleep(1)
    
    if user_num > 12:
        print("you cant have big number than 12")
        return #Invalid option if you have bigger number than 12
    else:
        print("Rollin.... ")
        sleep(2)
        print(first_roll)
        sleep(1)
        print(second_roll)
        sleep(1) #Calculates the roll
        total_roll = first_roll + second_roll
        print(total_roll)
        print("Result... ")
        sleep(1)
        if user_num == total:
            print("you schooled me you fool ¯\_(ツ)_/¯")
            wager = wager * 12
            return wager
            
        else:
            print("get schooled you fool o7") #Responses that we get from winnin or losin
            return -wager


x = 0

while budget > 0 or choice == "q":
    wager = int(input("whats your bet"))
    budget = budget + roll_dice(wager, budget)
    print(budget)


        
        
    

    




    
