try:
   myfile = open(filename, "r+") # or "a+", whatever you need
except IOError:
    print "Could not open file! Please close Excel!"

def checks():
  