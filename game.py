#!/usr/bin/python3
from map import rooms
from player import *
from items import *
from gameparser import *
from mapitem import map_print
import sys



def list_of_items(items):
    
    list_item = ("")
        
    for item in items:

        list_item = list_item + item["name"] + ", "

    list_item = list_item[:-2]

    return list_item


def print_room_items(room):

    items = list_of_items(room["items"])
    if items == (""):
        pass
    else:
        print ("There is " + items + " here.")
        print ("")
    


def print_inventory_items(items):

    items = list_of_items(inventory)
    if items == (""):
        pass
    else:
        print ("You have " + items + ".")
        print ("")

def print_room(room):

    # Display room name
    has_coffee = coffee()
    if has_coffee == True:
        print()
        print(room["name"].upper())
        print()
    # Display room description
        print(room["coffee_description"])
        print()
    else:
        print()
        print(room["name"].upper())
        print()
    # Display room description
        print(room["description"])
        print()

    print_room_items(room)

def exit_leads_to(exits, direction):

    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):

    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):

    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for items in room_items:
        print("TAKE " + items["id"].upper() + " to take a " + items["name"])

    for items in inv_items:
        print("DROP " + items["id"].upper() + " to drop your " + items["name"])

    for items in inv_items:
        if items["id"] == "map":
            print("SHOW your MAP")
    


    for items in inv_items:
        if items["id"] == "coffee":
                print("GIVE your COFFEE to ")


    print("What do you want to do?")

    print("")


def is_valid_exit(exits, chosen_exit):

    return chosen_exit in exits


def execute_go(direction):
    global current_room
      
    if current_room == rooms["Matts Office"]:
        question_master()
    elif direction in current_room["exits"]:
        
        current_room = move(current_room["exits"], direction)
        return current_room
    else:
        print("You cannot go there.")

    
def execute_show_map(inv_items):
    got_map()
    for item in inventory:
        if item["id"] == "map":
            map_print()

def execute_give(inv_items):
    give = True
    has_coffee = coffee()
    inside_tower = in_watchtower()
    print (inside_tower)
    if inside_tower == True:
        for item in inventory:
            if item["id"] == "coffee":
                inventory.remove(item)
                give = False
                return give
            else:
                give = True
            if give == False:
                print("You cannot give that item.")
            pass
            

def execute_take(item_id):
    
    for item in current_room["items"]:
        if item["id"] == item_id:
            current_room["items"].remove(item)
            inventory.append(item)
            global take
            take = True
        else:
            take = False
    if take == False:        
        print("You cannot take that item.")
    pass




    

def execute_drop(item_id):
    
    drop = False

    for item in inventory:
        if item["id"] == item_id:
            current_room["items"].append(item)
            inventory.remove(item)
            drop = True
            return drop
        else:
            drop = False
    if drop == False:
        print("You cannot drop this item.")
    pass
    
    

def execute_command(command):

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "show":
        if len(command) > 1:
            execute_show_map(command[1])
        else:
            print("Show what?")
            
    elif command[0] == "give":
        if len(command) > 1:
            execute_give(command[1])
        else:
            print("Give what?")

    elif command[0] == "use":
        if len(command) > 1:
            execute_use(command[1])
        else:
            print("Use what?")

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):

    return rooms[exits[direction]]


def coffee():

    has_coffee = False
    if item_coffee in inventory:
        has_coffee = True
        return has_coffee
    else:
        has_coffee = False
        return has_coffee

def got_map():

    has_map = False
    if item_map in inventory:
        has_map = True
        return has_map
    else:
        has_map = False
        return has_map

def got_money():

    has_money = False
    if item_lunch_money in inventory:
        has_money = True
        return has_money
    else:
        has_money = False
        return has_money

def got_flashlight():

    has_flashlight = False
    if item_flashlight in inventory:
        has_flashlight = True
        return has_flashlight
    else:
        has_flashlight = False
        return has_flashlight

def in_watchtower():

    inside_tower = False
    global current_room
    if current_room == ["Watch Tower"]:
        inside_tower = True
        return inside_tower
    else:
        inside_tower = False
        return inside_tower

def question_master():
    """
    >>> question_master()
    
    <Blank line>
    
    """
    
    complete1 = False
    complete2 = False
    complete3 = False
    complete4 = False
    
    kick = False
    
    question1 = print("Lets see, if through my questions, you can get the key?" + "\n" + "Who is Warden Kirill's favourite Star Trek Character? ")
    question2 = print("1 down with 4 to go, lets test how much you know.." + "\n" + "Can you tell me what can't be fixed?")
    question3 = print("2 down and 3 more, 2 more questions? or out the door.." + "\n" + "What is Matt Ph.D the Guard's favourite coffee? ")
    question4 = print("3 gone and 2 remain, will these questions drive you insane? " + "\n" + "What is it I needed to remember to do? ")
    #question5 = print("" + "\n" + "")    
    
    question1_answer = "spock"
    question2_answer = "lights"
    question3_answer = "latte"
    question4_answer = "buy shirt"
    #question5_answer = ""               For later use
    
    if kick == False:
        print(question1) 
        user_input = input(str("what is your answer? ") + "\n")
        if normalise_input(user_input) == question1_answer:
            complete1 = True
        else:
           kick = True
        
        #not sure if elif's are better here, they'd make it cleaner at least - Dobby        
        
        if complete1 == True:
            print(question2)
            user_input = input(str("what is your answer? ") + "\n")
            if normalise_input(user_input) == question2_answer:
                complete2 = True
            else:
                kick = True
        
                
        if complete2 == True:
            print(question3)
            user_input = input(str("what is your answer? ") + "\n")
            if normalise_input(user_input) == question3_answer:
                complete3 = True
            else:
                kick=True
        
                
        if complete3 == True:
            print(question4)
            user_input = input(str("what is your answer?") + "\n")
            if normalise_input(user_input) == question4_answer:
                complete4 = True
            else:
                kick = True
                
        if complete4 == True:
            print("You have bested me, here is the key")
    
    #We need to make sure that execute_go("east") is a thing
    #If so we might be able to make this work for other stuff 


    
    
def main():

    while True:
        print_room(current_room)
        print_inventory_items(inventory)
        command = menu(current_room["exits"], current_room["items"], inventory)
        execute_command(command)

if __name__ == "__main__":
    main()

