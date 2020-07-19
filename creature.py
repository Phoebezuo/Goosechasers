class Creature:
    # Constructor, instantiates a Creature class
    def __init__(self, name, terror_rating, location=None, desc=None, dire=None):
        self.name = name
        self.desc = desc
        self.terror_rating = int(terror_rating)
        self.dire = dire
        self.items = []
        self.location = location
        self.catch_time = 0

    # return the context of variable
    def __str__(self):
        return self.name

    # A function when a creature take an item object
    def take(self, item):
        self.items.append(item)
        self.terror_rating += item.get_terror()

    # A function when a creature drop an item object
    def drop(self, item):
        self.items.remove(item)
        self.terror_rating -= item.get_terror()

    def get_terror_rating(self):
        return self.terror_rating

    def get_items(self):
        return self.items

    def get_desc(self):
        return self.desc

    def get_name(self):
        return self.name

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def clockwise_dir(self, dir):
        if dir == 'north':
            return 'northeast'
        elif dir == 'northeast':
            return 'east'
        elif dir == 'east':
            return 'southeast'
        elif dir == 'southeast':
            return 'south'
        elif dir == 'south':
            return 'southwest'
        elif dir == 'southwest':
            return 'west'
        elif dir == 'west':
            return 'northwest'
        elif dir == 'northwest':
            return 'north'

    def get_catch_time(self):
        return self.catch_time

    def catch(self):
        self.catch_time += 1


    def come_to_player(self):
        paths = self.location.get_paths()

        # If creature can move to the player, change direction and move
        for key, loc in paths.items():
            creatures = loc.get_creatures()
            for creature in creatures:
                if creature.get_name() == 'goose':
                    self.dire = key
                    self.move()
                    return True

    # Keep changing the direction clockwise until they have their path in this direction
    def move_clockwise(self):
        paths = self.location.get_paths()
        i = 0
        while self.dire not in paths and i < 9:
            self.dire = self.clockwise_dir(self.dire)
            i+=1
        if self.dire in paths:
            self.move()
            return True

    # Remove creature from current location, change direction and then add creature to the destination
    def move(self):
        paths = self.location.get_paths()
        self.location.remove_creature(self)
        self.location = paths.get(self.dire)
        self.location.add_creature(self)
        self.catch_time = 0


