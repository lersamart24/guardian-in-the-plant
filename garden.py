import time
backpack = []
live = []
print("You wake and go outside to water your plant")
time.sleep(0.6)
print(" ")
print("But when he try to water your sun flower plant there was no water left")
time.sleep(0.6)
print(" ")
while True:
    first_step = input("What will you do (go find water/just give up/get a new plant/water your plant with tea)").lower()
    if first_step == "just give up":
        print("you give up and your plant die try again")
    
    elif first_step == "get a new plant":
        print("you get a new plant can talk and it talk about how it going to take over the world")
        time.sleep(0.5)
        print(" ")
        print("so you just water it with pool water try again")
    
    
    elif first_step == "water your plant with tea":
        print("you water your plant with tea and it die.")
        time.sleep(0.5)
        print(" ")
        print("i don't know what are you thinking with you pick this try again")
        
    elif first_step == "go find water":
        print("you going to start the new adventure of your own")
        
        break

    else:
        print("you miss spell try again")



        
   
     



def shovel():
    shovel = input("you hit somthing when you trying to find water(pick it/leave it there)").lower()
        if shovel == "pick it":
            print("you pick it and you keep going")
    
        elif shovel == "leave it there":
            print("you miss on somthing very cool")
    
        else:
            print("you miss spell")
    print("")
