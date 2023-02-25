import sys, os
sys.path.append("c:/users/" + os.getlogin() + "/scoop/apps/python/current/lib/site-packages/dataextract")

import os
import requests


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
  status = requests.get(URL).status_code
  headers = requests.get(URL).headers
  content = requests.get(URL).text
  encoding = requests.get(URL).encoding
  print("Status code: " + str(status))
  print("Headers: " + str(headers))
  print("Content: " + str(content))
  print("Encoding: " + str(encoding))
  
