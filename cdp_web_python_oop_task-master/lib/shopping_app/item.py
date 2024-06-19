from ownable import Ownable

class Item:
    instances = []

    def __init__(self, name, price, owner=None):
        self.name = name
        self.price = price
        self.set_owner(owner)
        # When an Item instance is created, that Item instance (self) is stored in the class variable instances.
        Item.instances.append(self)

    def label(self):
        return {"name": self.name, "price": self.price}

    @staticmethod
    def item_all():
        # Returns instances ==> Item.item_all() returns all Item instances created so far.
        return Item.instances
    
    def set_owner(self, owner):
            self.owner = owner
