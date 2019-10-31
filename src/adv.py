from room import Room
from player import Player
from items import Items

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

items = {
    'torch':  Items("Torch",
                     "A brightly burning torch that can light even the darkest passages"),

    'rope':    Items("Rope", """A long length of rope, sturdy and ready to be used"""),

    'gun': Items("Gun", """A shiny Glock 17. Examining the magazine, you see it only has 7 bullets left.  Better make them count"""),

    'whip':   Items("Whip", """A 5 foot whip.  You feel like Indiana Jones and suddenly want to whip someone"""),

    'hat': Items("Hat", """An explorers hat.  You know deep down that you'll never be worthy of it"""),
    'treasure': Items("Treasure", """And old crown, worth at least a few bucks.  At least this trip wasn't a total loss""")
}


# Link rooms together

#room['outside'].n_to = room['foyer']
#room['foyer'].s_to = room['outside']
#room['foyer'].n_to = room['overlook']
#room['foyer'].e_to = room['narrow']
#room['overlook'].s_to = room['foyer']
#room['narrow'].w_to = room['foyer']
#room['narrow'].n_to = room['treasure']
#room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

playerOne = Player("Henry", room["outside"], room["treasure"])

room["outside"].addItemsToRoom(items["torch"])
#, items["hat"])
room["foyer"].addItemsToRoom(items["whip"])
room["overlook"].addItemsToRoom(items["rope"])
room["narrow"].addItemsToRoom(items["gun"])
room["treasure"].addItemsToRoom(items["treasure"])
#scores = [ student.name for student in names if student.gender == "Male" ]

#print(room["outside"].__str__)
# Write a loop that:
#

#def itemLoop():
   # for eachItem in playerOne.currentRoom.items:
            #print("eachItem is ", eachItem)
            #for each in eachItem:
                # playerOne.viewableItems(each)
                # print ("each is ", each)
                # print("playeritems is ", playerOne.whatPlayerSees)
                # print(each.itemName)
                #roomItems = each.itemDescription

def movement():   
    # if playerOne.currentRoom.name == playerOne.lastRoom.name:
    #     print("You cannot go in that direction")
    if playerOne.currentRoom == room['outside'] and playGame.action == "north":
        playerOne.updateRoom(room['foyer'])
        playerOne.updatePreviousRoom(room['outside'])
        for eachItem in playerOne.currentRoom.items:
            for each in eachItem:
                roomItems = each.itemDescription
        #print ("items are ", playerOne.currentRoom.items)

        # for eachItem in room["outside"].items:
        #     print("eachItem is ", eachItem)
        #     for each in eachItem:
        #         #playerOne.viewableItems(each)
        #         print ("each is ", each)
        #         #print("playeritems is ", playerOne.whatPlayerSees)
        #         print("each itemName is: ", each.itemName)
        #         print("each itemDescription is ", each.itemDescription)


    elif playerOne.currentRoom == room['foyer'] and playGame.action == "south":
        playerOne.updateRoom(room['outside'])
        playerOne.updatePreviousRoom(room['foyer'])

    elif playerOne.currentRoom == room['foyer'] and playGame.action == "north":
        playerOne.updateRoom(room['overlook'])
        playerOne.updatePreviousRoom(room['foyer'])

    elif playerOne.currentRoom == room['overlook'] and playGame.action == "south":
        playerOne.updateRoom(room['foyer'])
        playerOne.updatePreviousRoom(room['overlook'])

    elif playerOne.currentRoom == room['foyer'] and playGame.action == "east":
        playerOne.updateRoom(room['narrow'])
        playerOne.updatePreviousRoom(room['foyer'])
    elif playerOne.currentRoom == room['narrow'] and playGame.action == "west":
        playerOne.updateRoom(room['foyer'])
        playerOne.updatePreviousRoom(room['narrow'])
    elif playerOne.currentRoom == room['narrow'] and playGame.action == "north":
        playerOne.updateRoom(room['treasure'])
        playerOne.updatePreviousRoom(room['narrow'])
    elif playerOne.currentRoom == room['treasure'] and playGame.action == "south":
        playerOne.updateRoom(room['narrow'])
        playerOne.updatePreviousRoom(room['treasure'])
    # elif playerOne.__eq__ == True:
    #     print("You cannot go in that direction")
    else:
        print("Invalid Input")

def getItem():
    test = playGame.action.split()
    if len(test) == 2:
        if test[0] == "get":
            for eachItem in playerOne.currentRoom.items:
                for each in eachItem:
                    #print("each.itemName is ", each.itemName)
                    if test[1] == each.itemName:
                        print("each is room item ", each)
                        playerOne.addItem(each)
                        playerOne.currentRoom.removeItemsFromRoom(each)
                    else:
                        print("You mispelled that")
        elif test[0] ==  "drop":
            for eachItem in playerOne.playerInventory:
                for each in eachItem:
                    if test[1] == each.itemName:
                        print("each is inven", each)
                        #print("each.itemName is ", each.itemName)
                        playerOne.dropItem(each)
                        playerOne.currentRoom.addItemsToRoom(each)
                    else:
                        print("You mispelled that")
                
        elif test[0] == "inventory":
            for eachItem in playerOne.playerInventory:
                print("eachItem is ", eachItem)
                for each in eachItem:
                    print("each is ", each)
                #print("eachItemName is ", eachItem.itemName)
                    # if len(each) == 0:
                    #     print("Your inventory is empty")
                    # else:
                    print("\nYour inventory is ", each.itemDescription)
        else:
            print("Please try again")
    #else:
       # print("one word")

def playGame():
    running = True
    print(f"Hello, {playerOne.name}, let's go on an adventure.    Your inventory consists of {playerOne.playerInventory}.  Press Q to quit at any time")
    playerOne.lastRoom.name = "the sheer cliff you just scaled"
    while running:
        #if len(playerOne.currentRoom.items) == 0:
            #playerOne.currentRoom.items = "nothing"
        # ^ Turns item list into a string.  Bad transformation
        print(f"You leave {playerOne.lastRoom.name} and enter {playerOne.currentRoom.name}.  You look and see that {playerOne.currentRoom.description}.  You can see {playerOne.currentRoom.items} on the floor")
        playGame.action = input("Enter which direction you want to go: ")
        if playGame.action == "q":
            print(f"{playerOne.name} decides to quit.  Have a nice day")
            running = False
        else:
            movement()
            getItem()

print(playGame())


# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
