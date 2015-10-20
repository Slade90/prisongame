room_matts_office = {
    "name": "Matts Office",
    
    "description": 
    """a""",

    "coffee_description":
    """123""", 

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

    "items": []

}

room_toilets = {
    "name": "Toilets",

    "description":
    """a""",

    "coffee_description":
    """123""",

    "exits": {"west": "Main cell", "east": "Showers"},

    "items": []

}

room_cell_a = {
    "name": "Cell A",

    "description":
    """a""",

    "coffee_description":
    """123""",

    "exits": {"south": "Main cell"},

    "items": []

}

room_cell_b = {
    "name": "Cell B",

    "description":
    """a""",

    "coffee_description":
    """123""",

    "exits": {"south": "Main cell"},

    "items": []
}

room_cell_c = {
    "name": "Cell C",

    "description":
    """a""",

    "coffee_description":
    """123""",

    "exits": {"north": "Main cell"},

    "items": []
}


room_cell_d = {
    "name": "Cell D",

    "description":
    """a""",

    "coffee_description":
    """123""",

    "exits": {"north": "Main cell"},

    "items": []

}

room_cell_main = {
    "name": "Main Cell",

    "description":
    """a""",

    "coffee_description":
    """123""",

    "exits": {"south": "Yard", "northwest": "Cell A", "north": "Cell B", "southwest": "Cell D", "southeast": "Cell C", "east": "Toilets", "west": "Visiting"},

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

    "exits": {"northwest": "Matts office", "north": "Staff room", "northeast": "Kirills office", "south": "Visiting", "east": "Library"},

    "items": []

}

room_library = {
    "name": "Library",

    "description":
    """a""",

    "coffee_description":
    """123""",

    "exits": {"west": "Hallway", "south": "Main cell"},

    "items": []

}

room_visiting = {
    "name": "Visiting",

    "description":
    """a""",

    "coffee_description":
    """123""",

    "exits": {"north": "Hallway", "east": "Main cell", "west": "Reception"},

    "items": []

}

room_sweatshop = {
    "name": "Code Sweatshop",

    "description":
    """a""",

    "coffee_description":
    """123""",

    "exits": {"south": "Watch tower", "north": "Showers"},

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

    "exits": {"north": "Main cell", "east": "Tower"},

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
    "Watch tower": room_watch_tower,
    "Cell A": room_cell_a,
    "Cell B": room_cell_b,
    "Cell C": room_cell_c,
    "Cell D": room_cell_d,
    "Toilets": room_toilets,
    "Staff room": room_staff_room,
    "Kirills office": room_kirills_office,
    "Matts office": room_matts_office,
    "Main cell": room_cell_main,
    "Reception": room_reception,
    "Sweatshop": room_sweatshop

}
