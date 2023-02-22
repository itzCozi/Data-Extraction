# Imports
import rsa
import os
import binascii
import random

# Global Variables
class Files():
  logFile = str("C:/logs/python/Data-Extraction")
  modulePath = str("C:/Users/" + os.getlogin() + "/AppData/Local/Programs/Python/Libs")
  filterFile = str(modulePath + "/data-extraction/modules/filterfile.py")
  extractList = str(modulePath + "/data-extraction/modules/extractlist.py")
  extractTable = str(modulePath + "/data-extraction/modules/extracttable.py")
  randomHex = str(modulePath + "/data-extraction/modules/randomhex.py")

keyValue = random.randint(90, 300)
user = str(os.getlogin())


# Functions
def createDigest():
  publicKey, privateKey = rsa.newkeys(keyValue)
  encMessage = rsa.encrypt(str(random.randint(1,10)).encode(), publicKey)
  hexMessage = binascii.hexlify(encMessage)
  bar = str(hexMessage).replace("'", '')
  foo = str(bar).replace('b', '')

  return foo
