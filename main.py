import os
import time
from random import randint
import animations
import sys

def docs():
  animations.create.create_typewriter("This text animation in made doing 'animations.create.create_typewriter(text, 0.25, animations.colors.RED, 'rainbow')' ", 0.05, animations.colors.RED, 'rainbow')
  animations.create.create_typewriter("In the next version, i will add more styles! But, lets see other features!", 0.05, animations.colors.CYAN, 'default')
  input(" ")
  os.system('clear')
  animations.create.create_typewriter("This one is cool! You can create a moving rocket! Doing this... 'animations.otherAnimations.rocket(0.05, 2)' Press enter to see the animation.", 0.05, animations.colors.PURPLE, 'default')
  input(" ")
  animations.otherAnimations.rocket(0.10, 2)
  input("Continue by pressing enter...")
  animations.textAnimations.typewriter("By doing this: 'animations.otherAnimations.space_invader()' you will be able to create a moving spaceship. Press enter to see the animation.", 0.05)
  input(" ")
  os.system('clear')
  animations.otherAnimations.space_invader(0.05, 10)
  os.system('clear')
  animations.textAnimations.typewriter("You can also customize them more! Using this: 'animations.create.create_rocket/create_spaceship/create_typewriter(0.05, 5, spaceship/rocket_top, rocket_middle, spaceship/rocket_bottom)' more detailed in docs.md (You can view it in the proyect files)", 0.05)
  input(" ")
  os.system('clear')
  animations.textAnimations.typewriter("You can also use 'animations.textAnimations.loadingText' to create this cool loading effect:", 0.05)
  input("")
  os.system('clear')
  animations.textAnimations.loadingText("Example... ", 0.05)
  animations.textAnimations.loadingText("Example... ", 0.05)
  animations.textAnimations.loadingText("Example... ", 0.05)
  input("")
  os.system('clear')
  animations.textAnimations.typewriter("You can also use this 'animations.otherAnimations.progress_bar('Optional Text', '=', 10)' to make a working and customizable loading bar!", 0.05)
  animations.otherAnimations.progress_bar('Optional Text', '=', 10)
  os.system('clear')
  animations.textAnimations.typewriter("That's it! Thank you for reading this! If you want to see more, go to docs.md in the files!", 0.05)
  input(" ")
  os.system('clear')
  animations.textAnimations.loadingText("Closing proyect file...", 0.05)

animations.textAnimations.typewriter("Hey everyone! I created a library for text animations and other cool animations. This text animation is from it. Fork this file or copy the code into a file called 'animations.py' and put 'import animations' in the start of your main python code. If you want to know more about it, press enter.", 0.05)
input(" ")
os.system('clear')
docs()
#animations.create.create_rocket(0.5, 3, "︿", "||", "︻")
