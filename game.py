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
        if not(item_hoover) == item:
            list_item = list_item + item["name"] + ", "

    list_item = list_item[:-2]

    return list_item


def print_room_items(room):

    items = list_of_items(room["items"])
    add_orange_shirt()
    add_coffee()

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

    has_coffee = coffee()

    has_torch = got_torch()

    has_map = got_map()
    if has_map == True:
        if current_room == rooms["Main Cell"] or current_room == rooms["Cell C"]:
            print()
            print(room["name"].upper())
            print()
    # Display room description
            print(room["map_description"])
            print()
        else: 
            print()
            print(room["name"].upper())
            print()
    # Display room description
            print(room["description"])
            print()
    elif has_coffee == True:
        if current_room == rooms["Yard"] or current_room == rooms["Visiting"]:
            print()
            print(room["name"].upper())
            print()
    # Display room description
            print(room["coffee_description"])
            print()
            remove_coffee()
        else: 
            print()
            print(room["name"].upper())
            print()
    # Display room description
            print(room["description"])
            print()
    elif has_torch == True:
        if current_room == rooms["Cell D"]:
            print()
            print(room["name"].upper())
            print()
    # Display room description
            print(room["torch_description"])
            print()
            
        else:
            print()
            print(room["name"].upper())
            print()
    # Display room description
            print(room["description"])
            print()
    else:
        print()
        print(room["name"].upper())
        print()
    # Display room description
        print(room["description"])
        print()        

    

    if not(item_hoover) in inventory:
        if current_room == rooms["Sweatshop"]:
            code_commander()

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
        if not(item_hoover) == items:
            print("TAKE " + items["id"].upper() + " to take a " + items["name"])

    for items in inv_items:
        if not(item_hoover) == items:
            print("DROP " + items["id"].upper() + " to drop your " + items["name"])

    for items in inv_items:
        if not(item_hoover) == items:
            print("EXAMINE " + items["id"].upper() + " to look at your " + items["name"])

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
    
    if direction in current_room["exits"]:
        current_room = move(current_room["exits"], direction)
        return current_room
    else:
        print("You cannot go there.")

    
def execute_show_map(inv_items):
    got_map()
    for item in inventory:
        if item["id"] == "map":
            map_print()
            

def execute_take(item_id):
    global current_room
    global take
    take = False
    for item in current_room["items"]:

        if item["id"] == "key" and current_room == rooms["Matts Office"]:
            question_master()
        else:
            if item["id"] == item_id:
                current_room["items"].remove(item)
                inventory.append(item)
                take = True
            else:
                take = False
            if take == False:        
                print("You cannot take that item.")
            pass

def execute_examine(item_id):

    for item in inventory:
        if item["id"] == item_id:
            print(item["description"])
    

def execute_drop(item_id):
    
    drop = False
    
    for item in inventory:
        if item["id"] == "soap":
            if current_room == "Showers":
                print("Nothing seems to happen, phew!")



    for item in inventory:
        if item["id"] == item_id and item["id"] != "hoover" and item["id"] != "soap":
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

    elif command[0] == "examine":
        if len(command) > 1:
            execute_examine(command[1])
        else:
            print("Examine what?")

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

def got_torch():

    has_torch = False
    if item_torch in inventory:
        has_torch = True
        return has_torch
    else:
        has_torch = False
        return has_torch

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
    print ("""\"To all intents and purposes,\nthe only way to get the key is to answer these following questions.\"""")
    question1 = "Who is Warden Kirill's favourite Star Trek Character? "
    question2 = "1 down with 4 to go, lets test how much you know.." + "\n" + "Can you tell me what can't be fixed?"
    question3 = "2 down and 3 more, 2 more questions? or out the door.." + "\n" + "What is Matt Ph.D the Guard's favourite coffee? "
    question4 = "3 gone and 2 remain, will these questions drive you insane? " + "\n" + "What is it I needed to remember to do? "
    #question5 = print("" + "\n" + "")    
    
    question1_answer = ("spock")
    question2_answer = ("lights")
    question3_answer = ("latte")
    question4_answer = ("buy shirt")
    #question5_answer = ""               For later use
    
    if kick == False:
        print(question1) 
        user_input = input(str("what is your answer? ") + "\n")
        user_input = normalise_input(user_input)
        if user_input[0] == "spock":
            complete1 = True
        else:
            kick = True
        #not sure if elif's are better here, they'd make it cleaner at least - Dobby        
        
    if complete1 == True:
        print(question2)
        user_input = input(str("what is your answer? ") + "\n")
        user_input = normalise_input(user_input)    
        if user_input[0] == question2_answer:
            complete2 = True
        else:
            kick = True
        
                
    if complete2 == True:
        print(question3)
        user_input = input(str("what is your answer? ") + "\n")
        user_input = normalise_input(user_input)
        if user_input[0] == question3_answer:
            complete3 = True
        else:
            kick=True
        
                
    if complete3 == True:
        print(question4)
        user_input = input(str("what is your answer?") + "\n")
        user_input = normalise_input(user_input)
        if (user_input[0] + " " + user_input[1]) == question4_answer:
            complete4 = True
        else:
            kick = True
                
    if complete4 == True:

        
        print("You have bested me, here is the key")
        take = True
        inventory.append(item_matt_key)
        execute_go("south")
        return take
        
    

    if kick == True:
        print("You have failed!")
        execute_go("south")
    
    #We need to make sure that execute_go("east") is a thing
    #If so we might be able to make this work for other stuff


def code_commander():
    print("print(""No one understands me in this place!"")")
    
    print("It looks like you'll have to speak to him to proceed..")
    welcomed = False
    
    while welcomed == False:
        user_input = input("What do you say? ")
        correct_input = normalise_input(user_input)
        correct_input.append("randomrandom")
        if "printhello" == correct_input[0]:
            welcomed = True
        elif correct_input[1] != "randomrandom":
            if "print hello" == correct_input[0] + " " + correct_input[1]:
                welcomed = True
                return welcomed
           
        else:
            print("He didn't seem to like that..")
            print("Try again: ")
            
    if welcomed == True:
        inventory.append(item_hoover)
        inventory.append(item_torch)
        execute_go("south")
        


def remove_coffee():
    inventory.remove(item_coffee)

def add_coffee():
    if current_room == rooms["Staff Room"]:
        if not(item_coffee) in current_room["items"] and not(item_coffee) in inventory:
            current_room["items"].append(item_coffee)

def add_orange_shirt():
    if current_room == rooms["Yard"]:
        if item_matt_key in inventory and not(item_orange_shirt) in inventory:
            current_room["items"].append(item_orange_shirt)

def add_torch():
    inventory.append(item_torch)

def win_game():
    if current_room == rooms["Reception"]:
        if item_matt_key in inventory:
            print ("The key unlocks the door and you have escaped the prison!")
            victory_print()
            sys.exit()

    if current_room == rooms["Matts Office"]:
            if item_orange_shirt in inventory:
                print ("add description here")
                victory_print()
                sys.exit()

def victory_print():

    print(" __ ___ _ _ ")
    print(" \ \ / (_) ___| |_ ___ _ __ _ _| |")
    print(" \ \ / /| |/ __| __/ _ \| '__| | | | |")
    print(" \ V / | | (__| || (_) | | | |_| |_|")
    print(" \_/ |_|\___|\__\___/|_| \__, (_)")
    print(" |___/ ")
    print(" Credits: ")
    print(" Alex Stanton ")
    print(" Baridi Innocent ")
    print(" Ken Cabrera ")
    print(" Cameron Dobby ")
    print(" Ben Lindon ")
    print(" Nathan Greenslade ")
    
def main():

    while True:
        win_game()
        print_room(current_room)
        print_inventory_items(inventory)
        command = menu(current_room["exits"], current_room["items"], inventory)
        execute_command(command)

if __name__ == "__main__":
    main()

