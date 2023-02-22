# https://www.freecodecamp.org/news/build-your-first-python-package/
from setuptools import setup, find_packages

VERSION = '0.1' 
DESCRIPTION = 'Extract data from files in python'
LONG_DESCRIPTION = 'A python package for extracting data from files'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="Data Extract", 
        version=VERSION,
        author="Cooper ransom",
        author_email="Cooperransom08@outlook.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'data', 'extraction', 'list'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Coders",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: Windows :: Linux",
            "Operating System :: Linux :: Windows",
        ]
)
