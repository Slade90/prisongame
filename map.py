from items import *

room_matts_office = {
    "name": "Matts Office",
    
    "description": 
    """a""",

    "coffee_description":
    """a""", 

    "exits": {"south": "Hallway"},

    "items": []
}

room_kirills_office = {
    "name": "Kirills Office",

    "description":
    """a""",

    "coffee_description":
    """123""",

    "exits": {"south": "Hallway"},

    "items": []

}


room_staff_room = {
    "name": "Staff Room",

    "description":
    """a""",

    "coffee_description":
    """123""",

    "exits": {"south": "Hallway"},

    "items": [item_coffee]

}

room_toilets = {
    "name": "Toilets",

    "description":
    """a""",

    "coffee_description":
    """123""",

    "exits": {"west": "Main Cell", "east": "Showers"},

    "items": []

}

room_cell_a = {
    "name": "Cell A",

    "description":
    """a""",

    "coffee_description":
    """123""",

    "exits": {"south": "Main Cell"},

    "items": []

}

room_cell_b = {
    "name": "Cell B",

    "description":
    """a""",

    "coffee_description":
    """123""",

    "exits": {"south": "Main Cell"},

    "items": [item_lunch_money]
}

room_cell_c = {
    "name": "Cell C",

    "description":
    """a""",

    "coffee_description":
    """123""",

    "exits": {"north": "Main Cell"},

    "items": [item_map]
}


room_cell_d = {
    "name": "Cell D",

    "description":
    """a""",

    "coffee_description":
    """123""",

    "exits": {"north": "Main Cell"},

    "items": []

}

room_cell_main = {
    "name": "Main Cell",

    "description":
    """a""",

    "coffee_description":
    """123""",

    "exits": {"south": "Yard", "northwest": "Cell A", "north": "Cell B", "southwest": "Cell D", "southeast": "Cell C", "east": "Toilets", "west": "Visiting", "northeast": "Library"},

    "items": []

}

room_watch_tower = {
    "name": "Watch Tower",

    "description":
    """a""",

    "coffee_description":
    """123""",

    "exits": {"west": "Yard", "north": "Sweatshop"},

    "items": []

}

room_token_hallway = {
    "name": "Office Hallway",

    "description":
    """a""",

    "coffee_description":
    """123""",

    "exits": {"northwest": "Matts Office", "north": "Staff Room", "northeast": "Kirills Office", "south": "Visiting", "east": "Library"},

    "items": []

}

room_library = {
    "name": "Library",

    "description":
    """a""",

    "coffee_description":
    """123""",

    "exits": {"west": "Hallway", "south": "Main Cell"},

    "items": []

}

room_visiting = {
    "name": "Visiting",

    "description":
    """a""",

    "coffee_description":
    """123""",

    "exits": {"north": "Hallway", "east": "Main Cell", "west": "Reception"},

    "items": []

}

room_sweatshop = {
    "name": "Code Sweatshop",

    "description":
    """a""",

    "coffee_description":
    """123""",

    "exits": {"south": "Watch Tower", "north": "Showers"},

    "items": []

}

room_showers = {
    "name": "Showers",

    "description": 
    """a""", 

    "coffee_description":
    """123""",

    "exits": {"south": "Sweatshop", "west": "Toilets"},

    "items": []
}

room_yard = {
    "name": "Yard",

    "description": 
    """a""",

    "coffee_description":
    """123""", 

    "exits": {"north": "Main Cell", "east": "Watch Tower"},

    "items": []
}

room_reception = {
    "name": "Reception",

    "description":
    """a""",

    "coffee_description":
    """123""",

    "exits": {"east": "Visiting"},

    "items": []
}

rooms = {
    "Yard": room_yard,
    "Showers": room_showers,
    "Hallway": room_token_hallway,
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
