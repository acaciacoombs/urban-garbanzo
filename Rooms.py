from numpy import array

MOVEMENT = {
	"n" : array([0,1,0]),
	#north
	"s" : array([0,-1,0]),
	#south
	"e" : array([1,0,0]),
	#east
	"w" : array([-1,0,0]),
	#west
	"u" : array([0,0,1]),
	#up
	"d" : array([0,0,-1]),
	#down
	}

class Room():
	def __innit__(self):
		self.items = []
		self.allowed_movements = []
		self.description = {}
		self.viewables = []

	def pickup(self,player):
		if self.items:
				pickup = self.items[0]
				inventory.append(pickup)
				self.items.remove(pickup)
		else:
			print("You have picked up every item in this room")

	def movement(self,player):
		if player_input in MOVEMENT:
			if player_input in self.allowed_movements:
				print(f"You are now in {room}.")
				position = player_input
			else:
				print("You cannot go that direction.")
		else:
			print("That is not a valid direction")


west_puzzle = False
up_puzzle = False
down_puzzle = False



rooms = {}
#main room
main_room = Room()
main_room.allowed_movements.append('n')
main_room.allowed_movements.append('s')
main_room.allowed_movements.append('e')
if "kitchen key" in player.inventory:
	player_input = input("Would you like to unlock the kitchen door? (y or n)\n")
	if player_input.lower() == 'y':
		print("Congrats! You've unlocked the kitchen door!")
		west_puzzle = True
if west_puzzle == True:
	main_room.allowed_movements.append('w')
rooms[(0,0,0)] = main_room
main_room.description[((),())] = f"Main: You enter a large, nearly empty living room. {NPC_name} stands by the couch, looking {NPC_expression}."

north_room = Room()
main_room.allowed_movements.append('s')
north_room.items.append("phone")
north_room.viewables.append("bookshelf")
if up_puzzle == True:
	north_room.allowed_movements.append('u')
	north_room.description[((),())] = "North: You enter a study full of thousands of bookshelves and a staircase leading to a door."
	north_room.description[(('phone'),())] = "North: You enter a study full of thousands of bookshelves and a staircase leading to a door. You notice that a lost phone is laying on a desk."
north_room.description[(('phone'),())] = "North: You enter a study full of thousands of bookshelves and a staircase leading to a locked door. You notice that a lost phone is laying on a desk. However, you notice a book that is slightly sticking out of the bookshelf."
north_room.description[((),())] = "North: You enter a study full of thousands of bookshelves and a staircase leading to a locked door. However, you notice a book that is slightly sticking out of the bookshelf."
rooms[(0,1,0)] = north_room


south_room = Room()
south_room.allowed_movements.append('n')
south_room.items.append("paintbrush")
south_room.viewables.append("painting")
if "downstairs bedroom key" in player.inventory:
	player_input = input("Would you like to unlock the downstairs bedroom door? (y or n)\n")
	if player_input.lower() == 'y':
		print("Congrats! You've unlocked the downstairs bedroom door!")
		down_puzzle = True
if down_puzzle == True:
	south_room.allowed_movements.append('d')
	south_room.description[((),())] = "South: You walk into a room filled with pictures and paintings. There is a staircase leading down to a door."
	south_room.description[(('paintbrush'),())] = "South: You walk into a room filled with pictures and paintings. Next to one of the paintings is a set of paintbrushes. There is a staircase leading down to a door."
south_room.description[(('paintbrush'),())] = "South: You walk into a room filled with pictures and paintings. Next to one of the paintings is a set of paintbrushes. There is a staircase leading down to a locked door. However, you notice that there are some words painted on one of the paintings."
south_room.description[((),())] = "South: You walk into a room filled with pictures and paintings. There is a staircase leading down to a locked door. However, you notice that there are some words painted on one of the paintings."
rooms[(0,-1,0)] = south_room

east_room = Room()
east_room.allowed_movements.append('w')
east_room.viewables.append("computer")
if west_puzzle == 1:
	east_room.description[(('circuitboard'),())] = "East: You see a room filled with computers and other electronics. One of the electronics that you notice appears to be open, a circuit board poking out."
	east_room.description[((),())] = "East: You see a room filled with computers and other electronics."
east_room.description[(('circuitboard'),())] = "East: You see a room filled with computers and other electronics. One of the electronics that you notice appears to be open, a circuit board poking out. However, another computer is also turned on with a program open."
east_room.description[((),())] = "East: You see a room filled with computers and other electronics. However, another computer is also turned on with a program open."
rooms[(1,0,0)] = east_room

west_room = Room()
west_room.allowed_movements.append('e')
west_room.items.append('soda')
west_room.description[(("soda"),())] = "West: You enter a pristine kitchen, on the counter, there is a can of soda."
west_room.description[((),())] = "West: You enter a pristine kitchen."
rooms[(-1,0,0)] = west_room

upper_room = Room()
upper_room.allowed_movements.append('d')
upper_room.items.append('screwdriver')
upper_room.description[(("screwdriver"),())] = "Upper: You ascend the staircase and see a messy bedroom filled with junk. In an open drawer full of tools, you see a screwdriver."
upper_room.description[((),())] = "You ascend the staircase and see a messy bedroom filled with junk."
rooms[(0,0,1)] = upper_room

lower_room = Room()
lower_room.allowed_movements.append('u')
lower_room.items.append('doll')
lower_room.description[(("doll"),())] = "Lower: You descend the staircase to a tidy bedroom. There is a doll on the bed."
lower_room.description[((),())] = "Lower: You descend the staircase to a tidy bedroom."
rooms[(0,0,-1)] = lower_room