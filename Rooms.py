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
		player_input = input(f"Which direction would you like to move? You can move in the following directions\n{self.allowed_movements}\n")
		if player_input in MOVEMENT:
			if player_input in self.allowed_movements:
				
				#player.position = player_input
				player.position = MOVEMENT.get(player_input)
			else:
				print("You cannot go that direction.")
		else:
			print("That is not a valid direction")

	def descriptions(self):
		key = tuple(self.items), tuple(self.viewables)

		return "\n"+self.description.get(key, "Something broke")

	def kitchen(self):
		main_room.allowed_movements.append('west')

	def upperroom(self):
		north_room.allowed_movements.append('up')
		
	def lowerroom(self):
		south_room.allowed_movements.append('d')


rooms = {}
#main room
main_room = Room()
main_room.allowed_movements.append('north')
main_room.allowed_movements.append('south')
main_room.allowed_movements.append('east')
rooms[(0,0,0)] = main_room
main_room.description[((),())] = f"Main: You enter a large, nearly empty living room. A person stands by the couch."

north_room = Room()
north_room.allowed_movements.append('south')
north_room.items.append("phone")
north_room.viewables.append("bookshelf")
north_room.description[(('phone',),("bookshelf",))] = "North: You enter a study full of thousands of bookshelves and a staircase leading to a locked door. You notice that a lost phone is laying on a desk. However, you notice a book that is slightly sticking out of the bookshelf."
north_room.description[((),("bookshelf",))] = "North: You enter a study full of thousands of bookshelves and a staircase leading to a locked door. However, you notice a book that is slightly sticking out of the bookshelf."
north_room.description[((),())] = "North: You enter a study full of thousands of bookshelves and a staircase leading to a door."
north_room.description[(('phone'),())] = "North: You enter a study full of thousands of bookshelves and a staircase leading to a door. You notice that a lost phone is laying on a desk."
rooms[(0,1,0)] = north_room


south_room = Room()
south_room.allowed_movements.append('north')
south_room.items.append("paintbrush")
south_room.viewables.append("painting")
south_room.description[((),())] = "South: You walk into a room filled with pictures and paintings. There is a staircase leading down to a door."
south_room.description[(('paintbrush'),())] = "South: You walk into a room filled with pictures and paintings. Next to one of the paintings is a set of paintbrushes. There is a staircase leading down to a door."
south_room.description[(("paintbrush",),('painting',))] = "South: You walk into a room filled with pictures and paintings. Next to one of the paintings is a set of paintbrushes. There is a painting with a strange riddle painted onto it. There is a staircase leading down to a door."
south_room.description[((),('painting',))] = "South: You walk into a room filled with pictures and paintings. There is a painting with a strange riddle painted onto it. There is a staircase leading down to a door."
rooms[(0,-1,0)] = south_room

east_room = Room()
east_room.allowed_movements.append('west')
east_room.viewables.append("computer")
east_room.items.append('circuitboard')
east_room.description[(('circuitboard',),('computer',))] = "East: You see a room filled with computers and other electronics. One of the electronics that you notice appears to be open, a circuit board poking out. However, another computer is also turned on with a program open."
east_room.description[((),('computer',))] = "East: You see a room filled with computers and other electronics. However, another computer is also turned on with a program open."
east_room.description[(('circuitboard',),())] = "East: You see a room filled with computers and other electronics. One of the electronics that you notice appears to be open, a circuit board poking out."
east_room.description[((),())] = "East: You see a room filled with computers and other electronics."
rooms[(1,0,0)] = east_room

west_room = Room()
west_room.allowed_movements.append('east')
west_room.items.append('soda')
west_room.description[(("soda",),())] = "West: You enter a pristine kitchen, on the counter, there is a can of soda."
west_room.description[((),())] = "West: You enter a pristine kitchen."
rooms[(-1,0,0)] = west_room

upper_room = Room()
upper_room.allowed_movements.append('down')
upper_room.items.append('screwdriver')
upper_room.description[(("screwdriver",),())] = "Upper: You ascend the staircase and see a messy bedroom filled with junk. In an open drawer full of tools, you see a screwdriver."
upper_room.description[((),())] = "You ascend the staircase and see a messy bedroom filled with junk."
rooms[(0,1,1)] = upper_room

lower_room = Room()
lower_room.allowed_movements.append('up')
lower_room.items.append('doll',)
lower_room.description[(("doll"),())] = "Lower: You descend the staircase to a tidy bedroom. There is a doll on the bed."
lower_room.description[((),())] = "Lower: You descend the staircase to a tidy bedroom."
rooms[(0,-1,-1)] = lower_room