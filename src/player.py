# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
        self.items = []
    
    def addItem(self, itemAdd):
        self.items.append(itemAdd)
        print(f"You've added {itemAdd}")
    
    def dropItem(self, itemDrop):
        self.items.remove(itemDrop)
        print(f"Your current inventory: {self.items}")
