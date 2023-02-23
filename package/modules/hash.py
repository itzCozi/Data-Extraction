# This is a module for hashing in python this will also be implemented in standalone
import random
import time
import string


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

  