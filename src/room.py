# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
    
    def addItemsToRoom (self, *item):
        self.items.append(item)
        print(f"You added {item} to the room")
    
    def removeItemsFromRoom (self, **item):
        self.items.remove(item)
        print(f"You drop {item} on the floor")
    
    # def listItemsInRoom(self):
    #     print (self.items)
    
    def __repr__(self):
        #return str(self.__class__) + ": " + str(self.__dict__)
        #return f"{self.items}"
        for eachItem in self.items:
            for each in eachItem:
                return each.itemDescription

#def itemLoop():
   # for eachItem in playerOne.currentRoom.items:
            #print("eachItem is ", eachItem)
            #for each in eachItem:
                # playerOne.viewableItems(each)
                # print ("each is ", each)
                # print("playeritems is ", playerOne.whatPlayerSees)
                # print(each.itemName)
                #roomItems = each.itemDescription

    
    # def describeRoom(self):
    #     print(f"You are in {self.name}, you can see {self.description}")
