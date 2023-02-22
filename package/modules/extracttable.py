# Imports
try:
  import rsa
  import os
  import binascii
  import time
  import random
  import datetime
  from colorama import Fore, Style
except:
  print("Error: Missing required modules. Please install the following modules: rsa, datetime, time, colorama and random")

try:
  from randomhex import createDigest
  from filterfile import filterFile
  from clearconsole import clearConsole
  from extractlist import extractList
  from extracttable import extractTable
except:
  print("Error: Missing required program files, ensure that the following files are present: randomhex.py, clearconsole.py, filterfile.py, extractlist.py and extracttable.py")


# Global Variables
class Files():
  logFile = str("C:/logs/python/Data-Extraction")
  modulePath = str("C:/Users/" + os.getlogin() + "/AppData/Local/Programs/Python/Libs")
  filterFile = str(modulePath + "/data-extraction/modules/filterfile.py")
  extractList = str(modulePath + "/data-extraction/modules/extractlist.py")
  extractTable = str(modulePath + "/data-extraction/modules/extracttable.py")
  randomHex = str(modulePath + "/data-extraction/modules/randomhex.py")
  
class errorMessages():
  error = str("ERROR: An unknown error has occured.")
  fileUnreadable = str("ERROR: The file given cannot be read.")
  fileEmpty = str("ERROR: The given file is empty and contains no data.")
  insufficientPerm = str("ERROR: The file cannot be accessed due to insufficient permissions.")
  fileExists = str("ERROR: The file does not exist/the path can't be found.")
  fileOpen = str("ERROR: The file cannot be opened due to it being in use by another process.")   

user = str(os.getlogin())
sleep = time.sleep(3)
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n"

# Functions
def extractTable():
  pass