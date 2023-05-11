from numpy import array

MOVEMENT = {
	"north" : array([0,1,0]),
	#north
	"south" : array([0,-1,0]),
	#south
	"east" : array([1,0,0]),
	#east
	"west" : array([-1,0,0]),
	#west
	"up" : array([0,0,1]),
	#up
	"down" : array([0,0,-1]),
	#down
	}

class Room():
	def __init__(self):
		self.items = []
		self.allowed_movements = []
		self.description = {}
		self.viewables = []

	def pickup(self,player):
		if self.items:
				pickup = self.items[0]
				player.inventory.append(pickup)
				self.items.remove(pickup)
		else:
			print("You have picked up every item in this room")

	def movement(self,player):
		player_input = input(f"Which direction would you like to move? You can move in the following directions\n{self.allowed_movements}")
		if player_input in MOVEMENT:
			if player_input in self.allowed_movements:
				print(f"{self.description}")
				player.position = player_input
			else:
				print("You cannot go that direction.")
		else:
			print("That is not a valid direction")

	west_puzzle = False
	up_puzzle = False
	down_puzzle = False

	def westpuzzle(self,player):
		if player.position == [(0,0,0)]:
			if "kitchen key" in player.inventory:
				player_input = input("Would you like to unlock the kitchen door? (y or n)\n")
				if player_input.lower() == 'y':
					print("Congrats! You've unlocked the kitchen door!")
					west_puzzle = True
			if west_puzzle == True:
				self.allowed_movements.append('w')
		if player.position == [(1,0,0)]:
			east_room.description[(('circuitboard'),())] = "East: You see a room filled with computers and other electronics. One of the electronics that you notice appears to be open, a circuit board poking out."
			east_room.description[((),())] = "East: You see a room filled with computers and other electronics."

	def uppuzzle(self,player):
		if "upstairs bedroom key" in player.inventory:
			player_input = input("Would you like to unlock the upstairs bedroom door? (y or n)\n")
			if player_input.lower() == 'y':
				print("Congrats! You've unlocked the upstairs bedroom door!")
				up_puzzle = True
		if up_puzzle == True:
			self.allowed_movements.append('u')
			north_room.description[((),())] = "North: You enter a study full of thousands of bookshelves and a staircase leading to a door."
			north_room.description[(('phone'),())] = "North: You enter a study full of thousands of bookshelves and a staircase leading to a door. You notice that a lost phone is laying on a desk."
		
	def downpuzzle(self,player):
		if "downstairs bedroom key" in player.inventory:
			player_input = input("Would you like to unlock the downstairs bedroom door? (y or n)\n")
			if player_input.lower() == 'y':
				print("Congrats! You've unlocked the downstairs bedroom door!")
				down_puzzle = True
		if down_puzzle == True:
			south_room.allowed_movements.append('d')
			south_room.description[((),())] = "South: You walk into a room filled with pictures and paintings. There is a staircase leading down to a door."
			south_room.description[(('paintbrush'),())] = "South: You walk into a room filled with pictures and paintings. Next to one of the paintings is a set of paintbrushes. There is a staircase leading down to a door."



rooms = {}
#main room
main_room = Room()
main_room.allowed_movements.append('n')
main_room.allowed_movements.append('s')
main_room.allowed_movements.append('e')
rooms[(0,0,0)] = main_room
main_room.description[((),())] = f"Main: You enter a large, nearly empty living room. A person stands by the couch"

north_room = Room()
main_room.allowed_movements.append('s')
north_room.items.append("phone")
north_room.viewables.append("bookshelf")
north_room.description[(('phone'),())] = "North: You enter a study full of thousands of bookshelves and a staircase leading to a locked door. You notice that a lost phone is laying on a desk. However, you notice a book that is slightly sticking out of the bookshelf."
north_room.description[((),())] = "North: You enter a study full of thousands of bookshelves and a staircase leading to a locked door. However, you notice a book that is slightly sticking out of the bookshelf."
rooms[(0,1,0)] = north_room


south_room = Room()
south_room.allowed_movements.append('n')
south_room.items.append("paintbrush")
south_room.viewables.append("painting")
rooms[(0,-1,0)] = south_room

east_room = Room()
east_room.allowed_movements.append('w')
east_room.viewables.append("computer")
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
rooms[(0,1,1)] = upper_room

lower_room = Room()
lower_room.allowed_movements.append('u')
lower_room.items.append('doll')
lower_room.description[(("doll"),())] = "Lower: You descend the staircase to a tidy bedroom. There is a doll on the bed."
lower_room.description[((),())] = "Lower: You descend the staircase to a tidy bedroom."
rooms[(0,-1,-1)] = lower_room