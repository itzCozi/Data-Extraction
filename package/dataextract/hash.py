# This is a module for hashing in python this will also be implemented in standalone
try:
  import random
  import time
  import hashlib
  import string
  import os
except ImportError:
  print("Error: Missing module(s) please install the following module(s): random, time, hashlib, string")


# Global variables
class errorMessages():
  error = str("ERROR: An unknown error has occured.")
  fileUnreadable = str("ERROR: The file given cannot be read.")
  fileEmpty = str("ERROR: The given file is empty and contains no data.")
  insufficientPerm = str("ERROR: The file cannot be accessed due to insufficient permissions.")
  fileExists = str("ERROR: The file does not exist/the path can't be found.")
  fileOpen = str("ERROR: The file cannot be opened due to it being in use by another process.")   
  

def keypair(print=None):
  threshold = random.randint(2, 8)
  buff = random.randint(200, 1000)
  length = random.randint(50, 400)
  tiny = random.uniform(0.01, 0.99)
  x = 0
  alphabet = string.ascii_letters + string.digits
  publicBase = '.'.join(random.choice(alphabet) for i in range(buff))
  privateBase = '.'.join(random.choice(alphabet) for i in range(buff))

  time.sleep(tiny)

  publicList = publicBase.split('.')
  privateList = privateBase.split('.')

  while x != threshold:
    x = privateList + publicList
    y = publicList + privateList
    for iteam in x, y:
      random.shuffle(x)
      random.shuffle(y)
    x =+ 1

  time.sleep(tiny)
  
  publicKey = ''.join(random.choice(x) for i in range(length))
  privateKey = ''.join(random.choice(y) for i in range(length))

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
    foo = randomkey + newList
    for i in foo:
      random.shuffle(foo)

  returnKey = ''.join(random.choice(foo) for i in range(keyLength))

  return returnKey