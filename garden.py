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
    while True:
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

    while True:
        plant = input("do you want to go in (yes/no): ").lower()

        if plant == "yes":
            print("you found an apple tree with a rafflesia around it")
            start()
            break

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
    while True:
        pepsii = input("what should you do 1(fight it) 2(run): ")

        if pepsii == "1":
            print("you try to fight it but you are too weak and die")
            

        elif pepsii == "2":
            print("you run away but find no survivors")
            break

        else:
            print("i didn't understand try again")


# ---- GAME START ----

alive = intro()

if alive:
    shovel()
    biohazard_scene()
    fight_scene()
