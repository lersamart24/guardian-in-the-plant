import time

backpack = []


def intro():
    print("right now the world is in danger because there was a outbreak in the biohazard.")
    time.sleep(0.6)
    print("the outbreak has mutate the plant and human the plant now is 10x stronger")
    print("humans are infected by the zoonotic bridge rafflesia (ZBR)")
    alive = True

    while True:
        first_step = input("everything start at 12:00 PM what will you do (save the world / do nothing): ").lower()

        if first_step == "do nothing":
            print("you got the bad ending every one die")
            alive = False
            break

        elif first_step == "save the world":
            print("you start your journey...")
            alive = True
            break

        else:
            print("you miss spell try again")

    return alive


def shovel():
    choice = input("you found a Ruellia tuberosa (pick/leave): ").lower()

        if choice == "pick":
            print("you pick it and store it in your backpack")
            backpack.append("Ruellia tuberosa")
            break

        elif choice == "leave":
            print("you miss on a very cool thing")
            break

        else:
            print("you miss spell")


def biohazard_scene():
    print("you pass by a biohazard")

    plant = input("do you want to go in (yes/no): ").lower()

    if plant == "yes":
        print("you found an apple tree with a rafflesia around it")
        start()
            

    elif plant == "no":
        print("you step on a sundew plant it eat you try again")

    else:
        print("i didn't understand")


def start():
    print("you find a sheet of paper...")
    time.sleep(0.6)

    print("it say the only cure to ZBR is the golden apple")
    time.sleep(0.6)

    print("the rafflesia will destroy it in 2 day")
    time.sleep(0.6)

    print("the only rafflesia weakness is fire")


def fight_scene():
    pepsii = input("what should you do 1(fight it) 2(run): ").lower()

    if pepsii == "1":
        print("you try to fight it but you are too weak and die")
            

    elif pepsii == "2":
        print("you run away but find no survivors")
        weapon()
            
        
    else:
        print("Pick 1 or 2 try again")



def weapon():
    print("you did find any surviors so you decide to craft some weapon")
    time.sleep(0.6)   
    print( )
    print("you go out to find some ingredient")
    time.sleep(0.6)   
    print( )
    print("you know the rafflesia is weak to fire so you need ingredirnt to make waepon")
    time.sleep(0.6)   
    print( )
    coming = input("Before you can do anything a group of infected come near you(fight/run/hide): ").lower()

    if coming == "fight":
        print("You try to fight it but you got no weapon and die")

    elif coming == "hide":
        print("You try to hide behind a tree and it work the infected leave and you come out")
        ingredirnt()
        

    elif coming == "run":
        print("you maybe can outrun a 100 of zombie but not a 1000 you die")
        
    else:
        print("pick between fight/run/hide")




def ingredirnt():
    print("After you run away from the infected you found a pine tree sap")
    time.sleep(0.6)   
    print(" ")    
    print("you pick the sap for the ingredirnt and store it in a jar")
    time.sleep(0.6)   
    print(" ")    
    backpack.append("sap in a jar")
    print(backpack)
    time.sleep(0.6)   
    print(" ")
    print("the ingredirnt for a fire weapon is")
    time.sleep(0.6)   
    print(" ")
    print("(pine tree sap/lighter/stick)")
    time.sleep(0.6)   
    print(" ")
    print("So you got to search for a lighter")
    time.sleep(0.6)   
    print(" ")
    print("You didn't find anything but a abandoned camp")
    survivors = input("should you investigate the camp(yes/no)").lower()
    if survivors == "yes":
        print("You investigate the camp and found a backpack inside that it a lighter")
        group():
    
    elif survivors == "no":
        print("you didn't investigate the camp so you go out in forest and a infected")

    else:
        print("you miss spell")

def group():
    craft = input("You got the lighter that is your last ingredirnt do you want to craft it (yes/no)")

    if craft == "yes":
        #part for checking if the backpack have the ingredirnt 
        print("you caft the flamethrower")

    elif craft == "no":
        print("what are you saving that in ingredirnt for 🧐")

    else:
        print("you miss spell")

    

alive = intro()

if alive:
    shovel()
    biohazard_scene()
    fight_scene()



