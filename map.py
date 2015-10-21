from items import *

room_matts_office = {
    "name": "Matts Office",
    
    "description": 
    """You have entered Matt Morgan\'s office.\nHe is sat at his desk trying to look busy, he vaguely acknowledges\nyour presence.""" """and says \"To all intents and purposes,\nthe only way to get the key is to answer these following questions.\"""", 

    "exits": {"south": "Token Hallway"},

    "items": [item_matt_key]
}

room_kirills_office = {
    "name": "Kirills Office",

    "description":
    """You have entered Kirill\'s office. His PC seems to be locked as he is not currently here.\nYou can\'t help but notice the incredible amount of Star Trek merchandise scattered around the room.""",
    
    "exits": {"south": "Token Hallway"},

    "items": [item_spock]

}


room_staff_room = {
    "name": "Staff Room",

    "description":
    """You have entered the staff room. There is a coffee machine at the back of the room that requires money for it to work.""",

    "exits": {"south": "Token Hallway"},

    "items": [item_coffee]

}

room_toilets = {
    "name": "Toilets",

    "description":
    """You have entered the toilets. The only clean thing in here seems to be the bar of soap!""",

    "exits": {"west": "Main Cell", "east": "Showers"},

    "items": []

}

room_cell_a = {
    "name": "Cell A",

    "description":
    """You have woken up in a dark empty cell which you will call home for the next three years unless you escape from this hell hole.\n If only you didn\'t drop that map in one of the cells!""",

    "description_2":
    """You have entered the cell that you woke up in. There is nothing in here that you could use.""",

    "exits": {"south": "Main Cell"},

    "items": []

}

room_cell_b = {
    "name": "Cell B",

    "description":
    """You have entered Cell B. A prisoner is sat in a corner nursing a warm cup of coffee.""",

    "exits": {"south": "Main Cell"},

    "items": []
}

room_cell_c = {
    "name": "Cell C",

    "description":
    """You have entered Cell C. You notice that there is a map on the floor in the corner of your eye.""",

    "map_description":
    """You have entered cell C. Now that you have taken the map, this room is completely empty.""",

    "exits": {"north": "Main Cell"},

    "items": [item_map]
}


room_cell_d = {
    "name": "Cell D",

    "description":
    """You have entered Cell D. There is a message on the wall but it
is completely unreadable as the room is in complete darkness.""",

    "torch_description":
    """You have entered Cell D. The room is completely dark, so you use the 
torch in your inventory to light up the room which reveals a message on the wall.
It says: \"WE CAN\'T FIX THOSE LIGHTS! THOSE BLOODY LIGHTS!\"""",

    "exits": {"north": "Main Cell"},

    "items": []

}

room_cell_main = {
    "name": "Main Cell",

    "description":
    """You have now entered the main cell. 
This seems to be the hub of the prison where all the cells are connected to one another.
Matt Ph.D. the guard has spotted you, you try to greet him but he ignorantly shrugs 
you away and mutters 
\"12 hour shift on the guard tower and I haven\'t even had a coffee, damn it!
I can only drink coffee in the staff room or Kirill will kill me! 
What a joke...How can I get one?\"""",
   
    "map_description":
    """You have now entered the main cell. 
This seems to be the hub of the prison where all the cells are connected to one another.
The guard that was here earlier is no longer here, he must have gone up to the guard tower.""",

    "exits": {"south": "Yard", "northwest": "Cell A", "northeast": "Library", "north": "Cell B", "southwest": "Cell D", "southeast": "Cell C", "east": "Toilets", "west": "Visiting"},

    "items": []

}

room_watch_tower = {
    "name": "Watch Tower",

    "description":
    """You have entered the guard tower. 
From here you can view the entire prison and all of the possible exits.
Matt Ph.D. the guard is here and he is still grouchy about not having a coffee.""",

    "coffee_description":
    """You have entered the guard tower.
Matt Ph.D. the guard\'s face lights up with glee as he notices
the coffee that you are carrying.\n He snatches the coffee from 
you before you can even offer it and says \"A LATTE, MY FAVOURITE! 
HOW DID YOU KNOW?\"
""",

    "exits": {"west": "Yard", "north": "Sweatshop"},

    "items": []

}

room_token_hallway = {
    "name": "Token Hallway",

    "description":
    """You have entered the token hallway. There is nothing here except for three
doors, the Staff Room, Kirill\'s Office and Matt\'s office.
There is a sign on Matt\'s door that says: 
\"Do not enter unless you have important information for me.\"""",

    "other_description":
    """123""",

    "exits": {"northwest": "Matts Office", "north": "Staff Room", "northeast": "Kirills Office", "south": "Visiting", "east": "Library"},

    "items": []

}

room_library = {
    "name": "Library",

    "description":
    """You have entered the library. There are shelves full of books about programming for as far as your eyes can see.""",

    "other_description":
    """123""",

    "exits": {"west": "Token Hallway", "south": "Main Cell"},

    "items": [item_matts_diary]

}

room_visiting = {
    "name": "Visiting",

    "description":
    """You have entered the Visiting room, there are no visitors for you, what a surprise...""",

    "coffee_description":
    """Kirill has spotted you with coffee outside of the staff room. \"You shouldn\'t have that in here! Give it to me now!\"\n You lose the coffee, better not let him catch you again!""",

    "exits": {"north": "Token Hallway", "east": "Main Cell", "west": "Reception"},

    "items": []

}

room_sweatshop = {
    "name": "Code Sweatshop",

    "description":
    """Before you lies a horrific site, rows and rows of sweaty men dressed in ragged star wars t-shirts being forced to code in assembly language. Who is capable of such cruelty to Star Wars fans?\n According to some of the profanity coming from the poor soul\'s mouths, Warden Kirill. There appears to be a Code Commander that is nursing a flashlight while patrolling around the sweatshop.\n You say hello but he responds with \"Print(\"SYNTAX ERROR, CANNOT UNDERSTAND\")""",

    "description_success":
    """He seems to understand you! \"Finally! Someone that speaks my language with proper syntax!\n Hello friend, is there anything I can help you with?\"""",

    "exits": {"south": "Watch Tower", "north": "Showers"},

    "items": []

}

room_showers = {
    "name": "Showers",

    "description": 
    """You have now entered the shower room. There is nothing in here but you can hear a mysterious tapping sound coming from the south.""", 

    "exits": {"south": "Sweatshop", "west": "Toilets"},

    "items": []
}

room_yard = {
    "name": "Yard",

    "description": 
    """You have entered the yard area, you can tell that most of the gym equipment has never been used.\n There isn\'t anything useful to pick up here.""",

    "coffee_description":
    """Kirill has spotted you with coffee outside of the staff room. \"You shouldn\'t have that in here! Give it to me now!\"\n You lose the coffee, better not let him catch you again!""", 

    "exits": {"north": "Main Cell", "east": "Watch Tower"},

    "items": []
}

room_reception = {
    "name": "Reception",

    "description":
    """You have entered the Reception. There is a crazy looking receptionist behind the desk that is currently shopping for catnip.\n Doesn\'t look like you can leave through this exit without a key.""",

    "description_win":
    """You have entered the Reception. You now have the key to leave this place and to be free for the rest of your days. RUN YOU FOOL!""",

    "exits": {"east": "Visiting"},

    "items": []
}

rooms = {
    "Yard": room_yard,
    "Showers": room_showers,
    "Token Hallway": room_token_hallway,
    "Visiting": room_visiting,
    "Library": room_library,
    "Watch Tower": room_watch_tower,
    "Cell A": room_cell_a,
    "Cell B": room_cell_b,
    "Cell C": room_cell_c,
    "Cell D": room_cell_d,
    "Toilets": room_toilets,
    "Staff Room": room_staff_room,
    "Kirills Office": room_kirills_office,
    "Matts Office": room_matts_office,
    "Main Cell": room_cell_main,
    "Reception": room_reception,
    "Sweatshop": room_sweatshop

}
