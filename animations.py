import os
import time
import random
import sys

class colors:
    BLACK = "\033[0;30m";
    RED = "\033[0;31m";     
    GREEN = "\033[0;32m";    
    YELLOW = "\033[0;33m";   
    BLUE = "\033[0;34m";     
    PURPLE = "\033[0;35m";   
    CYAN = "\033[0;36m";     
    WHITE = "\033[0;37m";   
    HEADER = '\033[95m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class create:
  def create_typewriter(text, speed, textColor, style):
    if style == "default":
      for letter in text:
        print(textColor + letter, end="")
        sys.stdout.flush()
        time.sleep(speed)
    if style == "rainbow":
      letters = 0
      for letter in text:
        letters += 1
      for letter in text:
        letters -= 1
        rainbow = ['\033[0;31m', '\033[0;32m', '\033[0;33m', '\033[0;34m', '\033[0;35m', '\033[0;36m', '\033[0;37m', '\033[0;1m']
        rnd = random.choice(rainbow)
        print(rnd + letter, end="")
        sys.stdout.flush()
        time.sleep(speed)
      if letters < 1:
        print(colors.WHITE + ' ') #resets colors
  def create_spaceship(speed, loops, spaceship_top, spaceship_bottom):
    distance_from_top = 0
    distance_from_left_side = 0
    step = 1
    looping = True
    while looping:
      print("\n" * distance_from_top)
      print((" " * distance_from_left_side) + str(spaceship_top))
      print((" " * distance_from_left_side) + str(spaceship_bottom))
      distance_from_left_side += step
      if distance_from_left_side > 20 or distance_from_left_side <= 0:
        step = -step 
        distance_from_top += 2
        if loops < 1:
          looping = False
        if distance_from_top > 20:
          loops =- 1
          distance_from_top = 0
          distance_from_left_side = 0
          step = 1
      time.sleep(speed)
      os.system('clear')
  def create_rocket(speed, loops, rocket_top, rocket_middle, rocket_bottom):
    if loops == None:
      loops = 2
    looping = True
    distance_from_top = 20
    while looping:
      if loops == 0:
        looping = False
      print("\n" * distance_from_top)
      print(f"          {rocket_top}        ")
      print(f"          {rocket_middle}        ")
      print(f"          {rocket_middle}        ")
      print(f"          {rocket_bottom}        ")
      time.sleep(speed)
      os.system('clear')  
      distance_from_top -= 1
      if distance_from_top < 0:
        loops -= 1
        distance_from_top = 20

class textAnimations:
  def loadingText(text, speed):
    print(text, end='', flush=True)
    for x in range(3):
      for frame in r'-\|/-\|/':
        # Back up one character then print our next frame in the animation
          print('\b', frame, sep='', end='', flush=True)
          time.sleep(speed)
    print('\b ')

  def typewriter(text,speed):
    for letter in text:
      print(letter, end="")
      sys.stdout.flush()
      time.sleep(speed)

class otherAnimations:
  def progress_bar(optionalText, loadingSymbol, seconds):
    for progress in range(0,seconds+1):
      percent = (progress * 100) // seconds
      print("\n")
      print(optionalText)
      print("<" + (loadingSymbol * progress) + (" " * (seconds-progress)) + "> " + str(percent) + "%")
      print("\n")
      time.sleep(1)
      os.system('clear') 
  
  def rocket(speed, loops):
    if loops == None:
      loops = 2
    looping = True
    distance_from_top = 20
    while looping:
      if loops == 0:
        looping = False
      print("\n" * distance_from_top)
      print("          /\        ")
      print("          ||        ")
      print("          ||        ")
      print("         /||\        ")
      time.sleep(speed)
      os.system('clear')  
      distance_from_top -= 1
      if distance_from_top < 0:
        loops -= 1
        distance_from_top = 20
  def space_invader(speed, loops):
    distance_from_top = 0
    distance_from_left_side = 0
    step = 1
    looping = True
    while looping:
      print("\n" * distance_from_top)
      print((" " * distance_from_left_side) + "_^_")
      print((" " * distance_from_left_side) + "/|\\")
      distance_from_left_side += step
      if distance_from_left_side > 20 or distance_from_left_side <= 0:
        step = -step 
        distance_from_top += 2
        if loops < 1:
          looping = False
        if distance_from_top > 20:
          loops =- 1
          distance_from_top = 0
          distance_from_left_side = 0
          step = 1
      time.sleep(speed)
      os.system('clear') 