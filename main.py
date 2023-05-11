from Rooms import rooms, MOVEMENT
import pickle
from numpy import array

prompts = "PROMPTS:\np = view prompts\nm = move\nt = talk to NPC\ng = gift item to NPC\np = pick up item\ni = view inventory\nr = remove from inventory\nv = view\nq = quit\n"
NPC_name = ''

class Player():
	def __init__(self):
		self.__position = (0, 0, 0)
		self.inventory = []
	@property
	def position(self):
		return tuple(self.__position)
	@position.setter
	def position(self, new_position):
		self.__position += new_position

player = Player()

def main(player):
	NPC_expression = 'ambivalent'
	Friendship_points = 1
	player_input = ''
	print(f"Hi! Welcome to Friendship Simulator. Here are all the prompts that you can use when interacting with items, rooms, and NPC's!\nPROMPTS:\nn = move north\ne = move east\ns = move south\nw = move west\nu = move up\nd = move down\np = pick up item\ni = view inventory\nq = quit\n")
	
	while player_input != 'q':
		room = rooms.get(player.position, "Something broke, please quit")
		if player_input == '':
			NPC_choice = input(f"Please pick an NPC to befriend. 'Social Butterfly',(SB), 'Curious Creative',(CC), or 'Loner Analyst', (LA).\n")
			NPC_choice = NPC_choice.lower()
			if NPC_choice == 'sb':
				NPC_name = 'Stella'
			elif NPC_choice == 'cc':
				NPC_name = 'Quinn'
			elif NPC_choice == 'la':
				NPC_name = 'Liam'
			else:
				print(f"'{NPC_choice}' isn't a valid choice.")
				NPC_choice = input(f"Please pick an NPC to befriend. 'Social Butterfly',(SB), 'Curious Creative',(CC), or 'Loner Analyst', (LA).\n")

			if NPC_name == 'Stella':
				player_name = input(f'''You walk into an abandoned building. In the center room of the building, you see someone. The person looks at you, speaking. "Oh my goodness hi! what's your name? I'm Stella!"\n''')
				zero_friendship_talk = f'''"... Oh hi {player_name}. What's up. Did you find my phone yet? I can't add your number if you haven't."'''
				one_friendship_talk = f'''"Hi {player_name}! I just walked into this stupid abandoned building and I guess I was bored enough to explore, but it's pretty boring. I even lost my phone in one of the rooms!!!"\n'''
				two_friendship_talk = f'''"HEY {player_name}!!! Thanks so much for the gift! Do you know if there is anything to drink around here? I'm thirsty and I want to make a toast to our new friendship!. Thanks soooo much!"'''
				liked_items = ['phone','soda']

			if NPC_name == 'Quinn':
				player_name = input(f'''You walk into an abandoned building. In the center room of the building, you see someone. The person looks at you, speaking. "Oh. Hi there! Nice to meet you. What's your name? I'm Quinn."\n''')
				zero_friendship_talk = f'''"Hey there. I guess you didn't hear me before but I'm looking for a paintbrush. PAINTBRUSH. I don't want anything else until I have a paintbrush"'''
				one_friendship_talk = f'''"What's up {player_name}? This abandoned building isn't much, but it's full of cool art! I hope I can find something new to paint with."\n'''
				two_friendship_talk = f'''"How's it going {player_name}?! These paintbrushes are the best! Thanks for the gift my dude! Now if only I could find something to give my super girly little sister. Maybe there is something in the house!"'''
				liked_items = ['paintbrush','doll']

			if NPC_name == 'Liam':
				player_name = input(f'''You walk into an abandoned building. In the center room of the building, you see someone. The person looks at you, speaking."Oh, uh, hi. Who are you?"\n''')
				zero_friendship_talk = f'''"... Hi {player_name}. Don't give me anything unless it can be used for my computer. Thanks..."'''
				one_friendship_talk = f'''"Oh. Hi {player_name}. I was just looking for some stuff to use to build my computer. If you find any and you don't want it, maybe you could give it to me. Or not. Doesn't matter."\n'''
				two_friendship_talk = f'''"Hey {player_name}. I'm looking for a screwdriver. My dad doesn't allow me near his tools anymore and I need one to assemble my new computer. Appreciate it, dude... Ew why did I just say dude."'''
				liked_items = ['circuitboard', 'screwdriver']
			print(f"{one_friendship_talk}")

		if Friendship_points == 0:
			NPC_expression = 'frustrated'
		if Friendship_points == 1:
			NPC_expression = 'ambivalent'
		if Friendship_points == 2:
			NPC_expression = 'happy'
	
		player_input = input("What now? (use 'p' to see prompts)\n")
		if player_input.lower() == 'p':
			print(f"\n{prompts}")
		
		if player_input.lower() == 't':
			if player.position == [(0,0,0)]:
				if Friendship_points == 0:
					print(f"{zero_friendship_talk}")
				elif Friendship_points == 1:
					print(f"{one_friendship_talk}")
				elif Friendship_points == 2:
					print(f"{two_friendship_talk}")
			else:
				print("Sorry, there is no one to talk to in this room.")
				print(f"\n{prompts}")

		if player_input.lower() == 'p':
			player_input = ("Would you like to pick up the item in this room? (Answer 'y' or 'n')")
			if player_input.lower() == 'y':
				pickup()
			else:
				print(f"\n{prompts}")

		if player_input.lower() == 'n':
			room.movement(player)
		if player_input.lower() == 'e':
			room.movement(player)
		if player_input.lower() == 'w':
			room.movement(player)
		if player_input.lower() == 'u':
			room.movement(player)
		if player_input.lower() == 'd':
			room.movement(player)
		
		if player_input.lower() == 'i':
			print(player.inventory)
		
		if player_input.lower() == 'v':
			if len(room.viewables) > 0:
				player_input = (f"Would you like to view {room.viewables[0]}? (y or n)\n")
				if player_input.lower() == "y":
					if "computer" in room.viewables:
						player_input = input("On the computer, a riddle is displayed. It reads as follows:\nWhat is at the beginning of end and is also at the end of time?\n")
						if player_input.lower() != 'e':
							player_input = input("Hint: look closely at the words 'time' and 'end'.\n")
							if player_input.lower() != 'e':
								print("I'm out of hints! The answer was e")
								print("You've recieved the kitchen key in your inventory!")
								player.inventory.append("kitchen key")
								room.viewables.remove("computer")
							else:
								print("You've solved the riddle! You've recieved the kitchen key in your inventory!")
								player.inventory.append("kitchen key")
								room.viewables.remove("computer")
						else:
							print("You've solved the riddle! You've recieved the kitchen key in your inventory!")
							player.inventory.append("kitchen key")
							room.viewables.remove("computer")

					elif "painting" in room.viewables:
						player_input = input("There is a riddle painted on the canvas. It reads as follows:\nYou feed me, I grow stronger, and when I drink, I die. What am I?\n")
						if player_input.lower() != "fire":
							player_input = input("Hint: I am the opposite of water.")
							if player_input.lower() != "fire":
								print("I'm out of hints! The answer was fire.")
								print("You've recieved the downstairs bedroom key in your inventory!")
								player.inventory.append("downstairs bedroom key")
								room.viewables.remove("painting")
							else:
								print("You've solved the riddle! You've recieved the downstairs bedroom key in your inventory!")
								player.inventory.append("downstairs bedroom key")
								room.viewables.remove("painting")
						else:
							print("You've solved the riddle! You've recieved the downstairs bedroom key in your inventory!")
							player.inventory.append("downstairs bedroom key")
							room.viewables.remove("painting")

					elif "bookshelf" in room.viewables:
						player_input = input("You grab the book and open it, inside there is a riddle. It reads as follows:\nHow many months of the year have 28 days?")
						if player_input != '12':
							player_input = input("Hint: 30 > 28")
							if player_input != '12':
								print("I'm out of hints! The answer was 12.")
								print("You've recieved the upstairs bedroom key in your inventory!")
								player.inventory.append("upstairs bedroom key")
								room.viewables.remove("bookshelf")
							else:
								print("You've solved the riddle! You've recieved the upstairs bedrrom key in your inventory!")
								player.inventory.append("upstairs bedroom key")
								room.viewables.remove("bookshelf")
						else:
							print("You've solved the riddle! You've recieved the upstairs bedrrom key in your inventory!")
							player.inventory.append("upstairs bedroom key")
							room.viewables.remove("bookshelf")
				else:
					print(f"What now?\n{prompts}")
			else:
				print(f"There is nothing here left to view.\n{prompts}")

		if player_input.lower() == 'g':
			if player.position == [(0,0,0)]:
				if player.inventory:
					print(player.inventory)
					player_input = input("What item would you like to gift?")
					if player_input in player.inventory:
						player.inventory.remove(player_input)
						if player_input in liked_items:
							Friendship_points += 1
						else:
							Friendship_points -= 1
					else:
						print("Item not in inventory")
				else:
					print("Nothing in inventory")


		if Friendship_points < 0:
			you_loser()
		if Friendship_points > 2:
			if NPC_name == "Stella":
				print("OMG thank you so much! You're my best friend! Let's hang out again later!")
			if NPC_name == "Liam":
				print("I don't know how to thank you enough. You're defintely my best friend, I'll see you around sometime.")
			if NPC_name == "Quinn":
				print("WOW! You're amazing. Thanks dude! I'll need to get you some gifts next time we see each other!")
			you_winner()



def you_loser():
	print("You lose! Wow, you're bad at making friends...")
	player_input = 'q'

def you_winner():
	print("You won! You're great at making friends!")
	print("CREDITS:\nProgrammer: Acacia Coombs\n Developer: Acacia Coombs\nEditor: Acacia Coombs\nThe Best Person Ever: Acacia Coombs\n\nThanks for playing!")
		

if __name__ == "__main.py__":
	main()
