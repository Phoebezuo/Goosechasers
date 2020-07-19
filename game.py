import sys
from creature import Creature
from item import Item
from location import Location
from preprocessing import process_locations, process_exits, process_items, process_creatures

### All functions used in the main body
# The left side is padded 16 characters in width
def help():
    print("{:16}- Shows some available commands.".format("HELP"))
    print("{:16}- Lists all the items in your inventory.".format("INV"))
    print("{:16}- Takes an item from your current location.".format("TAKE <ITEM>"))
    print("{:16}- Drops an item at your current location.".format("DROP <ITEM>"))
    print()
    print("{:16}- Lets you see the map/location again.".format("LOOK or L"))
    print("{:16}- Lets you see an item in more detail.".format("LOOK <ITEM>"))
    print("{:16}- Sometimes, you just have to admire the feathers.".format("LOOK ME"))
    print("{:16}- Sizes up a nearby creature.".format("LOOK <CREATURE>"))
    print("{:16}- Shows a list of all items in the room.".format("LOOK HERE"))
    print()
    print("{:16}- Moves you to the northwest.".format("NORTHWEST or NW"))
    print("{:16}- Moves you to the north.".format("NORTH or N"))
    print("{:16}- Moves you to the northeast.".format("NORTHEAST or NE"))
    print("{:16}- Moves you to the east.".format("EAST or E "))
    print()
    print("{:16}- Moves you to the southeast.".format("SOUTHEAST or SE"))
    print("{:16}- Moves you to the south.".format("SOUTH or S"))
    print("{:16}- Moves you to the southwest.".format("SOUTHWEST or SW"))
    print("{:16}- Moves you to the west.".format("WEST or W"))
    print()
    print("{:16}- Attempt to flee from your current location.".format("FLEE"))
    print("{:16}- Attempt to scare off all creatures in the same location.".format("HONK or Y"))
    print("{:16}- Do nothing. All other creatures will move around you.".format("WAIT"))
    print("{:16}- Ends the game. No questions asked.".format("QUIT"))

# Prints the player's inventory
def inv():
    # All the items you have carried
    items = me.get_items()
    if len(items) == 0:
        print("You are carrying nothing.")
    else:
        if len(items) == 1:
            print("You, a goose, are carrying the following item:")
        else: 
            print("You, a goose, are carrying the following items:")
        for item in items:
            # Only each item's item_name is printed
            print(" - " + item.get_item_name())

# To check this location has creature or not
def has_creature(dir, paths):
    location = paths.get(dir)
    if len(location.get_creatures()) > 0:
        return True
    else:
        return False

# Display the location you are currently in
def look():
    line1 = [''] * 5
    line2 = [''] * 5
    line3 = [''] * 5
    line4 = [''] * 5
    line5 = [''] * 5
    line1[1] += ' '
    line1[3] += ' '
    line2[0] += '   '
    line2[4] += '   '
    line4[0] += '   '
    line4[4] += '   '
    line5[1] += ' '
    line5[3] += ' '

    paths = me.get_location().get_paths()

    # Display each direaction line by line each time
    if 'northwest' in paths:
        if has_creature('northwest', paths):
            line1[0] += '[C]'
        else:
            line1[0] += '[ ]'
        line2[1] += '\\'
    else:
        line1[0] = '   '
        line2[1] = ' '

    if 'north' in paths:
        if has_creature('north', paths):
            line1[2] += '[C]'
        else:
            line1[2] += '[ ]'
        line2[2] += ' | '
    else:
        line1[2] += '   '
        line2[2] += '   '

    if 'northeast' in paths:
        if has_creature('northeast', paths):
            line1[4] += '[C]'
        else:
            line1[4] += '[ ]'
        line2[3] += '/'
    else:
        line1[4] += '   '
        line2[3] += ' '

    if 'west' in paths:
        if has_creature('west', paths):
            line3[0] += '[C]'
        else:
            line3[0] += '[ ]'
        line3[1] += '-'
    else:
        line3[0] += '   '
        line3[1] += ' '

    # Location where user currently at
    line3[2] += '[x]'

    if 'east' in paths:
        if has_creature('east', paths):
            line3[4] += '[C]'
        else:
            line3[4] += '[ ]'
        line3[3] += '-'
    else:
        line3[4] += '   '
        line3[3] += '   '

    if 'southwest' in paths:
        if has_creature('southwest', paths):
            line5[0] += '[C]'
        else:
            line5[0] += '[ ]'
        line4[1] += '/'
    else:
        line5[0] += '   '
        line4[1] += ' '

    if 'south' in paths:
        if has_creature('south', paths):
            line5[2] += '[C]'
        else:
            line5[2] += '[ ]'
        line4[2] += ' | '
    else:
        line5[2] += '   '
        line4[2] += '   '

    if 'southeast' in paths:
        if has_creature('southeast', paths):
            line5[4] += '[C]'
        else:
            line5[4] += '[ ]'
        line4[3] += '\\'
    else:
        line5[4] += '   '
        line4[3] += ' '

    line1_str = ''
    line2_str = ''
    line3_str = ''
    line4_str = ''
    line5_str = ''
    for i in line1:
        line1_str += i
    for i in line2:
        line2_str += i
    for i in line3:
        line3_str += i
    for i in line4:
        line4_str += i
    for i in line5:
        line5_str += i
    print(line1_str.rstrip(' '))
    print(line2_str.rstrip(' '))
    print(line3_str.rstrip(' '))
    print(line4_str.rstrip(' '))
    print(line5_str.rstrip(' '))

    print('You are now at: ' + me.get_location().get_name() + '.')

    if len(me.get_location().get_items()) == 0 and len(me.get_location().get_creatures()) == 1:
        print("There is nothing here.")
    else:
        # Check this location has item or not
        what_you_have = ''
        for item in me.get_location().get_items():
            if len(what_you_have) == 0:
                what_you_have += item.get_desc()
            else:
                what_you_have += ' ' + item.get_desc()

        # Check this location has creature or not
        for creature in me.get_location().get_creatures():
            if creature.get_name().lower() != 'goose':
                if len(what_you_have) == 0:
                    what_you_have += creature.get_desc()
                else:
                    what_you_have += ' ' + creature.get_desc()
        print(what_you_have)
        
    # Check this location is in the exit.txt file or not
    if me.get_location().is_a_exit():
        print("The path to freedom is clear. You can FLEE this place.")
    
# Check what is your current terror rating
def look_me():
    print("You are a goose. You are probably quite terrifying.")
    print("In fact, you have a terror rating of: " + str(me.get_terror_rating()))

# List all the items at the user's current location
def look_here():
    if len(me.get_location().get_items()) == 0 and len(me.get_location().get_creatures()) == 1:
        print("There is nothing here.")
    else:
        for item in me.get_location().get_items():
            print(item.get_name().upper().ljust(16) + '| ' + item.get_item_name())

# Move to the direction input from user if it has paths
def move(cmd):
    paths = me.get_location().get_paths()
    if cmd == 'n':
        cmd = 'north'
    elif cmd == 'w':
        cmd = 'west'
    elif cmd == 'e':
        cmd = 'east'
    elif cmd == 's':
        cmd = 'south'
    elif cmd == 'nw':
        cmd = 'northwest'
    elif cmd == 'ne':
        cmd = 'northeast'
    elif cmd == 'se':
        cmd = 'southeast'
    elif cmd == 'sw':
        cmd = 'southwest'

    if cmd in paths:
        me.get_location().remove_creature(me)
        me.set_location(paths.get(cmd))
        me.get_location().add_creature(me)
        print("You move %s, to %s." % (cmd, me.get_location().get_name()))
        return True
    else:
        print("You can't go that way.")

# Pick up item from the location and remove from the location item list
def take_item(name):
    found = False
    for item in me.get_location().get_items():
        if item.get_name() == name:
            print("You pick up the " + item.get_item_name() + ".")
            me.get_location().remove_item(item)
            me.take(item)
            found = True

    if not found:
        print("You don't see anything like that here.")
    return found

# Take off item to the location and add to the location's item list
def drop_item(name):
    found = False
    for item in me.get_items():
        if item.get_name() == name:
            print("You drop the " + item.get_item_name() + '.')
            me.drop(item)
            me.get_location().add_item(item)
            found = True
    if not found:
        print("You don't have that in your inventory.")
    return found

# If you can flee at specific location, you win the game
def flee():
    if me.get_location().is_a_exit():
        print('You slip past the dastardly Goosechasers and run off into the wilderness! Freedom at last!')
        print('========= F R E E D O M =========')
        exit()
    else:
        print("There's nowhere you can run or hide! Find somewhere else to FLEE.")

# Check the item's name at location and terror_rating
def look_item(name):
    for item in me.get_location().get_items():
        if item.get_name() == name:
            print(item.get_item_name() + ' - Terror Rating: ' + str(item.get_terror()))
            return True

# Check the item's name with goose and terror_ratin
def look_inv(name):
    for item in me.get_items():
        if item.get_name() == name:
            print(item.get_item_name() + ' - Terror Rating: ' + str(item.get_terror()))
            return True
        
# Check the creature's name and terror_rating as well as compare with user's terror_rating
def look_creature(name):
    for creature in me.get_location().get_creatures():
        if creature.get_name().lower() == name:
            if me.get_terror_rating() - creature.get_terror_rating() >= 5:
                print("{} looks a little on-edge around you.".format(creature.get_name()))
            elif me.get_terror_rating() - creature.get_terror_rating() <= -5:
                print("{} doesn't seem very afraid of you.".format(creature.get_name()))
            else:
                print("Hmm. {} is a bit hard to read.".format(creature.get_name()))
            return True

# Creature come to players
def creatures_come_to_player(creature):
    if creature.come_to_player():
        if creature.get_location() == me.get_location():
            print("\n%s has arrived at %s." % (creature.get_name(), creature.get_location().get_name()))
        return True

# If the user and creature at the same location
def creatures_catch(creature):
    if creature.get_location() == me.get_location() and creature.get_catch_time() < 2:
        print("\n%s is trying to catch you!" % creature.get_name())
        creature.catch()
        # print(creature.get_catch_time())
        if me.get_terror_rating() <= creature.get_terror_rating() or creature.get_catch_time() == 2:
            print("Oh no, you've been caught!")
            print("========= GAME OVER =========")
            exit()
        else:
            print("But your presence still terrifies them...")
        return True

# Creature pick up items
def creatures_pick(creature):
    items = creature.get_location().get_items()
    if len(items) > 0:
        creature.take(items[0])
        creature.get_location().remove_item(items[0])
        return True

# Creature's actions at every costly actions and alarming actions
def creatures_act():
    for creature in creatures:
        if creatures_catch(creature):
            pass
        elif creatures_come_to_player(creature):
            pass
        elif not creatures_pick(creature):
            creature.move_clockwise()

# Scared away creatures if user have higher terror_rating
def honk():
    cres = me.get_location().get_creatures()
    
    # Copy creatures of the location of the goose
    clone_cres = cres[:] 
    if len(cres) == 1:
        print("All shall quiver before the might of the goose! HONK!")
    elif len(cres) > 1:
        print("You sneak up behind your quarry and honk with all the force of a really angry airhorn! HONK!")
        for creature in cres:
            if creature.get_name().lower() != 'goose' and me.get_terror_rating() > creature.get_terror_rating():
                print("%s is spooked! They flee immediately!" % creature.get_name())
                
                # Remove the creature from the copy
                clone_cres.remove(creature)
                creatures.remove(creature)
            elif creature.get_name().lower() != 'goose':
                print("%s is not spooked :(" % creature.get_name())
                
        # Set the creatures of this location to the copy
        me.get_location().set_creature(clone_cres) 
        
        # If user scare away all creatures, they win
        if len(creatures) == 0:
            print('\nNone can stand against the power of the goose!')
            print('========= V I C T O R Y =========')
            exit()
        
#### Load data from the arguments
if len(sys.argv) < 4:
    print("Usage: python3 game.py <PATHS> <ITEMS> <CHASERS> <EXITS>")
    exit()

locations = process_locations(sys.argv[1])
process_items(sys.argv[2], locations)
creatures = process_creatures(sys.argv[3], locations)
process_exits(sys.argv[4], locations)

me = Creature("goose", 5, locations[0], desc='')
locations[0].add_creature(me)

#### Main body of the project
look()
print()
cmd = input('>> ')
while cmd != '':
    # All commands are case-insensitive
    cmd = cmd.lower()
    cmd = cmd.split(" ")

    if cmd[0] == 'quit':
        print('Game terminated.')
        exit()

    # Free actions
    elif cmd[0] == 'help':
        help()
    elif cmd[0] == 'inv':
        inv()
    elif cmd[0] == 'flee':
        flee()
    elif cmd[0] in ['look', 'l']:
        if len(cmd) == 1:
            look()
        elif cmd[1] == 'me':
            look_me()
        elif cmd[1] == 'here':
            look_here()
        else:
            name = cmd[1].lower()
            if not (look_item(name) or look_creature(name) or look_inv(name)):
                print("You don't see anything like that here.")

    # Costly actions
    elif cmd[0] in ['northwest', 'nw', 'north', 'n', 'northeast', 'ne', 'east', 'e'
        , 'southeast', 'se', 'south', 's', 'southwest', 'sw', 'west', 'w']:
        if move(cmd[0]):
            creatures_act()
            look()
    elif cmd[0] == 'take':
        name = cmd[1]
        if take_item(name):
            creatures_act()
    elif cmd[0] == 'drop':
        name = cmd[1]
        if drop_item(name):
            creatures_act()

    # Alarming actions
    elif cmd[0] == 'wait':
        print("You lie in wait.")
        creatures_act()
    elif cmd[0] in ['honk', 'y']:
        honk()
        creatures_act()

    else:
        print("You can't do that.")
    print()
    cmd = input('>> ')

