# First, I typed import random so I could use the random module.
print("Welcome to da Honey Heist Bearacter Generator")
personality_of_bear = ("Rookie", "Washed up", "Retired", "Unhinged", "Slick", "Incompetent")
bear_type = ("Grizzly Bear", "Polar Bear", "Panda", "Black Bear", "Sun Bear", "Honey Badger")
criminal_role_of_bear = ("Enforcer", "Mastermind", "Getaway Driver", "Hacker", "Thief", "Face")
# I need to add user input to start the process.
input("Press ENTER to create a new character, capeesh?")
print()
import random
stat1 = random.choice(personality_of_bear)
stat2 = random.choice(bear_type)
stat3 = random.choice(criminal_role_of_bear)
print("Badda-BOOM! You're part of the gang now, ya filthy animal!")
print()
print("Ya know, you remind me of my brudda. He was also a stinkin':")
print(stat1), print(stat2), print(stat3)

# TODO: Create a finish screen.
#       Create a screen with "roll" button to replace current enter prompt. 
