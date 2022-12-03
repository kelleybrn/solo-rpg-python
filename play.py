# import statements
from random import randint

# arrays of options

scene_complication = ["Hostile forces oppose you", "An obstacle blocks your way", "Wouldn't it suck if...", "An NPC acts suddenly", "All is not as it seems", "Things actually go as planned"]

altered_scene = ["A major detail of the scene is somehow enhanced or made worse", "The environment is different", "Unexpected NPCs are present", "Add a SCENE COMPLICATION", "Add a PACING MOVE", "Add a RANDOM EVENT"]

# ORACLE (YES/NO)
# When you need to ask a simple question, choose the likelihood and roll 2d6.
yn_answer = ["Likely: Yes on 3+", "Even: Yes on 4+", "Unlikely: Yes on 5+"]

yn_mod = ["but...", "", "", "", "", "and..."]

pacing_move = ["Foreshadow Trouble", "Reveal a New Detail", "An NPC Takes Action", "Advance a Threat", "Advance a Plot", "Add a RANDOM EVENT to the scene"] 

failure_move = ["Cause Harm", "Put Someone in a Spot", "Offer a Choice", "Advance a Threat", "Reveal an Unwelcome Truth", "Foreshadow Trouble"]

oracle_how = ["Surprisingly lacking", "Less than expected", "About average", "About average", "More than expected", "Extraordinary"]

action_focus = ["Seek", "Oppose", "Communicate", "Move", "Harm", "Create", "Reveal", "Command", "Take", "Protect", "Assist", "Transform", "Deceive"]

detail_focus = ["Small", "Large", "Old", "New", "Mundane", "Simple", "Complex", "Unsavory", "Specialized", "Unexpected", "Exotic", "Dignified", "Unique"]

topic_focus = ["Current need", "Allies", "Community", "History", "Future Plans", "Enemies", "Knowledge", " Rumors", "A plot arc", "Recent events", "Equipment", "A faction", "The PCs"]
     
objective = ["Eliminate a threat", "Learn the truth", "Recover something valuable", "Escort or deliver to safety", "Restore something broken", "Save an ally in peril"]

adversaries = ["A powerful organization", "Outlaws", "Guardians", "Local inhabitants", "Enemy horde or force", "A new or recurring villain"]

rewards = ["Money or valuables", "Money or valuables", "Knowledge and secrets", "Support of an ally", "Advance a plot arc", "A unique item of power"]

identity = ["Outlaw", "Drifter", "Tradesman", "Commoner", "Entertainer", "Adherent", "Leader", "Mystic", "Adventurer", "Lord", "Soldier", "Merchant ", "Specialist"]

suit = ["Heart: Social (personal, connection", "Spades: Mystical (meaning, capability)", "Diamonds: Technical (mental, operation", "Clubs: Physical (appearance, existence)"]

goal = ["Enrich Self", "Avenge", "Fulfill Duty", "Escape", "Create", "Serve", "Obtain", "Learn", "Harm", "Restore", "Find", "Travel", "Protect"]

notable_feature = ["Unremarkable", "Notable nature", "Obvious physical trait", "Quirk or mannerism", "Unusual equipment", "Unexpected age or origin"]

location = ["Typical area", "Transitional area", "Living area or meeting place", "Working or utility area", "Area with a special feature", "Location for a specialized purpose"]

encounter = ["None", "None", "Hostile enemies", "Hostile enemies", "An obstacle blocks the way", "Unique NPC or adversary"]

obj = ["Nothing, or mundane objects ", "Nothing, or mundane objects", "An interesting item or clue", "A useful tool, key, or device", "Something valuable", "Rare or special item"]

total_exits = ["Dead end", "Dead end", "1 additional exit", "1 additional exit", "2 additional exits", "2 additional exits"]

actions = [""]

# TODO: Turn this into a menu with number options
def menu():
	print("Welcome to the Python Solo Engine! The tables are based on the One Page Solo Engine [URL]")
	print("Input options once the game starts:")
	print("- Quit")
	print("- Menu (displays game input options")
	print("- Set the scene")
	print("- End turn (ends the current player's turn and begins the next one)")
	print("- Roll some dice")
	print("- Generate an adventure hook")
	print("- Generate a dungeon")
	print("- Generate next area in a dungeon")
	print("- Generate a random event")
	print("- Generate an NPC")
	print("- Pacing move (GM move)")
	print("- Failure move (GM move)")
	print("- Ask a yes or no question (Oracle question, Yes/No")
	print("- Ask an Oracle question - How (Oracle question, How")
	print("- Ask a complex question (Oracle question, Focus")
	print("Or, enter any additional text at the prompt in order to add supplementary details, record your interpretation of the results, or just record your gameplay!")
	print("")
	breakout = input("Enter any text to continue: ")

def quit():
	print("Farewell, traveler!")
	exit

def roll_dice(n):
	rollx = randint(1,n)
	return(rollx)

def roll_dice_2(x, y):
	total = 0
	all_rolls = []
	for n in range(0, x):
		rollx = randint(1, y)
		total += rollx
		all_rolls.append(rollx)
	print("All rolls: " + str(all_rolls))
	print("Sum of rolls: " + str(total))
	return

def generate(arr):
	rollx = randint(0, len(arr) - 1)
	result = arr.pop(rollx)
	return result

def is_altered_scene():
	is_altered_scene = 0
	roll = randint(1,6)
	if roll < 5:
		is_altered_scene = 0
	else:
		is_altered_scene = 1
	return is_altered_scene

def random_event():
	action = generate(action_focus)
	topic = generate(topic_focus)
	print("Action: " + action)
	print("Topic: " + topic)

def oracle_yn(likelihood):
	answer = ""
	mod = ""
	odds = roll_dice(6)
	if (likelihood == "likely" or likelihood == "Likely"):
		if odds >= 3: 
			answer = "Yes"
		else:
			answer = "No"
	elif (likelihood == "even" or likelihood == "Even"):
		if odds >= 4: 
			answer = "Yes"
		else:
			answer = "No"
	elif (likelihood == "unlikely" or likelihood == "Unlikely"):
		if odds >= 5: 
			answer = "Yes"
		else:
			answer = "No"
	else:
		print("Please input one of the following options: Likely, Unlikely, or Even.")
	
	mod_roll = roll_dice(6)
	if mod_roll == 1:
		mod = "But..."
	elif mod_roll < 6:
		mod = ""
	elif mod_roll == 6: 
		mod = "And..."
	else:
		"Error: Something happened"
	print(answer + ". " + mod)
	return

user_input = ""

# display welcome message
menu()
user_input = input("What would you like to do?: ")

# still need to deal with how to quit and if we need quit logic on both ends (yuck. pfaugh. hiss.)
while user_input != "Quit":
	match user_input:
		
		case "Menu":
			# TODO
			menu()
			user_input = input("What would you like to do?: ")

		case "End turn":
			print("")
			print("")
			print("The current player's turn ends.")
			next_player = input("Please enter the next player's name (e.g. player or GM): ")
			print(next_player + "'s turn begins.")
			print("")
			print("")
			user_input = input("What would you like to do?: ")
		
		case "Set the scene":
			print("")
			print("")
			input("Describe what your character is trying to accomplish: ")
			print("Your scene complication is: " + generate(scene_complication))
			is_it_altered_scene = is_altered_scene()
			if is_it_altered_scene:
				print("Your scene is altered by: " + generate(altered_scene))
			print("")
			print("")
			user_input = input("What else would you like to do?: ")
		
		case "Ask a yes or no question":
			print("")
			print("")
			question_yn = input("Ask a yes or no question of the Oracle, e.g. 'Is it likely/unlikely/even odds that...': ")
			potentiality = (input("Confirm the likelihood you want to ascertain, (unlikely, likely, or even)"))
			print("")
			oracle_yn(potentiality)
			print("")
			print("")
			user_input = input("What else would you like to do?: ")
		
		case "Ask an Oracle question - How":
			print("")
			print("")
			question_how = input("Ask a question of the Oracle about how big/good/bad/strong/numerous/etc. something is: ")
			print("")
			print(generate(oracle_how))
			print("")
			print("")
			user_input = input("What else would you like to do?: ")
		
		case "Pacing move":
			# broken
			print("")
			print("")
			print(generate(pacing_move))
			print("")
			print("")
			user_input = input("What else would you like to do?: ")
		
		case "Failure move":
			# broken
			print("")
			print("")
			print(generate(failure_move))
			print("")
			print("")
			user_input = input("What else would you like to do?: ")
		
		case "Generate a random event":
			print("")
			print("")
			random_event()
			print("")
			print("")
			user_input = input("What else would you like to do?: ")
		
		case "Ask a complex question":
			print("")
			print("")
			input("Type in your question: ")
			focus_type = input("Choose the appropriate focus table for your question (Action focus, Detail focus, or Topic focus): ")
			if focus_type == "Action focus":
				print("")
				print("")
				print("Action focus: " + generate(action_focus))
				print("Domain: " + generate(suit))
			elif focus_type == "Detail focus":
				print("")
				print("")
				print("Action focus: " + generate(detail_focus))
				print("Domain: " + generate(suit))
			elif focus_type == "Topic focus":
				print("")
				print("")
				print("Action focus: " + generate(topic_focus))
				print("Domain: " + generate(suit))
			else:
				print("Please input one of the three options: Action focus, Detail focus, or Topic focus")
			print("")
			print("")
			print("If the question is not sufficiently answered, try adding results from a second focus roll")
			user_input = input("What else would you like to do?: ")


		case "Generate an adventure hook":
			print("")
			print("")
			print("Objective: " + generate(objective))
			print("Adversaries: " + generate(adversaries))
			print("Rewards: " + generate(rewards))
			print("")
			print("")
			user_input = input("What else would you like to do?: ")
		
		case "Generate an NPC":
			print("")
			print("")
			print("Identity: " + generate(identity))
			print("Goal: " + generate(goal))
			print("Notable feature: " + generate(detail_focus) + ", " + generate(notable_feature))
			print("Attitude to PCs: " + generate(oracle_how))
			print("Conversation: " + generate(topic_focus))
			print("")
			print("")
			user_input = input("What else would you like to do?: ")
		
		case "Generate a dungeon":
			print("")
			print("")
			print("Dungeon theme: ")
			print("How it looks: " + generate(detail_focus))
			print("How it is used: " + generate(action_focus))
			print("")
			print("The first location in the dungeon has 3 exits and: ")
			print("Location/usage: " + generate(location))
			print("Encounter?: " + generate(encounter))
			print("Any objects?: " + generate(obj))
			print("")
			print("")
			user_input = input("What else would you like to do?: ")
		
		case "Generate next area in the dungeon":
			# broken
			print("")
			print("")
			print("Location/usage: " + generate(location))
			print("Encounter?: " + generate(encounter))
			print("Any objects?: " + generate(obj))
			print("This area has " + generate(total_exits))
			print("")
			print("")
			user_input = input("What else would you like to do?: ")
		
		case "Roll some dice":
			print("")
			print("")
			dice = input("Enter the number of sides on the die & how many times you'd like to roll, e.g. 4d8: ")
			roll_dice_2(int(dice[0]), int(dice[2]))
			print("")
			print("")
			user_input = input("What else would you like to do?: ")
		
		case _:
			print("")
			print("")
			print(user_input)
			print("")
			print("")
			user_input = input("And then what?: ")

if user_input == "Quit":
	quit()