# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
    
    def addItemsToRoom (self, *item):
        self.items.append(item)
        print(f"You added {self.items in range (2)} to the room")
    
    def removeItemsFromRoom (self, **item):
        self.items.remove(item)
        print(f"You drop {item} on the floor")
    
    # def listItemsInRoom(self):
    #     print (self.items)
    
    def __repr__(self):
        #return str(self.__class__) + ": " + str(self.__dict__)
        return f"{self.items}"

    
    # def describeRoom(self):
    #     print(f"You are in {self.name}, you can see {self.description}")
