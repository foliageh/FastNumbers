with open('main_en.py', 'r', encoding='utf-8') as f:
    s = f.read()

s = s.replace(", 'resourсes'", '').replace('img\\\\', '').replace("'sounds\\\\' + ", '')

with open('main_en_build.py', 'w', encoding='utf-8') as f:
    f.write(s)
