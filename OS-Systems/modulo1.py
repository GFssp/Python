import os, inspect
from pathlib import Path

# Nome do sistema operacional (Linux: posix / Microsoft: nt)
print(os.name)

# Caminho atual
print(os.getcwd())

# Caminho da raiz ao usuário
print(Path.home())

# Caminho raiz
print(os.path.abspath(os.sep))

# Caminho que inclui o script 
print(os.path.abspath(inspect.getfile(inspect.currentframe())))

# Camiho apartir do caminho acima
path = os.path.abspath(inspect.getfile(inspect.currentframe()))
current_path = os.path.dirname(path)
print(current_path)

input(' ')