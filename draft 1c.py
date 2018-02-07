# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 13:53:33 2018

@author: marks

First, I typed import random so I could use the random module.
"""
import random
"""
Next, I created the variable 'descriptor' and populated it with the 6 options
"""
descriptor = ("Rookie", "Washed up", "Retired", "Unhinged", "Slick", "Incompetent")
"""
I created the 'backstory' variable which is the outcome of 'descriptor' with random.choice applied.
Then I asked python to print the result. 
"""
backstory = random.choice(descriptor)
print(backstory)

"""
I still need to:
    add the other 2 bear stat categories
    script a command to run the whole series of expressions
    create a start and finish screen.
"""
