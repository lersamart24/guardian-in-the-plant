import time
import sys
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
            biohazard_scene()
            break

        elif choice == "leave":
            print("you miss on a very cool thing")
            biohazard_scene()
            break

        else:
            print("you miss spell")


def biohazard_scene():
    print("you pass by a biohazard")
    while True:
        plant = input("do you want to go in (yes/no): ").lower()

        if plant == "yes":
            print("you go in and found an apple tree with a rafflesia around it you walk around a bit")
            start()
            break
           
        #there a bug on this one
        elif plant == "no":
            print("you step on a sundew plant it eat you")
            sys.exit()
        
        else:
            print("i didn't understand")


def start():
    print("and find a sheet of paper...")
    time.sleep(0.6)

    print("it say the only cure to ZBR is the golden apple")
    time.sleep(0.6)

    print("the rafflesia will destroy it in 2 day")
    time.sleep(0.6)

    print("the only rafflesia weakness is fire")
    time.sleep(0.6)

    print("you need to find the golden apple")
    time.sleep(0.6)

    print("you need to find a way to kill the rafflesia")
    

def fight_scene():
    while True:
            pepsii = input("what should you do 1(fight it) 2(run): ").lower()
        
            if pepsii == "1":
                print("you try to fight it but you are too weak and die")
                sys.exit()
                    
        
            elif pepsii == "2":
                print("you run away but find no survivors")
                weapon()
                break    
                
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
    while True:
        coming = input("Before you can do anything a group of infected come near you(fight/run/hide): ").lower()
    
        if coming == "fight":
            print("You try to fight it but you got no weapon and die")
            sys.exit()
    
        elif coming == "hide":
            print("You try to hide behind a tree and it work the infected leave and you come out")
            ingredirnt()
            break
    
        elif coming == "run":
            print("you maybe can outrun a 100 of zombie but not a 1000 you die")
            sys.exit()
            
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
    while True:
        survivors = input("should you investigate the camp(yes/no)").lower()
    
        if survivors == "yes":
            print("You investigate the camp and found a backpack inside that it a lighter")
            group()
            break
            
        elif survivors == "no":
            print("you didn't investigate the camp so you go out in forest and a infected kill you")
            sys.exit()
    
        else:
            print("pick between (yes/no)")
    
def group():
    print("All you need left is a stick so you pick some random stick on the ground")
    backpack.append("stick")
    print(backpack)
    while True:
        craft = input("You got a stick that is your last ingredirnt do you want to craft it (yes/no)")
    
        if craft == "yes":
            #part for checking if the backpack have the ingredirnt 
            print("you caft the flamethrower")
            backpack.append("flamethrower")
            weapon_test()
            break

    
        elif craft == "no":
            print("what are you saving that in ingredirnt for 🧐")
            weapon_test()
            break
    
        else:
            print("you miss spell")

    

def weapon_test():
    print("you got the flamethrower but you want to test if it work")
    time.sleep(0.6)
    print(" ")
    print("so you find a group of infected and try to use it")
    time.sleep(0.6)
    print(" ")
    while True:
        test = input("do you want to test it (yes/no)").lower()
    
        if test == "yes":
            if "flamethrower" in backpack:
                print("you test it and it work you burn the infected and you are ready to fight the rafflesia")
                first_round()
                break
            else:
                print("you don't have the flamethrower so you can't test it and the infected kill you")
                sys.exit()
            
        elif test == "no":
            print("you don't test it and go to fight the rafflesia so you don't now how to use it and die")
            sys.exit()

        else:
            print("you miss spell")

def first_round():
    print("you go to the biohazard again to fight the rafflesia")
    time.sleep(0.6)
    print(" ")
    print("it grow bigger and stronger and the golden apple is almost destroyed the time right now is 11:00 AM")
    time.sleep(0.6)
    print(" ")
    while True:
        fight = input("do you want to fight it now (yes/no)").lower()
    
        if fight == "yes":
            print("you try to fight it but you are not strong enough and die")
            sys.exit()

            
        elif fight == "no":
            print("your thinking a plan right now but the there no time left the rafflesia destroy the golden apple and will everyone die")
            close()
            break

        else:   
            print("you miss spell")


def close():
    print("you go to fight the rafflesia but the rafflesia it start to become stronger")
    time.sleep(0.6)
    print(" ")
    print("the rafflesia fully grow and the golden apple is destroy")
    time.sleep(0.6)
    print(" ")
    print("you don't know what to do so you just rush in")
    time.sleep(0.6)
    print(" ")
    while True:
        rush = input("you rush in to kill but it try to grab you what should you do 1(burn it) 2 move out)(1/2)").lower()
    
        if rush == "1":
            print("you try to burn it but the flamethrower can't burn it fast enough and the rafflesia grab you and you die")
            sys.exit()
            
        elif rush == "2":
            print("you try to move out of the way and it work the rafflesia miss you got a chance to stike")
            teammate()
            break
            
        else:
            print("pick between 1 or 2 try again")
            
def teammate():
    print("you got a chance to strike the rafflesia but you are not strong enough to kill it alone")      
    time.sleep(0.6)
    print(" ")
    print("you need to find a teammate to help you fight the rafflesia")
    time.sleep(0.6)
    print(" ")   
    while True:
        teammate = input("you retreat to find a survivor to help you fight the rafflesia do you want to look for a teammate (yes/no)").lower()
        
        if teammate == "yes":
            print("you look for a trace of survior and you find footprint you follow it and find a cave")
            cave()
            break
            
        elif teammate == "no":
            print("you don't look for a teammate and go back to fight the rafflesia but you are not strong enough and die")
            sys.exit()
            
        else:
            print("pick between yes or no try again")
            
def cave():
    print("you use the flamethrower to light up a torch located where the footprint")
    time.sleep(0.6)
    print(" ")
    print("you follow the torch light and find a survivor hiding in the cave")
    time.sleep(0.6)
    print(" ")
    print("the survivor try to attack you but try to talk to him and find out he not alone there is a group of survivor hiding in the cave")
    time.sleep(0.6)
    print(" ")
    print("you talk to the survivor and find out they are also trying to find a way to kill the rafflesia and they want to join you to fight the rafflesia it been 1 and a half day")
    time.sleep(0.6)
    print(" ")
    while True:
        number = input("you do want to join them (yes/no)").lower()
        
        if number == "yes":
            print("you join the survior to fight the rafflesia together")
            team()
            break
        
        elif number == "no":
            print("you didn't join the survior and go back alone you got killed by the rafflesia")
            sys.exit()
        
        else:
            print("pick between yes or no try again")
            
            
            
def team():
    print("you had a team to fight the rafflesia but the rafflesia almost destroy the golden apple you need to fight it now the time right now is 1:00 AM")
    time.sleep(0.6)
    print(" ")
    time.sleep(0.6)
    print("one hr pass the rafflesia has full destroy the golden apple the virus has virus spread all around the world")
    time.sleep(0.6)
    print(" ")
    while True:
        fight = input("you reach the biohazrd and the rafflesia is ready for you(go in/stay back)").lower()
        
        if fight == "go in":
            print("you go in and fight the rafflesia together you burn it eye you is blind for a second")
            time.sleep(0.6)
            print(" ")
            print("you take the chance to strike the rafflesia and you did it you hit it in the head")
            last_round()
            break
            
        elif fight == "stay back":
          print("you stay in the back but you trip on a rock a you land on your head and die")
          sys.exit()
        
        
        else:
          print("you miss spell")
    
    
    
def last_round():
     print("the rafflesia is not very weak it call all the infected")
     time.sleep(0.6)
     print(" ")
     print("all your teammate your injured so you got to do it my yourself")
     time.sleep(0.6)
     print(" ")
     while True:
      swam = input("all the infected is in one place what should you do 1 rush in 2 defend your teammate (1/2)")
      
      if swam == "1":
        print("you rush in kill and infected in your way with your weapon")
        last_run()
        break
      
      
      elif swam == "2":
        print("you project your teammate but they one be getting up soon the zombie overwhelmed and die ")
        sys.exit()
      
      else:
        print("pick between 1/2")
        
      
      
def last_run():
  print("you keep running unit you ran out of fual")
  time.sleep(0.6)
  print(" ")
  print("you reach the rafflesia but you ran out of fual")
  time.sleep(0.6)
  print(" ")
  while True:
    HIT = input("you infront of the rafflesia you got 2 choice ONE (you use the stick part of the flamethrow as a sword)TWO(use other plan) (1/2)")
    
    if HIT == "1":
      print("you rush in and jump on the rafflesia and stab it in the middle but it didn't work and the infected kill you")
      sys.exit()
      
     #BUG HERE FIXING 
    elif HIT == "2":
      print("You need to come up with something you see a puddle of water that gave you a idea")
      time.sleep(0.6)
      print(" ")
      print("you use the jar that store your pine tree sap")
      nothing()
      break
      
      
    else:
      print("Pick 1 or 2")
    
    
def nothing():
    while True:
        
        if "Ruellia tuberosa" in backpack:
            print("you store the water in a jar and told the Ruellia tuberosa in")
            time.sleep(0.6)
            print(" ")
            print("You jump on to the rafflesia and stick the jar inside the rafflesia the rafflesia explode and you win but the golden apple is destroy")
            win()
            break
    
        elif "Ruellia tuberosa" not in backpack:
            print("you didn't have the Ruellia tuberosa and you can't do anything with a jar of water so sadly the rafflesia kill you")  
            sys.exit()
   
def win():
     print("luckily there one golden apple seed one the ground you plant it and it grow into a golden apple tree and save the world")  
   

  
   
   
         
alive = intro()

if alive:
    shovel()
    biohazard_scene()
    fight_scene()
