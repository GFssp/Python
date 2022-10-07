# Enviando os arquivos de texto gerados para a pasta 'automatic-folder'

from pathlib import Path
import os
import shutil
from time import sleep

Path("automatic-folder").mkdir(exist_ok=True)
new_path = os.getcwd() + "automatic-folder"

for file in os.listdir():
    name, ext = os.path.splitext(file)
    if file.endswith('txt'):
        shutil.copy(file, "automatic-folder")
        os.remove(file)
       
               