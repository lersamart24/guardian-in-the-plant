
import time
backpack = []
live = []

def sun_flower():
    while True:
        first_step = input("What will you do (go find water/just give up/get a new plant/water your plant with tea): ").lower()

        if first_step == "just give up":
            print("you give up and your plant die try again")

        elif first_step == "get a new plant":
            print("you get a new plant can talk and it talk about how it going to take over the world")
            time.sleep(0.5)
            print()
            print("so you just water it with pool water try again")

        elif first_step == "water your plant with tea":
            print("you water your plant with tea and it die.")
            time.sleep(0.5)
            print()
            print("i don't know what are you thinking with you pick this try again")

        elif first_step == "go find water":
            print("you going to start the new adventure of your own")
            shovel()
            break

        else:
            print("you miss spell try again")


def shovel():
    while True:
        choice = input("you hit something when you trying to find water (pick it/leave it there): ").lower()

        if choice == "pick it":
            backpack.append("apple seed")
            print("you pick it and it's an apple seed, you keep going")
            break

        elif choice == "leave it there":
            print("you miss on a very cool looking plant try again")

        else:
            print("you miss spell")


def it_start():
    print("The apple tree starts growing...")
    

sun_flower()

print("You open your backpack to plant the apple seed")
print(backpack)

while True:
    plant = input("Do you want to plant the apple seed (yes/no): ").lower()
    
    if plant == "yes":
            print("you plant the apple seed")
            backpack.remove("apple seed")
            print("You plant the seed and go to sleep")
            it_start()
            break
        
    
    elif plant == "no":
        print("i guess this is the good ending but IT WILL JUST END HERE SO NEXT TIME CLICK YES")
    
    else:
        print("I didn't understand, please type yes or no.")
