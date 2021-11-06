import random
number=random.randint(1,9)
chance=0
print("NUMBER GUSSEING GAME")
print("GUESS THE NUMBER (BETWEEN 1 TO 9)")

while(chance <4):
    string=int(input("ENTER YOUR GUESS:-"))
    if(number==string):
        print("YOU WON! CONGRATS...")
        break 
    elif(string<number):
        print("YOUR GUESS IS LOW TRY AGAIN!")
       
    elif(string>number):
        print("YOUR GUESS IS HIGH TRY AGAIN!")

    chance=chance+1
   

