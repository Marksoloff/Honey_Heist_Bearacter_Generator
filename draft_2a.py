# First, I typed import random so I could use the random module.
import random
print("Welcome to da Honey Heist Bearacter Generator")
personality_of_bear = ("Rookie", "Washed up", "Retired", "Unhinged", "Slick", "Incompetent")
bear_type = ("Grizzly Bear", "Polar Bear", "Panda", "Black Bear", "Sun Bear", "Honey Badger")
criminal_role_of_bear = ("Enforcer", "Mastermind", "Getaway Driver", "Hacker", "Thief", "Face")
# user input to starts the process.
input("Press ENTER to create a new character, capeesh?")
print()

stat1 = random.choice(personality_of_bear)
stat2 = random.choice(bear_type)
stat3 = random.choice(criminal_role_of_bear)
print("Badda-BOOM! Hey get a load of you, ya stinkin':")
print()
print(stat1), print(stat2), print(stat3)
print()
input("Welcome to the gang, ya filthy animal! Let's figure out your bear name. Hit ENTER, okay?")
# TODO: Create a finish screen.
#       Create a screen with "roll" button to replace current enter prompt. 

# First & Last name strings to randomize
boy_name = ("Bugsy", "Artie", "Mooksie", "Petey", "Vinnie", "Lou", "Mungo", "Mack", "Tony", "Teddy", "Bobo", "Chucky", "Bobby", "Lucio", "Musky", "Sticks", "Clawsy", "Yogi")
girl_name = ("Ursula", "Coco", "Wendy", "Velvet", "Betty", "Mama", "Louisa", "Belladonna", "Carmen", "Jaimie", "Veronica", "Squeaky", "Bang-Bang", "Cookies", "Delores")
asex_name = ("Pittsburgh", "Brumbo", "Binky", "Stabs", "Punchy", "Husky", "Shortstack", "Pookie", "Bing Bing", "Clawsy", "Dead-eye", "Knuckles", "Mookie", "Sneaky", "Two-toes", "Shades", "Bully", "Meatsy", "Chuckles", "Bingo", "Pat")    
surname = ("Malone", "LeRoy", "Falcone", "O'Malley", "Pitsacotta", "Rourke", "Putanesca", "the Chopper", "MacKenzie", "the Knife", "Fujimora", "Tanaka", "the Vermin of Scarsdale")    

# Variable names assigned to randomly selected names 
rando_boy_name1 = random.choice(boy_name)
rando_girl_name1 = random.choice(girl_name)
rando_asex_name1 = random.choice(asex_name)
rando_surname = random.choice(surname)

# Nested If statements narrow user's name options 
gendered = input ("Ey, I been wonderin'... Does your bear have a gender?: Y/N?")
if gendered.upper() == "N":
    print("Ah, what's gender anyways but a social construct?\n")
    input("Hit ENTER again and I'll cook up a real crackerjack of a name for ya.")
    print("And your name is: " + rando_asex_name1 + " " + rando_surname +"!")   

if gendered.upper() == "Y":
    print("Okee doke!")
    male_or_fem = input ("Is your bear male or female? M/F? \n")
    
    if male_or_fem.upper() == "M":
        print("Nice to meetcha, pal!")
        input("Hit ENTER again and I'll cook up a real crackerjack name for ya. \n")
    
    if male_or_fem.upper() == "F":
        print("Pleased to meetcha miss. Charmed, I'm sure.")
        input("Hit ENTER again and I'll cook up a real crackerjack name for ya.\n")
    
    if male_or_fem.upper() == "M":
        print("And your name is: " + rando_boy_name1 + " " + rando_surname +"!")
    if male_or_fem.upper() == "F":
        print("And your name is: " + rando_girl_name1 + " " + rando_surname +"!")
print("Mazel tov, kid.")

