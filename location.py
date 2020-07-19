class Location:
    # Constructor, instantiates a Location class
    def __init__(self, name):
        self.name = name
        self.paths = {}
        self.items = []
        self.creatures = []
        self.is_exit = False

    # return the context of variable
    def __str__(self):
        return self.name + " items: " + str(len(self.items)) \
               + " creatures: " + str(len(self.creatures)) + " " + str(self.is_exit)

    def get_name(self):
        return self.name

    # A function when something is droped at a location, but can be useful in other ways
    def add_item(self, item):
        self.items.append(item)

    # A function when something is taken from a location, but can be useful in other ways
    def remove_item(self, item):
        self.items.remove(item)

    def add_path(self, dire, destination):
        # case insensitive
        d = dire.lower()
        self.paths[d] = destination

    def add_creature(self, creature):
        self.creatures.append(creature)

    def remove_creature(self, creature):
        self.creatures.remove(creature)
        
    def set_creature(self,creatures):
        self.creatures = creatures

    def set_exit(self):
        self.is_exit = True

    def get_paths(self):
        return self.paths

    def get_items(self):
        return self.items

    def get_creatures(self):
        return self.creatures

    def is_a_exit(self):
        return self.is_exit

