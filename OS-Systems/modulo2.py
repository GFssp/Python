# Convertendo os arquivos 'py' presentes no diretorios em arquivos de texto 

import os

current_path = os.getcwd()
for file in os.listdir(current_path):
    name, ext = os.path.splitext(file)
    splitted = name.split("-")
    splitted = [s.strip() for s in splitted]
    if file.endswith('py'):
        new_file = name + ".txt"
        with open(str(new_file), 'w') as file:
            file.write('duplcated file!')
        with open(str(new_file), 'r') as file:
            lines = [line for line in file.readlines()]
    

