class Items:
    def __init__(self, itemName, itemDescription):
        self.itemName = itemName
        self.itemDescription = itemDescription

    # def __str__(self):
    #     return str(self.__class__) + ": " + str(self.__dict__)
    
    def __repr__(self):
        return f"{self.itemName}: {self.itemDescription}"
        # str(self.__class__) + ": " + str(self.__dict__)

    
