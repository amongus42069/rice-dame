#Josh Park, Februrary 2022, Rolling dice program
from random import randint

from time import sleep

#Import the functions randint and sleep


budget = 100

def roll_dice(wager, budget): #The actual game
    user_num = int(input("Pick a numbah between 2-12 you fool >:) "))
    print("your roll is " + str(user_num))
    first_roll = randint(1,6)
    second_roll = randint(1,6) #Randomizes roll and gets total
    total = first_roll + second_roll
    sleep(1)
    
    if user_num > 12 or user_num < 2:
        print("you cant have big number than 12")
        return 0
         #Invalid option if you have bigger number than 12
    else:
        print("Rollin.... ")
        sleep(2)
        print("house rolls " + str(first_roll) + " for first roll")
        sleep(1)
        print("house rolls " + str(second_roll) + " for second roll")
        sleep(1) #Calculates the roll
        total_roll = first_roll + second_roll
        print("the total roll is... " + str(total_roll))
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
print("welcome to da casinooooooooooooooooooooooooo")
sleep(1)
while budget > 0 :
    if input("do you want to play press q for no") == str("q"):
        break
    wager = int(input("whats your bet"))
    if wager > budget:
        print("you don't have money like that")
    else:
        budget = budget + roll_dice(wager, budget)
        print("your new budget is... " + str(budget))


        
        
    

    




    
