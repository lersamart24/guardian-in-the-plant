
import time
backpack = []
live = []

def sun_flower():
    print("right now the world is in danger because there was a outbreak in the biohazard ")
    time.sleep(0.6)
    print(" ")
    print("The outbreak as mutate the plant and human the plant now is 10x stronger and the human infect by the zoonotic bridge rafflesia(ZBR)")
    while True:
        first_step = input("what will you do(save the world/do nothing): ").lower()

        if first_step == "do nothing":
            print("you got the bad ending every one die")
            break

 

        elif first_step == "save the world":
            print("You explore trying to find somthing that will help you with your adventure")
            shovel()
            break

        else:
            print("you miss spell try again")

#NEW STUFF LATER IN FIXING MODE
def shovel():
    while True:
        choice = input("while your trying to find somthing you found a Ruellia tuberosa(pick/leave)").lower()
            

        if choice == "pick":
            print("you pick it and it's an Ruellia tuberosa, you store it in your backpack and  keep going")
            backpack.append("Ruellia tuberosa")
            break

        
        elif choice == "leave":
            print("you miss on a very cool looking thing try")
            break

        else:
            print("you miss spell")


def start():
    print("beside that you found a sheet of paper")
    time.sleep(0.6)
    print(" ")
    print("it say (Since the breakout i have been search and found out) ")
    time.sleep(0.6)
    print(" ")
    print("What the only cure to the ZBR is the golden apple but the rafflesia going to kill it in 2 day")
    time.sleep(0.6)
    print(" ")
    print("the only rafflesia weakness is fire ")
    print(" ")
    time.sleep(0.6)


sun_flower()

print("you pass by a biohazrd")
while True:
    plant = input("Do you want to go and check what in it (yes/no): ").lower()
    
    if plant == "yes":
                print("You go in to check and found a apple tree with a rafflesia in wrap around the trunk")
                start()
                break
        
    
    elif plant == "no":
        print("You didn't go in and you step on a sundew plant it eat you try again ")
        
    else:
        print("I didn't understand, please type yes or no.")
