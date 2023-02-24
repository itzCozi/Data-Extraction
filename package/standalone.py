# Imports
try:
  import rsa
  import os
  import sys
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

class colorCodes():
  black = int(0);
  blue = int(1);
  green = int(2);
  aqua = int(3);
  red = int(4);
  purple = int(5);
  yellow = int(6);
  white = int(7);
  grey = int(8);
  light_blue = int(9);
  light_green = str('A');
  light_aqua = str('B');
  light_red = str('C');
  light_purple = str('D');
  light_yellow = str('E');
  bright_white = str('F');

def ResetAll():
  os.system("Color " + colorCodes.black + colorCodes.white)
def clear():
  if platform == "linux" or platform == "linux2":
    os.system("clear")
  else:
    os.system("cls")

user = str(os.getlogin())
sleep = time.sleep(3)
keyValue = random.randint(90, 300)
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n"


# Initialisation
sys.path.append("C:/Users/" + os.getlogin() + "/scoop/apps/python/current/Lib/site-packages")


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


def tick(inc, args=None):
  tickVar = 0
  argB = "set"
  argC = "reset"
  
  if args == argB:
    tickVar += inc
    print(tickVar)
  if args == argC:
    tickVar = 0
    print(tickVar)
  else:
    tickVar += inc
    
  return tickVar



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
  with open(file, "r+") as fin:
    content = fin.read()
    if content.find(blklistword) is True:
      writeIteam = content.replace(blklistword, "")
      fin.write(writeIteam)
      fin.close()
    else:
      pass
      
      
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

  def hash(target, print=None):
    sha256 = hashlib.sha256()
    xO = random.randint(10, 200)
    targetConvert = list(target)
    for i in range(xO):
      random.shuffle(targetConvert)

    targetShuffled = ''.join(targetConvert)
    sha256.update(targetShuffled.encode())

    if print != None: 
      print(sha256.hexdigest())
    else:
      return sha256.hexdigest()

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
    

class text():
  def Black():
    os.system("Color " + str(colorCodes.black))
  def Blue():
    os.system("Color " + str(colorCodes.blue))
  def Green():
    os.system("Color " + str(colorCodes.green))
  def Aqua():
    os.system("Color " + str(colorCodes.aqua))
  def Red():
    os.system("Color " + str(colorCodes.red))
  def Purple():
    os.system("Color " + str(colorCodes.purple))
  def Yellow():
    os.system("Color " + str(colorCodes.yellow))
  def White():
    os.system("Color " + str(colorCodes.white))
  def Grey():
    os.system("Color " + str(colorCodes.grey))
  def Lightblue():
    os.system("Color " + str(colorCodes.light_blue))
  def Lightgreen():
    os.system("Color " + str(colorCodes.light_green))
  def Lightaqua():
    os.system("Color " + str(colorCodes.light_aqua))
  def Lightred():
    os.system("Color " + str(colorCodes.light_red))
  def Lightpurple():
    os.system("Color " + str(colorCodes.light_purple))
  def Lightyellow():
    os.system("Color " + str(colorCodes.light_yellow))
  def Brightwhite():
    os.system("Color " + str(colorCodes.light_white))
  
  def Reset():
    os.system("Color " + int(colorCodes.black))
  def clear():
    if platform == "linux" or platform == "linux2":
      os.system("clear")
    else:
      os.system("cls")
  
  
class background():
  def Black():
    os.system("Color " + str(colorCodes.black + colorCodes.white))
  def Blue():
    os.system("Color " + str(colorCodes.blue + colorCodes.white))
  def Green():
    os.system("Color " + str(colorCodes.green + colorCodes.white))
  def Auqa():
    os.system("Color " + str(colorCodes.aqua + colorCodes.white))
  def Red():
    os.system("Color " + str(colorCodes.red + colorCodes.white))
  def Purple():
    os.system("Color " + str(colorCodes.purple + colorCodes.white))
  def Yellow():
    os.system("Color " + str(colorCodes.yellow + colorCodes.white))
  def White():
    os.system("Color " + str(colorCodes.white + colorCodes.black))
  def Grey():
    os.system("Color " + str(colorCodes.grey + colorCodes.black))
  def Lightblue():
    os.system("Color " + str(colorCodes.light_blue + colorCodes.white))
  def Lightgreen():
    os.system("Color " + str(colorCodes.light_green + colorCodes.white))
  def Lightaqua():
    os.system("Color " + str(colorCodes.light_aqua + colorCodes.white))
  def Lightred():
    os.system("Color " + str(colorCodes.light_red + colorCodes.white))
  def Lightpurple():
    os.system("Color " + str(colorCodes.light_purple + colorCodes.white))
  def Lightyellow():
    os.system("Color " + str(colorCodes.light_yellow + colorCodes.white))
  def Brightwhite():
    os.system("Color " + str(colorCodes.light_white + colorCodes.white))
  
  def Reset():
    os.system("Color " + str(colorCodes.black))
  def clear():
    if platform == "linux" or platform == "linux2":
      os.system("clear")
    else:
      os.system("cls")


class style():
  def Bright():
    os.system("Color " + str(colorCodes.bright_white))
  def Dim():
    os.system("Color " + str(colorCodes.grey))
  def ResetAll():
    os.system("Color " + str(colorCodes.black + colorCodes.white))
    

def bruteforce(target, print=None):
  staticList = []
  targetList = []
  initTime = time.time()
  for character in target:
    targetList.append(character)
    staticList.append(character)
  for i in range(60, 100):
    random.shuffle(targetList)

  while targetList != staticList:
    random.shuffle(targetList)
    if targetList == target:
      break

  endTime = time.time()
  elapsedtime = endTime - initTime

  if print != None:
    print(''.join(targetList))
    print("Bruteforce took:", elapsedtime, "seconds")
  else:
    return elapsedtime
  

def generate(length, type=None):
  if type == str("binary"):
    returniteam = []
    for i in range(length):
      temp = str(random.randint(0, 1))
      returniteam.append(temp)
      
  if type == str("password"):
    returniteam = []
    dataset = string.ascii_letters + string.digits
    for i in range(length):
      returniteam.append(random.choice(dataset))
      
  if type == str("address"):
    returniteam = []
    dataset = string.ascii_letters + string.digits + string.punctuation
    for i in range(length):
      returniteam.append(random.choice(dataset))
      
  if type == str("number"):
    returniteam = []
    dataset = string.digits + string.digits
    for i in range(length):
      returniteam.append(random.choice(dataset))

  return ''.join(returniteam)