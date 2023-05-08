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


west_puzzle = 0
up_puzzle = 0
down_puzzle = 0

rooms = {}
#main room
main_room = Room()
main_room.allowed_movements.append('n')
main_room.allowed_movements.append('s')
main_room.allowed_movements.append('e')
if west_puzzle == 1:
	main_room.allowed_movements.append('w')
rooms[(0,0,0)] = main_room
main_room.description[((),())] = f"Main: You enter a large, nearly empty living room. {NPC_name} stands by the couch, looking {NPC_expression}."

north_room = Room()
main_room.allowed_movements.append('s')
if up_puzzle == 1:
	north_room.allowed_movements.append('u')
	north_room.description[((),())] = "North: You enter a study full of thousands of bookshelves and a staircase leading to a door."
	north_room.description[(('phone'),())] = "North: You enter a study full of thousands of bookshelves and a staircase leading to a door. You notice that a lost phone is laying on a desk."
north_room.items.append('phone')
north_room.description[(('phone'),())] = "North: You enter a study full of thousands of bookshelves and a staircase leading to a locked door. You notice that a lost phone is laying on a desk. However, you notice a book that is slightly sticking out of the bookshelf."
north_room.description[((),())] = "North: You enter a study full of thousands of bookshelves and a staircase leading to a locked door. However, you notice a book that is slightly sticking out of the bookshelf."
rooms[(0,1,0)] = north_room

south_room = Room()
south_room.allowed_movements.append('n')
if down_puzzle == 1:
	south_room.allowed_movements.append('d')
	south_room.description[((),())] = "South: You walk into a room filled with pictures and paintings. There is a staircase leading down to a door."
	south_room.description[(('paintbrush'),())] = "South: You walk into a room filled with pictures and paintings. Next to one of the paintings is a set of paintbrushes. There is a staircase leading down to a door."
south_room.description[(('paintbrush'),())] = "South: You walk into a room filled with pictures and paintings. Next to one of the paintings is a set of paintbrushes. There is a staircase leading down to a locked door. However, you notice that there are some words painted on one of the paintings."
south_room.description[((),())] = "South: You walk into a room filled with pictures and paintings. There is a staircase leading down to a locked door. However, you notice that there are some words painted on one of the paintings."
rooms[(0,-1,0)] = south_room

east_room = Room()
east_room.allowed_movements.append('w')
if west_puzzle == 1:
	east_room.description[(('circuitboard'),())] = "East: You see a room filled with computers and other electronics. One of the electronics that you notice appears to be open, a circuit board poking out."
	east_room.description[((),())] = "East: You see a room filled with computers and other electronics."
east_room.description[(('circuitboard'),())] = "East: You see a room filled with computers and other electronics. One of the electronics that you notice appears to be open, a circuit board poking out. However, another computer is also turned on with a program open."
east_room.description[((),())] = "East: You see a room filled with computers and other electronics. However, another computer is also turned on with a program open."
rooms[(1,0,0)] = east_room