import os
from datetime import datetime
from time import sleep

os.chdir('C:/Users/Guilh_000/Documents/Logging_JSON_Basics')

print('METHOD USED TO FIND LOST FILES')
print('-'*40)

for dirpath, dirnames, filenames in os.walk('C:/Users/Guilh_000/Documents/Logging_JSON_Basics'):
    print('Current Path:', dirpath)
    print('Current Diretory:', dirnames)
    print('Files:', filenames)
    print('-'*40)

sleep(60)
