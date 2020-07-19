from creature import Creature
from item import Item
from location import Location

# Process paths.txt file
def process_locations(source):
    locs = []
    try:
        with open(source) as file:
            lines = file.readlines()
            if len(lines) == 0:
                print("The game cannot run without any rooms :(")
                exit()

            for line in lines:
                # Each parameter is seperate by >
                info = line.split(" > ")
                # Make sure the info has three elements, otherwise, pass to exception
                if len(info) == 3:
                    start_name = info[0]
                    dire = info[1]
                    dest_name = info[2].strip()

                    # Look for the location in the list, return false if not
                    start_location=look_for_loc(start_name,locs)
                    dest_location=look_for_loc(dest_name,locs)

                    # Add location into the list if it not already in it
                    if not start_location:
                        start_location = Location(start_name)
                        locs.append(start_location)
                    if not dest_location:
                        dest_location = Location(dest_name)
                        locs.append(dest_location)

                    # Add path to a list of paths
                    start_location.add_path(dire, dest_location)

    except FileNotFoundError:
        print("You have specified an invalid configuration file.")
        exit()
    return locs

# Check the target is in the locations list or not
def look_for_loc(target, locations):
    for loc in locations:
        if loc.get_name() == target:
            return loc
    return False

# Process item.txt file
def process_items(source, locations):
    items = []
    try:
        with open(source) as file:
            lines = file.readlines()
            for line in lines:
                info = line.split(" | ")
                if len(info) == 5:
                    short_name = info[0]
                    full_name = info[1]
                    desc = info[2]
                    terror_rating = info[3]
                    location = info[4].strip()

                    # Store this five parameter into the Item class and add to the item list
                    item = Item(short_name, full_name, desc, terror_rating)
                    items.append(item)

                    # If an item is dropped at a location
                    for loc in locations:
                        if loc.get_name() == location:
                            loc.add_item(item)

    except FileNotFoundError:
        print("You have specified an invalid configuration file.")
        exit()
    return items

# Input a list of location objects and process chasers.txt file
def process_creatures(source, locations):
    creatures = []
    try:
        with open(source) as file:
            lines = file.readlines()

            if len(lines) == 0:
                print("There is nothing chasing you!")
                exit()

            for line in lines:
                info = line.split(" | ")
                if len(info) == 5:
                    name = info[0]
                    desc = info[1]
                    terror_rating = info[2]
                    location = info[3].strip()
                    dire = info[4].strip().lower()

                    # Store this five parameter into the Creature class and add to the creature list
                    creature = Creature(name, terror_rating, dire=dire, desc=desc)
                    creatures.append(creature)

                    # Add creature to locations
                    for loc in locations:
                        if loc.get_name() == location:
                            creature.set_location(loc)
                            loc.add_creature(creature)

    except FileNotFoundError:
        print("You have specified an invalid configuration file.")
        exit()
    return creatures

# Input a list of location which allow user to use flee command and process exit.txt file
def process_exits(source, locations):
    try:
        with open(source) as file:
            for line in file:
                line = line.strip()

                # Exit at the location on the list
                for loc in locations:
                    if loc.get_name() == line:
                        loc.set_exit()

    except FileNotFoundError:
        print("You have specified an invalid configuration file.")
        exit()


