

# Goosechasers

## Description

This is a game that simulates a wild goose chase. The player will control a goose - a creature - that moves from one location to another, while avoiding other creatures that wish to harm it. The goose may attempt to frighten other creatures into running away (permanently) by honking at them, though some creatures will be more diﬃcult to frighten than others. If the goose is caught by another creature that it cannot frighten, the player loses. If the goose successfully navigates to a location that allows it to ﬂee from the other creatures, or successfully frightens away all other creatures on the map, the player wins.

## Conﬁguration Files

The program will be given 4 extra command line arguments when it is run:

```pytho
python3 game.py <PATHS> <ITEMS> <CHASERS> <EXITS>
```

These arguments (let's call them conﬁguration ﬁles) will be used to generate Location, Item, and Creature objects that you will need to run your program. The Location, Item, and Creature classes are to be deﬁned in the location.py, item.py, and creature.py ﬁles, respectively.

Examples of these conﬁguration ﬁles are sample_paths.txt, sample_items.txt, sample_chasers.txt, and sample_exits.txt. Empty lines encountered in any conﬁguration ﬁle can be safely skipped and ignored.

If fewer than 4 arguments are supplied, print: "Usage: python3 game.py <PATHS> <ITEMS> <CHASERS> <EXITS>" and exit the program.

Of the given arguments, you can expect that they will all be paths to a ﬁle (and/or the name of a ﬁle). If any one of the ﬁles speciﬁed by the arguments do not exist, print: "You have specified an invalid configuration file." and exit the program.

### <PATHS>

The ﬁrst argument, <PATHS> , should be the name of a ﬁle containing a list of all connections between Locations in the program. Each line is of the form: START > DIRECTION > DESTINATION

Where START and DESTINATION are the names of Location objects, and DIRECTION indicates a direction on the compass (northwest, north, northeast, east, southeast, south, southwest, west) that a creature must travel towards in order to move between START and DESTINATION . For example: Lake > northeast > Trail Trail > SOUTH > Gazebo

If a Creature is currently at the Lake , it can move NORTHEAST to arrive at the Trail . Similarly, if a Creature is currently on the Trail , it can travel SOUTH in order to arrive at the Gazebo . Paths do not need to be reﬂective - going north in location A and immediately going back south does not have to lead you back to location A. This is a game, so some paths might not make sense, and that's ok! For example: Lake > NORTH > Gazebo Gazebo > South > Gazebo

Location names are case sensitive, but DIRECTION s are not.

When the program starts, the player will begin in the FIRST room speciﬁed by this ﬁle. If an empty <PATHS> ﬁle is given, print: "The game cannot run without any rooms :(" and exit the program.

You can reasonably expect that any <PATHS> ﬁle we will give you will contain valid input (i.e. no weird lines like "Grass > Fence > More Grass" or "Not enough > arrows" .)

### <ITEMS>

The second argument, <ITEMS> , should be the name of a ﬁle deﬁning all the Item objects that are available in-game. Each line is of the form: short_name | item_name | full_desc | terror_rating | location

- full_desc is a long description of the item which is written to a Location 's description if the item exists at that location, but has not been picked up by a Creature. 

- location - as it implies - speciﬁes the name of a Location that the Item object will appear in when the game begins. You can expect that this is name will also appear somewhere in the <PATHS> conﬁguration ﬁle.

For example: rake | battered, old rake | A battered, old rake lies here, dreaming of lakes. | 2 | Garden

It is possible for the game to start and end with no items, so it is possible that the ﬁle speciﬁed by <ITEMS> is empty. Should this be the case, the game should run as normal.

### <CHASERS>

The third argument, <CHASERS> , should be the name of a ﬁle deﬁning all Creature objects in the game that are not controlled by the player. Each line of this ﬁle is of the form: name | description | terror_rating | location | direction

- The name of a Creature is a unique name that the program (and the user) can use to refer to the Creature object.

- A description of the Creature will be written to a Location 's description if the Creature is in the same Location as the player.

- terror_rating describes the terror_rating that a Creature begins with at the start of the game. This number represents how terrifying something is - or how diﬃcult a Creature is to frighten. 

- location - as it implies - speciﬁes the name of a Location that the Creature object will appear in when the game begins. You can expect that this is name will also appear somewhere in the <PATHS> conﬁguration ﬁle.

- direction describes a movement pattern that a Creature will engage in if it is not controlled by the player. 

An example: dog | A dog is barking at you! | 4 | Park | North

As the premise of the game is not possible without any creatures to chase the player, the <CHASERS> ﬁle cannot be empty! If an empty <CHASERS> ﬁle is provided, print: "There is nothing chasing you!" and exit the program.

### <EXITS>

The fourth argument, <EXITS> , should be the name of a ﬁle that contains a list of Location names. Each of these Location objects will allow the player to use the FLEE command to win the game. If a line speciﬁes a name that does not correspond to a Location , ignore it and move on to the next one.

It is possible for the <EXITS> conﬁguration ﬁle to be empty - in that case, the player has no choice but to scare oﬀ all other Creatures to win!

## Usage & Commands
![commands](https://github.com/Phoebezuo/Goosechasers/blob/master/commands.png)

``` py
python3 game.py sample_paths.txt sample_items.txt sample_chasers.txt sample_exits.txt
```

### QUIT

At any point, the player can end the game.

### HELP

The game will list all valid commands and their usage.

### INV

Prints the goose (player)'s inventory. 

### TAKE <ITEM>

Takes the speciﬁed item from the player's current location, and adds it to their inventory. This action can change the player's terror_rating .

### DROP <ITEM>

Removes the speciﬁed item from the player's inventory, and places it at their current location. This action can change the player's terror_rating .

### FLEE

If the player invokes this command at one of the locations speciﬁed by the <EXITS> conﬁguration ﬁle, the game is won. If the player attempts to FLEE at a Location that is not speciﬁed by the <EXITS> conﬁguration ﬁle, however, the attempt fails.

### HONK or Y

Attempts to scare oﬀ every other creature at the player's location using the player's terror_rating . If the player's terror_rating is higher than that of a target creature's, they are scared away permanently! If you successfully scare away ALL the creatures in the game, you win. If your terror_rating is less than or equal to that of a creature you honked at, the creature is not frightened - and will probably try to catch you.

### WAIT

This causes all Creature s that are not controlled by the player (i.e. Goosechasers) to "take their turn" (pick up an item, move one room, attempt to catch the goose, etc.)

### LOOK and L

Displays the location you are currently in.

### LOOK <ITEM>

Allows the player to examine items in their inventory or at their current location. The item's short_name will work for this.

### LOOK ME

Displays your current stats.

### LOOK <CREATURE>

Assesses a creature and how frightened it seems of the goose (player). Uses the creature's name as the argument. The creature must be in the same location as the player. Measures the player's terror_rating against target creature's.

### LOOK HERE

Lists the short_name s and item_name s of all Item objects at the player's current Location .

### Movement Commands

Moves the user to a connecting location in that speciﬁed direction.

## Sample Output

Here is a sample output of the program, which has been run using the sample conﬁguration ﬁles.

``` shell
[ ]     [C]
   \   /
[ ]-[x]
     |
    [ ]
You are now at: Fountain.
A grimy copper coin is stuck fast to the ground here. A weird blue rock minds its own business in the corner, unmoving.

>> look here
COIN            | strange copper coin
ROCK            | blue rock

>> LOOK coin
strange copper coin - Terror Rating: 2

>> look ME
You are a goose. You are probably quite terrifying.
In fact, you have a terror rating of: 5

>> east
You can't go that way.

>> cry
You can't do that.

>> take coin
You pick up the strange copper coin.

Dog has arrived at Fountain.

>> look dog
Hmm. Dog is a bit hard to read.

>> northwest
You move northwest, to Phone Booth.

Dog has arrived at Phone Booth.
        [ ]
       /
    [x]
   /   \
[C]     [ ]
You are now at: Phone Booth.
Bright red and striking, a ribbon adds a bit of colour to the ground here. A dog is barking at you!

>> ne
You move northeast, to Painted Fences.

Dog has arrived at Painted Fences.
    [ ] [ ]
     | /
    [x]-[ ]
   /
[ ]
You are now at: Painted Fences.
There is a bucket of green paint here. It is dangerously full. A dog is barking at you!

>> wait
You lie in wait.

Dog is trying to catch you!
But your presence still terrifies them...

>> n
You move north, to Windmill.

Dog has arrived at Windmill.


    [x]-[ ]
     |
    [ ]
You are now at: Windmill.
Someone has stabbed a knife into the ground here. It looks rusty. A dog is barking at you!
The path to freedom is clear. You can FLEE this place.

>> take knife
You pick up the rusty old knife.

Dog is trying to catch you!
But your presence still terrifies them...

>> look me
You are a goose. You are probably quite terrifying.
In fact, you have a terror rating of: 12

>> look dog
Dog looks a little on-edge around you.

>> HONK
You sneak up behind your quarry and honk with all the force of a really angry airhorn! HONK!
Dog is spooked! They flee immediately!

Greg has arrived at Windmill.

>> INV
You, a goose, are carrying the following items:
 - strange copper coin
 - rusty old knife

>> FLEE
You slip past the dastardly Goosechasers and run off into the wilderness! Freedom at last!
========= F R E E D O M =========
```

