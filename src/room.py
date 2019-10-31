# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
    
    def addItemsToRoom (self, *itemAdd):
        self.items.append(itemAdd)
        print(f"\nYou added {itemAdd} to the room\n")
    
    def removeItemsFromRoom (self, *itemDrop):
        self.items.remove(itemDrop)
        print(f"\n{itemDrop} was picked up\n")
    
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
                # roomItems = each.itemDescription

    
    # def describeRoom(self):
    #     print(f"You are in {self.name}, you can see {self.description}")
