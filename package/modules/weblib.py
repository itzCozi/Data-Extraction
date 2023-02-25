import sys, os
sys.path.append("c:/users/" + os.getlogin() + "/scoop/apps/python/current/lib/site-packages/dataextract")

try:
  import os
  from coolor import text, background, style
  import requests
except ImportError:
  print("Error: Missing module(s) please install the following module(s): colorama, datetime and os.")
  

# Global variables
class errorMessages():
  error = str("ERROR: An unknown error has occured.")
  fileUnreadable = str("ERROR: The file given cannot be read.")
  fileEmpty = str("ERROR: The given file is empty and contains no data.")
  fileExists = str("ERROR: The file does not exist/the path can't be found.")


# Functions
def webinstall(URL, Destination, NewName, FileExt):
  file_content = requests.get(URL)
  with open(Destination + '/' + NewName + FileExt, "wb") as file:
    file.write(file_content.content)
    file.close()
    

def analysepage(URL):
  page = requests.get(URL)
  status = page.status_code
  headers = page.headers
  content = page.text
  encoding = page.encoding
  
  text.Blue()
  print("Status code: " + str(status))
  text.Purple()
  print("Headers: " + str(headers))
  text.Green()
  print("Content: " + str(content))
  text.Red()
  print("Encoding: " + str(encoding))
  style.ResetAll()
  
  
analysepage("https://itzcozi.github.io/SafeGuard/") 