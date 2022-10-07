# Zipando a pasta automatic-folder

import zipfile

file_zipped = zipfile.ZipFile('automatic-folder', 'w')
file_zipped.write('automatic-folder', compress_type=zipfile.ZIP_DEFLATED)
file_zipped.close()