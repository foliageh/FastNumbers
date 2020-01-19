import subprocess
import os
import shutil

lang = 'en'

with open(f'main_{lang}.py', 'r', encoding='utf-8') as f:
    s = f.read()

s = s.replace(", 'resourсes'", '').replace('img\\\\', '').replace("'sounds\\\\' + ", '')

with open(f'main_{lang}_build.py', 'w', encoding='utf-8') as f:
    f.write(s)

with open(f'main.spec', 'a', encoding='utf-8') as f:
    f.write(f.read().replace('main_en_build', f'main_{lang}_build.py').replace('main_ru_build', f'main_{lang}_build.py'))

os.chdir('C:\\Users\\exe-builder')
subprocess.call('pyinstaller FastNumbers\\main.spec --icon FastNumbers\\resourсes\\icon.ico --upx-dir=C:\\Users\\exe-builder', shell=True)

