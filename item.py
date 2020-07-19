class Item:
    # Constructor, instantiates an Item class
    def __init__(self, short_name, item_name, full_desc, terror_rating):
        self.name = short_name
        self.item_name = item_name
        self.full_desc = full_desc
        self.terror_rating = int(terror_rating)

    # return the context of variable
    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

    def get_item_name(self):
        return self.item_name

    def get_desc(self):
        return self.full_desc

    def get_terror(self):
        return self.terror_rating

