# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, currentRoom, lastRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.lastRoom = lastRoom
        self.items = ["1 torch",]
    
    def updateRoom(self, direction):
        self.currentRoom = direction
    
    # def __eq__(self, lastLocation):
    #     if self.currentRoom == self.lastRoom:
    #         return True
    #     else:
    #         return False
    
    def updatePreviousRoom(self, lastLocation):
        self.lastRoom = lastLocation
    
    def addItem(self, itemAdd):
        self.items.append(itemAdd)
        print(f"You've added {itemAdd}")
    
    def dropItem(self, itemDrop):
        self.items.remove(itemDrop)
        print(f"Your current inventory: {self.items}")
