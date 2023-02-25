import sys, os
sys.path.append("C:/Users/" + os.getlogin() + "/scoop/apps/python/current/Lib/site-packages/dataextract")

from .randomhex import createDigest
from .filterfile import filterFile
from .extractlist import extractList
from .weblib import webinstall, analysepage
from .extracttable import extractTable
from .clearconsole import CC
from .coolor import text, background, style
from .extra import bruteforce, generate
from .randnum import randnum
from .hash import keypair, hashfile, comparehash, secure
from .Ptime import nowtime, currentdate, currenttime
from .easylog import eventlog, errorlog
from .tick import tick