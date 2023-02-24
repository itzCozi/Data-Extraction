# This is a module for easy logging in python this will also be implemented in standalone
try:
  import datetime
  import random
  import os
  import time
  import hashlib
  from threading import Thread
  from colorama import Fore, Style
except ImportError:
  print("Error: Missing module(s) please install the following module(s): colorama, datetime and hashlib.")


# Global variables
class errorMessages():
  error = str("ERROR: An unknown error has occured.")
  fileUnreadable = str("ERROR: The file given cannot be read.")
  fileEmpty = str("ERROR: The given file is empty and contains no data.")
  insufficientPerm = str("ERROR: The file cannot be accessed due to insufficient permissions.")
  fileExists = str("ERROR: The file does not exist/the path can't be found.")
  fileOpen = str("ERROR: The file cannot be opened due to it being in use by another process.")   

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n"


# Functions
def bruteforce(target):
  # Still in development
  thread = Thread(target = bruteforce, args = ())
  staticList = []
  targetList = []
  for character in target:
    targetList.append(character)
    staticList.append(character)
  for i in range(20, 100):
    random.shuffle(targetList)
  
  print("Starting brute force attack on target: " + str(targetList))
  time.sleep(3)
  thread.start()
  
  while targetList != staticList:
    random.shuffle(targetList)
    print(''.join(targetList))
    if targetList == target:
      thread.join()
      break
  print(targetList)
  input("Press enter to exit... ")
  
bruteforce()