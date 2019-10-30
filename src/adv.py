from room import Room
from player import Player

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
# Write a loop that:
#
def movement():   
    # if playerOne.currentRoom.name == playerOne.lastRoom.name:
    #     print("You cannot go in that direction")
    if playerOne.currentRoom == room['outside'] and playGame.move == "north":
        playerOne.updateRoom(room['foyer'])
        playerOne.updatePreviousRoom(room['outside'])
    elif playerOne.currentRoom == room['foyer'] and playGame.move == "south":
        playerOne.updateRoom(room['outside'])
        playerOne.updatePreviousRoom(room['foyer'])
    elif playerOne.currentRoom == room['foyer'] and playGame.move == "north":
        playerOne.updateRoom(room['overlook'])
        playerOne.updatePreviousRoom(room['foyer'])
    elif playerOne.currentRoom == room['overlook'] and playGame.move == "south":
        playerOne.updateRoom(room['foyer'])
        playerOne.updatePreviousRoom(room['overlook'])
    elif playerOne.currentRoom == room['foyer'] and playGame.move == "east":
        playerOne.updateRoom(room['narrow'])
        playerOne.updatePreviousRoom(room['foyer'])
    elif playerOne.currentRoom == room['narrow'] and playGame.move == "west":
        playerOne.updateRoom(room['foyer'])
        playerOne.updatePreviousRoom(room['narrow'])
    elif playerOne.currentRoom == room['narrow'] and playGame.move == "north":
        playerOne.updateRoom(room['treasure'])
        playerOne.updatePreviousRoom(room['narrow'])
    elif playerOne.currentRoom == room['treasure'] and playGame.move == "south":
        playerOne.updateRoom(room['narrow'])
        playerOne.updatePreviousRoom(room['treasure'])
    # elif playerOne.__eq__ == True:
    #     print("You cannot go in that direction")
    else:
        print("Invalid Input")

def playGame():
    running = True
    print(f"Hello, {playerOne.name}, let's go on an adventure.    Your inventory consists of {playerOne.items}.  Press Q to quit at any time")
    playerOne.lastRoom.name = "the sheer cliff you just scaled"
    while running:
        print(f"You leave {playerOne.lastRoom.name} and enter {playerOne.currentRoom.name}.  You look and see that {playerOne.currentRoom.description}")
        playGame.move = input("Enter which direction you want to go: ")
        if playGame.move == "q":
            print(f"{playerOne.name} decides to quit.  Have a nice day")
            running = False
        else:
            movement()     

print(playGame())


# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
