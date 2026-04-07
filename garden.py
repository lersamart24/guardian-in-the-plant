
import time
backpack = []
live = []

def sun_flower():
    print("right now the world is in danger because there was a outbreak in the biohazard ")
    time.sleep(0.6)
    print(" ")
    print("The outbreak as mutate the plant and human the plant now is 10x stronger and the human infect by the zoonotic bridge rafflesia(ZBR)")
    while True:
        first_step = input("What will you do (save the world/just give up): ").lower()

        if first_step == "just give up":
            print("you got the bad ending every one die")

 

        elif first_step == "save the world":
            print("you going to start the new adventure of your own")
            shovel()
            break

        else:
            print("you miss spell try again")

#NEW STUFF LATER IN FIXING MODE
def shovel():
    while True:
        choice = input(" (pick it/leave it there): ").lower()

        if choice == "pick it":
            backpack.append("apple seed")
            print("you pick it and it's an apple seed, you keep going")
            break

        elif choice == "leave it there":
            print("you miss on a very cool looking plant try")
            break

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
        if "apple seed" in backpack:
                backpack.remove("apple seed")
                print("You plant the seed and go to sleep")
                it_start()
                break
        else:
            print("you don't have the seed LIER now this time pick it up")
    
    elif plant == "no":
        print("i guess this is the good ending but IT WILL JUST END HERE SO NEXT TIME CLICK YES")
    
    else:
        print("I didn't understand, please type yes or no.")



def start():
    print("you smell somthing like rotten meat from your apple tree")
    time.sleep(0.6)
    print(" ")
    print("a rafflesia has grow on your plant it know as the parasite flower ")
    time.sleep(0.6)
    print(" ")
    print("you go out to side cure for your plant")
    time.sleep(0.6)
    print(" ")
    print("it start to rain and there was a poping sound then somthing got into your eye")
    time.sleep(0.6)
    print(" ")
    print("the seed that got in your eye is a Ruellia tuberosa it a seed that well wet will pop")
    time.sleep(0.6)
    print(" ")
    print("it pop seed won't do any harm but if it hit your eye it can make you vision bur")
    time.sleep(0.6)
    print(" ")
    print("you take the seed and put it in a jar and keep walking")
    backpack.append("Ruellia tuberosa")
    # while True
    #     water == input("you found a shadow pass by so you go closer(attack/peace)")
    #     if water == "attack":
    #         if "Ruellia tuberosa" in backpack:
    #             print("you add water to the jar and throw at the shadow ")
    #             backpack.pop("Ruellia tuberosa")
    #             print("you blind shadow and go behide the shadow and you ")
