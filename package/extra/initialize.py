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
  os.system("pip install -r requirements.txt")

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
def checks():

  # Check file status
  try:
   testLog = open(Files.logFile, "r")
   testFilter = open(Files.filterFile, "r")
   testList = open(Files.extractList, "r")
   testTable = open(Files.extractTable, "r")
   testhex = open(Files.randomHex, "r")
  except IOError:
    print(errorMessages.fileOpen)
    raise errorMessages.fileOpen

  # File checks
  if os.exists(Files.modulePath) == False:
    os.mkdir(Files.modulePath)
  if os.exists(Files.logFile) == False:
    open(Files.logFile, "x")
  if os.exists(Files.filterFile) == False:
    open(Files.filterFile, "x")
  if os.exists(Files.extractList) == False:
    open(Files.extractList, "x")
  if os.exists(Files.extractTable) == False:
    open(Files.extractTable, "x")
  if os.exists(Files.randomHex) == False:
    open(Files.randomHex, "x")
  else:
    with open(Files.logFile, "a") as log:
      log.write("All files exist and are readable - AT: " + now)
    pass


    