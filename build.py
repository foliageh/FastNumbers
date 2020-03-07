import subprocess
import sys, os
import shutil
os.chdir('C:\\Users\\Александр\\PycharmProjects\\FastNumbers')
# Open cmd from admin and write - python C:\Users\Александр\PycharmProjects\FastNumbers\build.py

lang = 'en'

with open(f'main_{lang}.py', 'r', encoding='utf-8') as f:
    s = f.read()

s = s.replace(", 'resourсes'", '').replace('img\\\\', '').replace("'sounds\\\\' + ", '')

with open(f'main_{lang}_build.py', 'w', encoding='utf-8') as f:
    f.write(s)

with open('main.spec', 'r', encoding='utf-8') as f:
    s = f.read()
with open('main.spec', 'w', encoding='utf-8') as f:
    f.write(s.replace('main_en_build', f'main_{lang}_build').replace('main_ru_build', f'main_{lang}_build'))


os.chdir('C:\\Users\\exe-builder')
subprocess.call('pyinstaller FastNumbers\\main.spec --upx-dir=C:\\Users\\exe-builder', shell=True)
shutil.move('C:\\Users\\Exe-Builder\\dist\\FastNumbers.exe',
            'C:\\Users\\Александр\\PycharmProjects\\FastNumbers\\results\\FastNumbers.exe')

# --icon FastNumbers\\resourсes\\icon.ico
