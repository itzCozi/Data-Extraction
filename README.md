# File Data Extraction - Python Package
The data extraction package was made for the soul purpose of me being bored. I also recently learned how to extract list and other data from a file, and while looking up how to do it I found nothing no one has ever asked and theres no packages, so I made one. Ladies and Gentlemen, I present to you the data extraction package. It comes equipped with a CC function to clear the console screen of any user. An extract list function this will make a list out of a file, every line is a itanam in the list. An extractable function, this does the same as the extractlist, but it joins each line to create a string and then adds that to the list. A filter file function which will search a file for the given word and if found, remove the word. A random hex function that returns a hex digest in the form of a string, this digest is always less than 20 characters.

**Features**

- Clear console
- Filter file
- Extract list
- Extract table
- Random hex


Extracting a list from a file with the data extraction package.
```
from data_extraction import extractList

print(extractList("data/test.txt"))
```
``
["Connor  Camden  982137882  21341", "Madine  Opeark  9031312354  21908"]
``


## Examples
The following are examples of a couple of ways to use the package.

**Example 1**
```
import time
from data_extract import CC, randomhex

print(randomhex())
time.sleep(2)
CC()
```
This code will result in a random hex being printed to the console and then the console will be cleared.

**Example 2**
```
from data_extract import extractlist

print(extractlist("test.txt"))
```
This code will result in the file given to be split into a list and then printed to the console.

### Quickstart & Standalone

**Get Started** With the inclusive [Quickstart Guide](https://github.com/itzCozi/Data-Extraction/wiki/Quickstart-Guide)  

Quick start ways.

``
from standalone import createDigest

print(createDigest())
``

``
from standalone import extractList

PATH = "data/"

for iteam in path:
  with open(iteam, "r") as file:
    print(extractList(file))
``

Notice the standalone file is not in a folder like the modules from the package instead it floats freely around the lib directory this alows for easy access to the functions.


## Development
The package is still in development, and will be for not to much longer. I will be adding more features and fixing bugs as I find them. If you have any suggestions or find any bugs, please let me know by creating an issue or by contacting me..Also feel free to reach out about contributing to the project.

### Source Code
The source code is public as this is a open source project the code can be found [here](https://github.com/itzCozi/Data-Extraction/blob/main/package/standalone/dataextraction.py). I am open to pull requests and suggestions in the form of issues with the "suggestions" label, Other versions of the code as in every function can be found in the [modules](https://github.com/itzCozi/Data-Extraction/tree/main/package/modules) folder in its respected file. 

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/itzCozi/Data-Extraction/blob/main/ignore/LICENSE) file for details.


## Extra

[Package on PyPi](https://pypi.org/project/Data-Extract/)  
[Latest Release](https://github.com/itzCozi/Data-Extraction/releases)  
[Quickstart Guide](https://github.com/itzCozi/Data-Extraction/wiki/Quickstart-Guide)  

Contact Me
---------------------------------
discord: BadDevoleper#4200                                                                                                                                             
Email: Cooperransom08@outlook.com                                                                                                                                      
[Replit](https://replit.com/@cozi08) | 
[Twitter](https://twitter.com/ransom_cooper)