# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, currentRoom, lastRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.lastRoom = lastRoom
        self.playerInventory = []
        #self.whatPlayerSees = []
    
    def updateRoom(self, direction):
        self.currentRoom = direction
    
    # def __eq__(self, lastLocation):
    #     if self.currentRoom == self.lastRoom:
    #         return True
    #     else:
    #         return False

    def viewableItems(self, *items):
        self.whatPlayerSees.append(items)
    
    def updatePreviousRoom(self, lastLocation):
        self.lastRoom = lastLocation
    
    def addItem(self, *playerItemAdd):
        self.playerInventory.append(playerItemAdd)
        print(f"\nYou've added {playerItemAdd}, your inventory is {self.playerInventory}\n")
    
    def dropItem(self, *itemDrop):
        self.playerInventory.remove(itemDrop)
        print(f"\nYour current inventory: {self.playerInventory}\n")
    
    
    

