import sys, os
sys.path.append("c:/users/" + os.getlogin() + "/scoop/apps/python/current/lib/site-packages/dataextract")

# Imports
try:
  import rsa
  import binascii
  import time
  import random
  import datetime
except:
  print("Error: Missing required modules. Please install the following modules: rsa, datetime, time, colorama and random")


# Global Variables
class Files():
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
keyValue = random.randint(90, 300)


# Functions
def createDigest():
  publicKey, privateKey = rsa.newkeys(keyValue)
  encMessage = rsa.encrypt(str(random.randint(1,10)).encode(), publicKey)
  hexMessage = binascii.hexlify(encMessage)
  bar = str(hexMessage).replace("'", '')
  foo = str(bar).replace('b', '')

  return foo

