# Imports
try:
  import rsa
  import os
  import string
  import binascii
  import hashlib
  import time
  import random
  import datetime
  from sys import platform
  from colorama import Fore, Style
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
keyValue = random.randint(90, 300)
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n"


# Functions
def CC():
  if platform == "linux" or platform == "linux2":
    os.system("clear")
  else:
    os.system("cls")
    

def extractList(file):
  with open(file, "r") as f:
    data = f.read()
    splitData = data.split('\n')
    f.close()
  
  print(splitData)
  return splitData


def randnum():
  rand = random.randint(100, 100000)
  rand2 = random.randint(100, 1000)
  foo_rand = int(rand) * int (rand)
  moo_rand = int(foo_rand) - int(rand2)
  bar_rand = int(moo_rand) + int(rand)
  
  return bar_rand


def extractTable(file):
  returnIteam = []
  with open(file, "r") as f:
    for line in f:
      data = f.read()
      extractedList = data.split('  ')
      extractData = ' '.join(extractedList)
      reformedData = str(extractData).split('\n')
      returnIteam.append(reformedData)

    print(returnIteam)
    return returnIteam
  

def filterFile(file, blklistword):
  with open(file, "r+") as f:
    for line in f:
      fline = line.split(' ')
      for word in fline:
        if word is blklistword:
          newline = line.replace(word, "")
          f.seek(word)
          f.write(newline)
        else:
          print("Word not found in file.")

        return fline
      
      
def createDigest():
  publicKey, privateKey = rsa.newkeys(keyValue)
  encMessage = rsa.encrypt(str(random.randint(1,10)).encode(), publicKey)
  hexMessage = binascii.hexlify(encMessage)
  bar = str(hexMessage).replace("'", '')
  foo = str(bar).replace('b', '')

  return foo



class hash():
  def keypair(print=None):
    threshold = random.randint(2, 8)
    buff = random.randint(10, 10000)
    length = random.randint(50, 400)
    iterable = 0
    tiny = random.uniform(0.001, 0.999)
    alphabet = string.ascii_letters + string.digits
    publicBase = '.'.join(random.choice(alphabet) for i in range(buff))
    privateBase = '.'.join(random.choice(alphabet) for i in range(buff))

    time.sleep(tiny)

    publicList = publicBase.split('.')
    privateList = privateBase.split('.')

    while iterable != threshold:
      x = privateList + publicList
      y = publicList + privateList
      for iteam in x, y:
        random.shuffle(x)
        random.shuffle(y)
      iterable += 1

    time.sleep(tiny)
  
    publicKey = ''.join(random.choice(x) for iterable in range(length))
    privateKey = ''.join(random.choice(y) for iterable in range(length))

    if print is print:
      print(publicKey)
      print("")
      print(privateKey)
    else:
      return publicKey, privateKey

  def hashfile(file):
    BUF_SIZE = os.path.getsize(file)

    sha256 = hashlib.sha256()

    with open(file, 'rb') as f:
     while True:
        data = f.read(BUF_SIZE)

        if not data:
          break

    sha256.update(data)
    return sha256.hexdigest()

  def comparehash(hashA, hashB):
    if hashA is hashB:
      return True
    else:
      return False
  
  def secure(key):
    keyLength = len(key)
    keyList = list(key)
    olprime = random.randint(3, 8)
    buff = random.randint(200, 1000)
    alphabet = string.ascii_letters + string.digits + string.digits
    randomkey = list(random.choice(alphabet) for i in range(buff))

    for z in range(olprime):
      random.shuffle(keyList)
      random.shuffle(keyList)
      print(z)
      bar = keyList + randomkey
      for i in bar:
        random.shuffle(bar)

    newkey = ''.join(random.choice(bar) for i in range(keyLength))

    newList = list(newkey)

    for y in range(olprime):
      random.shuffle(randomkey)
      random.shuffle(randomkey)

    for x in range(olprime):
      random.shuffle(newList)
      random.shuffle(newList)
      print(x)
      foo = randomkey + newList
      for i in foo:
        random.shuffle(foo)

    returnKey = ''.join(random.choice(foo) for i in range(keyLength))

    return returnKey
  
  
  
class Ptime():
  # Class variables
  now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n"
  time = datetime.datetime.now().strftime("%H:%M:%S") + "\n\n"
  date = datetime.datetime.now().strftime("%Y-%m-%d") + "\n\n"
  
  
  def nowtime(time=None, date=None):
    if time is False or date is True:
      return datetime.datetime.now().strftime("%Y-%m-%d") + "\n\n"
    if time is True or date is False:
      return datetime.datetime.now().strftime("%H:%M:%S") + "\n\n"
    else:
      return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n"
  
  def currentdate():
    return datetime.datetime.now().strftime("%Y-%m-%d") + "\n\n"

  def currenttime():
    return datetime.datetime.now().strftime("%H:%M:%S") + "\n\n"
  
  

class easylog():
  def eventlog(message, file):
    if os.path.exists(file):
      with open(file, "w") as fin:
        fin.write(message + " - AT: " + now)
        fin.close()
    else:
      print(errorMessages.fileExists)
      raise FileNotFoundError
  
  def errorlog(message, file):
    if os.path.exists(file):
      with open(file, "w") as fin:
        fin.write("ERROR: " + message + " - AT: " + now)
        fin.close()
      print(Fore.RED + "ERROR: " + message + Style.RESET_ALL)
    else:
      print(errorMessages.fileExists)
      raise FileNotFoundError

  def userlog(message):
    print(Fore.BLUE + "LOG: " + Fore.GREEN + message + Style.RESET_ALL)
    time.sleep(3)
    

