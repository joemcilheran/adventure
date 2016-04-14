import random

def playGame():
    items = ()
    play = input("Would you like to play Lost in the Woods?(Enter: yes or no) \n")
   
    if play == "yes":
        print("You've gotten lost in the trackless wilderness. Your map home has been taken by squirrels and buried...somewhere. \n You follow a path for several hours before coming to a fork. \n ")
        start(items)
        
    else:
        print("Goodbye")
        
def start(items):
    items = (items)
    way = input("This path splits. Would you like to go East, West, or South? \n")
    if way ==  "South":
        bear(items)
    elif way == "West":
        print("Quicksand! You die! \n")  
        playGame()   
    else:
        clearing(items)
        

def bear(items):
    items = (items)
    number = random.randint(1,4)
    shovel = "shovel"
    print("You come to a clearing where a fearsome bear stands in your way. At his feet is a shovel. \n")
    action = input('Would like to speak to the bear, run away, or fight it?(Enter: speak, run, or fight) \n')
    if action == "run":
        bearWay(items)
        return items
    elif (action == "fight") and ("knife" in items):
        if number < 3:
            print("You have been eaten by the bear! You die! \n")
            playGame()   
        else:
            print("You have killed the bear with your knife! take the shovel.") 
            items.append(shovel)
            bearWay(items)
            
    elif (action == "fight") and ("knife" not in items):
        if number < 4:
            print("You have been eaten by the bear! You die! \n")
            playGame()  
        else:
            print("You have killed the bear with your knife! take the shovel.") 
            items.append(shovel)
            bearWay(items)
            
    elif (action == "speak") and ("knife" in items):
            print("You've asked the bear for the shovel, \n and, intimidated by your knife, \n he has given you the shovel. \n")        
            items.append(shovel)
            bearWay(items)
            
    else:
        if number == 1:
            print("You have been eaten by the bear! You die! \n")
            playGame() 
        else:
            print("You've asked the bear for the shovel, \n and he has given you the shovel. \n")        
            items.append(shovel)
            bearWay(items)
            
                
def bearWay(items):
    items = (items)
    way = input("paths lead off in four directions. \n Which way would you like to go?(Enter: North, South, East or West) \n")
    if  way == "South":
        knifeSpot(items)
        
    elif way == "North":
        start()
        return items
    elif way == "East":
        clearing(items)
        
    else:
        mound(items)
        
        
def clearing(items):
    items = (items)
    way = input("After a few more hours of walking, the path splits in three directions. \n Which way would you like to go(Enter North, South, or West)? \n")
    if way == "North":
        start(items)
        
    if way == "West":
        bear(items)
        
    else:
        cougar(items)
        
        
def cougar(items):
    print("The sun goes down, and the path turns dark. Out of the woods jumps a hungry cougar, who attacks you! \n")
    if "knife" in items:
        way = input("You've killed the creature an a desperate struggle. Would you like to continue on this path or go back? (Enter: forward or back) \n")
        if way == "forward":
            knifeSpot(items)
                        
        else:
            clearing(items)
            
    else:
        print("You've have been eaten by the cougar! \n")    
        playGame()
        
def mound(items):
    items = (items)
    print("You've found a mound of freshly dug dirt. This must be where the map is buried. \n")
    if "shovel" in items:
        print("With your shovel you dig up the map. Now you can find your way home! Congratulations: You've Won! \n")
        playGame()
    else:
        way = input("Sadly you have nothing with which to dig. \n Would you like to follow the path East or South? (Enter: East or South) \n")
        if way == "East":
            bear(items)
            
        else:
            knifeSpot(items)
            
            
def knifeSpot(items):
    items = (items)
    knife = "knife"
    way = input("You finally reach a wide place in the path, \n where you spot something shining in the dirt. \n It is a large knife. You pick it up. \n You see there are three paths. Which would you like to take? (Enter: East, North, or West) \n")
    items.append(knife)
    if way == "North":
        bear(items)
        
    elif way == "East":
        cougar(items)
        
    else:
        mound(items)
        
    
            
playGame()
        