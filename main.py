import random
import os
import sys
from pygame import mixer
from datetime import datetime
from tkinter import *
root = Tk()

roaming = os.getenv('APPDATA')
path = os.path.dirname(roaming) + '\Local\FastNumbers(beta)'
try:
	os.mkdir(path)
except OSError:
	print('',end='',sep='')
path_inf = path + '\infa.txt'
if os.path.isfile(path_inf):
	print('',end='',sep='')
else:
	with open(path_inf, 'w', encoding='utf-8') as f:
		f.write('player_coins = 300\n')
		f.write('player_record_super_easy = 9:99:99.999999\n')
		f.write('player_record_easy = 9:99:99.999999\n')
		f.write('player_record_medium = 9:99:99.999999\n')
		f.write('player_record_hard = 9:99:99.999999\n')
		f.write('player_record_super_hard = 9:99:99.999999\n')
		f.write('player_tema_num = black\n')
		f.write('player_tema_bg = white\n')
		f.write('player_tema1 = Выбрано\n')
		f.write('player_tema2 = Купить!\n')
		f.write('player_tema3 = Купить!\n')
		f.write('player_tema4 = Купить!\n')
		f.write('player_tema5 = Купить!\n')
		f.write('player_tema6 = Купить!\n')

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


root.title('Быстрые цифры')
root.resizable(width=False, height=False)
num_poradok = 1
param_list = []
with open(path_inf) as f:
    for line in f:
        param_list.append(line.strip().split(' = '))

player_coins = int(param_list[0][1])
player_record_super_easy = param_list[1][1]
player_record_easy = param_list[2][1]
player_record_medium = param_list[3][1]
player_record_hard = param_list[4][1]
player_record_super_hard = param_list[5][1]
player_tema_num = param_list[6][1]
player_tema_bg = param_list[7][1]
player_tema1 = param_list[8][1]
player_tema2 = param_list[9][1]
player_tema3 = param_list[10][1]
player_tema4 = param_list[11][1]
player_tema5 = param_list[12][1]
player_tema6 = param_list[13][1]
icon = PhotoImage(file=resource_path('iconka.gif'))
img1 = PhotoImage(file=resource_path("thema6.gif"))
img2 = PhotoImage(file=resource_path("thema2.gif"))
img3 = PhotoImage(file=resource_path("thema3.gif"))
img4 = PhotoImage(file=resource_path("thema4.gif"))
img5 = PhotoImage(file=resource_path("thema5.gif"))
img6 = PhotoImage(file=resource_path("thema1.gif"))
mixer.init()


def save_param():
    with open(path_inf, 'w') as f:
        f.write('player_coins = '+ str(player_coins) + '\n')
        f.write('player_record_super_easy = '+ player_record_super_easy + '\n')
        f.write('player_record_easy = '+ player_record_easy + '\n')
        f.write('player_record_medium = '+ player_record_medium + '\n')
        f.write('player_record_hard = '+ player_record_hard + '\n')
        f.write('player_record_super_hard = '+ player_record_super_hard + '\n')
        f.write('player_tema_num = '+ player_tema_num + '\n')
        f.write('player_tema_bg = '+ player_tema_bg + '\n')
        f.write('player_tema1 = '+ player_tema1 + '\n')
        f.write('player_tema2 = '+ player_tema2 + '\n')
        f.write('player_tema3 = '+ player_tema3 + '\n')
        f.write('player_tema4 = '+ player_tema4 + '\n')
        f.write('player_tema5 = '+ player_tema5 + '\n')
        f.write('player_tema6 = '+ player_tema6 + '\n')


def MAIN():
    root.title('Быстрые цифры')
    list = root.pack_slaves()
    for i in list:
        i.destroy()
    del list
    list = root.grid_slaves()
    for i in list:
        i.destroy()
    del list
    icon_widjet = Label(image=icon)
    igrat = Button(text='Играть!', font="Arial 20", bg='orange', command=GAME_SETTING)
    magaz = Button(text='Магазин', font="Arial 20", bg='blue', fg='white', command=STORE)
    recordi = Button(text='Рекорды', font="Arial 20", bg='blue', fg='white', command=RECORDS)
    icon_widjet.grid(row=0, column=0, rowspan=6)
    igrat.grid(row=0, column=0, rowspan=6)
    magaz.grid(row=2, column=1)
    recordi.grid(row=3, column=1)


def RECORDS():
    root.title('Рекорды')
    list = root.pack_slaves()
    for i in list:
        i.destroy()
    del list
    list = root.grid_slaves()
    for i in list:
        i.destroy()
    del list
    back = Button(text="Вернуться", font="Arial 12", bg='grey', command=MAIN)
    label = Label(text='Очень легко: '+(player_record_super_easy if player_record_super_easy != '9:99:99.999999' else 'нет') +'\n'+
                       'Легко: '+(player_record_easy if player_record_easy != '9:99:99.999999' else 'нет')+'\n'+
                       'Средне: '+(player_record_medium if player_record_medium != '9:99:99.999999' else 'нет')+'\n'+
                       'Сложно: '+(player_record_hard if player_record_hard != '9:99:99.999999' else 'нет')+'\n'+
                       'Очень сложно: '+(player_record_super_hard if player_record_super_hard != '9:99:99.999999' else 'нет'),
                  font='Arial 16')
    label.pack()
    back.pack()

def STORE():
    root.title('Магазин')
    global player_coins
    global player_tema1
    global player_tema2
    global player_tema3
    global player_tema4
    global player_tema5
    global player_tema6
    global player_tema_num
    global player_tema_bg
    list = root.pack_slaves()
    for i in list:
        i.destroy()
    del list
    list = root.grid_slaves()
    for i in list:
        i.destroy()
    del list
    def buy1():
        global player_coins
        global player_tema1
        global player_tema2
        global player_tema3
        global player_tema4
        global player_tema5
        global player_tema6
        global player_tema_num
        global player_tema_bg
        if tema1_buy['text'] == 'Куплено':
            tema1_buy['text'] = 'Выбрано'
            tema1_buy['bg'] = 'yellow'
            player_tema1 = 'Выбрано'
            player_tema_num = 'black'
            player_tema_bg = 'white'
            if tema2_buy['text'] == 'Выбрано':
                tema2_buy['text'] = 'Куплено'
                tema2_buy['bg'] = 'grey'
                player_tema2 = 'Куплено'
            if tema3_buy['text'] == 'Выбрано':
                tema3_buy['text'] = 'Куплено'
                tema3_buy['bg'] = 'grey'
                player_tema3 = 'Куплено'
            if tema4_buy['text'] == 'Выбрано':
                tema4_buy['text'] = 'Куплено'
                tema4_buy['bg'] = 'grey'
                player_tema4 = 'Куплено'
            if tema5_buy['text'] == 'Выбрано':
                tema5_buy['text'] = 'Куплено'
                tema5_buy['bg'] = 'grey'
                player_tema5 = 'Куплено'
            if tema6_buy['text'] == 'Выбрано':
                tema6_buy['text'] = 'Куплено'
                tema6_buy['bg'] = 'grey'
                player_tema6 = 'Куплено'
        save_param()

    def buy2():
        global player_coins
        global player_tema1
        global player_tema2
        global player_tema3
        global player_tema4
        global player_tema5
        global player_tema6
        global player_tema_num
        global player_tema_bg
        if (tema2_buy['text'] == 'Купить!' and player_coins >= 500) or tema2_buy['text'] == 'Куплено':
            if tema2_buy['text'] == 'Купить!':
                player_coins -= 500
            tema2_buy['text'] = 'Выбрано'
            tema2_buy['bg'] = 'yellow'
            player_tema2 = 'Выбрано'
            player_tema_num = 'white'
            player_tema_bg = 'blue'
            if tema1_buy['text'] == 'Выбрано':
                tema1_buy['text'] = 'Куплено'
                tema1_buy['bg'] = 'grey'
                player_tema1 = 'Куплено'
            if tema3_buy['text'] == 'Выбрано':
                tema3_buy['text'] = 'Куплено'
                tema3_buy['bg'] = 'grey'
                player_tema3 = 'Куплено'
            if tema4_buy['text'] == 'Выбрано':
                tema4_buy['text'] = 'Куплено'
                tema4_buy['bg'] = 'grey'
                player_tema4 = 'Куплено'
            if tema5_buy['text'] == 'Выбрано':
                tema5_buy['text'] = 'Куплено'
                tema5_buy['bg'] = 'grey'
                player_tema5 = 'Куплено'
            if tema6_buy['text'] == 'Выбрано':
                tema6_buy['text'] = 'Куплено'
                tema6_buy['bg'] = 'grey'
                player_tema6 = 'Куплено'
        balance['text'] = "Ваш баланс: "+str(player_coins)
        save_param()
    def buy3():
        global player_tema1
        global player_tema2
        global player_tema3
        global player_tema4
        global player_tema5
        global player_tema6
        global player_coins
        global player_tema_num
        global player_tema_bg
        if (tema3_buy['text'] == 'Купить!' and player_coins >= 500) or tema3_buy['text'] == 'Куплено':
            if tema3_buy['text'] == 'Купить!':
                player_coins -= 500
            tema3_buy['text'] = 'Выбрано'
            tema3_buy['bg'] = 'yellow'
            player_tema3 = 'Выбрано'
            player_tema_num = 'yellow'
            player_tema_bg = 'purple'
            if tema1_buy['text'] == 'Выбрано':
                tema1_buy['text'] = 'Куплено'
                tema1_buy['bg'] = 'grey'
                player_tema1 = 'Куплено'
            if tema2_buy['text'] == 'Выбрано':
                tema2_buy['text'] = 'Куплено'
                tema2_buy['bg'] = 'grey'
                player_tema2 = 'Куплено'
            if tema4_buy['text'] == 'Выбрано':
                tema4_buy['text'] = 'Куплено'
                tema4_buy['bg'] = 'grey'
                player_tema4 = 'Куплено'
            if tema5_buy['text'] == 'Выбрано':
                tema5_buy['text'] = 'Куплено'
                tema5_buy['bg'] = 'grey'
                player_tema5 = 'Куплено'
            if tema6_buy['text'] == 'Выбрано':
                tema6_buy['text'] = 'Куплено'
                tema6_buy['bg'] = 'grey'
                player_tema6 = 'Куплено'
        balance['text'] = "Ваш баланс: "+str(player_coins)
        save_param()
    def buy4():
        global player_coins
        global player_tema1
        global player_tema2
        global player_tema3
        global player_tema4
        global player_tema5
        global player_tema6
        global player_tema_num
        global player_tema_bg
        if (tema4_buy['text'] == 'Купить!' and player_coins >= 500) or tema4_buy['text'] == 'Куплено':
            if tema4_buy['text'] == 'Купить!':
                player_coins -= 500
            tema4_buy['text'] = 'Выбрано'
            tema4_buy['bg'] = 'yellow'
            player_tema4 = 'Выбрано'
            player_tema_num = 'yellow'
            player_tema_bg = 'green'
            if tema1_buy['text'] == 'Выбрано':
                tema1_buy['text'] = 'Куплено'
                tema1_buy['bg'] = 'grey'
                player_tema1 = 'Куплено'
            if tema3_buy['text'] == 'Выбрано':
                tema3_buy['text'] = 'Куплено'
                tema3_buy['bg'] = 'grey'
                player_tema3 = 'Куплено'
            if tema2_buy['text'] == 'Выбрано':
                tema2_buy['text'] = 'Куплено'
                tema2_buy['bg'] = 'grey'
                player_tema2 = 'Куплено'
            if tema5_buy['text'] == 'Выбрано':
                tema5_buy['text'] = 'Куплено'
                tema5_buy['bg'] = 'grey'
                player_tema5 = 'Куплено'
            if tema6_buy['text'] == 'Выбрано':
                tema6_buy['text'] = 'Куплено'
                tema6_buy['bg'] = 'grey'
                player_tema6 = 'Куплено'
        balance['text'] = "Ваш баланс: "+str(player_coins)
        save_param()
    def buy5():
        global player_coins
        global player_tema1
        global player_tema2
        global player_tema3
        global player_tema4
        global player_tema5
        global player_tema6
        global player_tema_num
        global player_tema_bg
        if (tema5_buy['text'] == 'Купить!' and player_coins >= 500) or tema5_buy['text'] == 'Куплено':
            if tema5_buy['text'] == 'Купить!':
                player_coins -= 500
            tema5_buy['text'] = 'Выбрано'
            tema5_buy['bg'] = 'yellow'
            player_tema5 = 'Выбрано'
            player_tema_num = 'green'
            player_tema_bg = 'beige'
            if tema1_buy['text'] == 'Выбрано':
                tema1_buy['text'] = 'Куплено'
                tema1_buy['bg'] = 'grey'
                player_tema1 = 'Куплено'
            if tema3_buy['text'] == 'Выбрано':
                tema3_buy['text'] = 'Куплено'
                tema3_buy['bg'] = 'grey'
                player_tema3 = 'Куплено'
            if tema4_buy['text'] == 'Выбрано':
                tema4_buy['text'] = 'Куплено'
                tema4_buy['bg'] = 'grey'
                player_tema4 = 'Куплено'
            if tema2_buy['text'] == 'Выбрано':
                tema2_buy['text'] = 'Куплено'
                tema2_buy['bg'] = 'grey'
                player_tema2 = 'Куплено'
            if tema6_buy['text'] == 'Выбрано':
                tema6_buy['text'] = 'Куплено'
                tema6_buy['bg'] = 'grey'
                player_tema6 = 'Куплено'
        balance['text'] = "Ваш баланс: "+str(player_coins)
        save_param()
    def buy6():
        global player_coins
        global player_tema1
        global player_tema2
        global player_tema3
        global player_tema4
        global player_tema5
        global player_tema6
        global player_tema_num
        global player_tema_bg
        if (tema6_buy['text'] == 'Купить!' and player_coins >= 500) or tema6_buy['text'] == 'Куплено':
            if tema6_buy['text'] == 'Купить!':
                player_coins -= 500
            tema6_buy['text'] = 'Выбрано'
            tema6_buy['bg'] = 'yellow'
            player_tema6 = 'Выбрано'
            player_tema_num = 'yellow'
            player_tema_bg = 'black'
            if tema1_buy['text'] == 'Выбрано':
                tema1_buy['text'] = 'Куплено'
                tema1_buy['bg'] = 'grey'
                player_tema1 = 'Куплено'
            if tema3_buy['text'] == 'Выбрано':
                tema3_buy['text'] = 'Куплено'
                tema3_buy['bg'] = 'grey'
                player_tema3 = 'Куплено'
            if tema4_buy['text'] == 'Выбрано':
                tema4_buy['text'] = 'Куплено'
                tema4_buy['bg'] = 'grey'
                player_tema4 = 'Куплено'
            if tema5_buy['text'] == 'Выбрано':
                tema5_buy['text'] = 'Куплено'
                tema5_buy['bg'] = 'grey'
                player_tema5 = 'Куплено'
            if tema2_buy['text'] == 'Выбрано':
                tema2_buy['text'] = 'Куплено'
                tema2_buy['bg'] = 'grey'
                player_tema2 = 'Куплено'
        balance['text'] = "Ваш баланс: "+str(player_coins)
        save_param()

    title = Label(text="МАГАЗИН", justify=CENTER, font="Arial 20", fg="yellow", bg='blue')
    balance = Label(text="Ваш баланс: "+str(player_coins), font="Arial 12", bg='grey')
    back = Button(text="Вернуться", font="Arial 12", bg='grey', command=MAIN)
    frame1 = Frame(root, bg='grey', bd=5)
    frame2 = Frame(root, bg='black', bd=5)
    frame3 = Frame(root, bg='black', bd=5)
    label = Label(frame1, text="\n\n\n\n\n\n\n\n\n\n\n\n", bg='grey')
    label1 = Label(frame1, text="\n\n\n\n", bg='grey')
    temi = Button(frame1, text='    Темы    ', font="Arial 20")
    usilenia = Button(frame1, text=' Усиления \n(в разработке)', font="Arial 20")
    tema1 = Label(frame2, text="1. Тема №1\nСтоимость: 500 голды", bg='black', fg='orange', justify=LEFT, font="Arial 12")
    tema1_buy = Button(frame2, text=player_tema1, bg=('yellow' if player_tema1 == 'Выбрано' else('grey' if player_tema1 == 'Куплено' else 'white')), command=buy1)
    tema2 = Label(frame2, text="\n2. Тема №2\nСтоимость: 500 голды", bg='black', fg='orange', justify=LEFT, font="Arial 12")
    tema2_buy = Button(frame2, text=player_tema2, command=buy2, bg=('yellow' if player_tema2 == 'Выбрано' else('grey' if player_tema2 == 'Куплено' else 'white')))
    tema3 = Label(frame2, text="\n3. Тема №3\nСтоимость: 500 голды", bg='black', fg='orange', justify=LEFT, font="Arial 12")
    tema3_buy = Button(frame2, text=player_tema3, command=buy3, bg=('yellow' if player_tema3 == 'Выбрано' else('grey' if player_tema3 == 'Куплено' else 'white')))
    tema4 = Label(frame3, text="4. Тема №4\nСтоимость: 500 голды", bg='black', fg='orange', justify=LEFT, font="Arial 12")
    tema4_buy = Button(frame3, text=player_tema4, command=buy4, bg=('yellow' if player_tema4 == 'Выбрано' else('grey' if player_tema4 == 'Куплено' else 'white')))
    tema5 = Label(frame3, text="\n5. Тема №5\nСтоимость: 500 голды", bg='black', fg='orange', justify=LEFT, font="Arial 12")
    tema5_buy = Button(frame3, text=player_tema5, command=buy5, bg=('yellow' if player_tema5 == 'Выбрано' else('grey' if player_tema5 == 'Куплено' else 'white')))
    tema6 = Label(frame3, text="\n6. Тема №6\nСтоимость: 500 голды", bg='black', fg='orange', justify=LEFT,font="Arial 12")
    tema6_buy = Button(frame3, text=player_tema6, command=buy6, bg=('yellow' if player_tema6 == 'Выбрано' else('grey' if player_tema6 == 'Куплено' else 'white')))
    panel1 = Label(frame2, image=img1)
    panel2 = Label(frame2, image=img2)
    panel3 = Label(frame2, image=img3)
    panel4 = Label(frame3, image=img4)
    panel5 = Label(frame3, image=img5)
    panel6 = Label(frame3, image=img6)
    back.grid(row=0, column=2)
    balance.grid(row=0, column=0)
    title.grid(row=1, column=0, columnspan=3)
    frame1.grid(row=2, column=0, rowspan=30, sticky='ns')
    frame2.grid(row=2, column=1)
    frame3.grid(row=2, column=2)
    label.pack()
    temi.pack()
    label1.pack()
    usilenia.pack()

    tema1.pack()
    panel1.pack()
    tema1_buy.pack()

    tema2.pack()
    panel2.pack()
    tema2_buy.pack()

    tema3.pack()
    panel3.pack()
    tema3_buy.pack()

    tema4.pack()
    panel4.pack()
    tema4_buy.pack()

    tema5.pack()
    panel5.pack()
    tema5_buy.pack()

    tema6.pack()
    panel6.pack()
    tema6_buy.pack()


def GAME_SETTING():
    root.title('Настройки игрового режима')
    mixer.music.load(resource_path('click.mp3'))
    mixer.music.play()
    list = root.pack_slaves()
    for i in list:
        i.destroy()
    del list
    list = root.grid_slaves()
    for i in list:
        i.destroy()
    del list
    def p1_command():
        global num_poradok
        p1['bg'] = 'yellow'
        p2['bg'] = 'white'
        num_poradok = 1
        lvl1['state'] = NORMAL
        lvl2['state'] = NORMAL
        lvl3['state'] = NORMAL
        lvl4['state'] = NORMAL
        lvl5['state'] = NORMAL
    def p2_command():
        global num_poradok
        p2['bg'] = 'yellow'
        p1['bg'] = 'white'
        num_poradok = 2
        lvl1['state'] = NORMAL
        lvl2['state'] = NORMAL
        lvl3['state'] = NORMAL
        lvl4['state'] = NORMAL
        lvl5['state'] = NORMAL
    def game1():
        GAME('очень легко')
    def game2():
        GAME('легко')
    def game3():
        GAME('средне')
    def game4():
        GAME('сложно')
    def game5():
        GAME('очень сложно')
    vibor_poradka = Label(text="Выбирите порядок чисел: ", font="Arial 20")
    p1 = Button(text='Обычный', font="Arial 16", command=p1_command)
    p2 = Button(text='Обратный', font="Arial 16", command=p2_command)
    vibor = Label(text="Выбирите режим игры: ", font="Arial 20")
    lvl1 = Button(text='Очень легко', font="Arial 16", state=DISABLED, command=game1)
    lvl2 = Button(text='    Легко    ', font="Arial 16", state=DISABLED, command=game2)
    lvl3 = Button(text='  Средне   ', font="Arial 16", state=DISABLED, command=game3)
    lvl4 = Button(text='  Сложно   ', font="Arial 16", state=DISABLED, command=game4)
    lvl5 = Button(text='Очень сложно', font="Arial 16", state=DISABLED, command=game5)
    vibor_poradka.grid(row=0, column=0, columnspan=5)
    p1.grid(row=1, column=0)
    p2.grid(row=1, column=1)
    vibor.grid(row=2, column=0, columnspan=5)
    lvl1.grid(row=3, column=0)
    lvl2.grid(row=3, column=1)
    lvl3.grid(row=3, column=2)
    lvl4.grid(row=3, column=3)
    lvl5.grid(row=3, column=4)


def GAME(record_type):
    root.title('Игра - '+record_type)
    global num_poradok
    list1 = root.pack_slaves()
    for i in list1:
        i.destroy()
    del list1
    list1 = root.grid_slaves()
    for i in list1:
        i.destroy()
    del list1
    plus_coins = 0
    if record_type == 'очень легко':
        player_record = player_record_super_easy
        matrix_size = 5
    elif record_type == 'легко':
        player_record = player_record_easy
        matrix_size = 7
    elif record_type == 'средне':
        player_record = player_record_medium
        matrix_size = 10
    elif record_type == 'сложно':
        player_record = player_record_hard
        matrix_size = 12
    else:
        player_record = player_record_super_hard
        matrix_size = 15
    cell_size = 40
    canvas_size = cell_size*matrix_size
    matrix = []
    numbers = []
    num_now = 1 if num_poradok == 1 else matrix_size*matrix_size
    errors = 0
    score = '9:99:99.999999'

    def GAME0():
        nonlocal player_record
        global player_record_super_easy
        global player_record_easy
        global player_record_medium
        global player_record_hard
        global player_record_super_hard
        if record_type == 'очень легко':
            player_record_super_easy = player_record
        elif record_type == 'легко':
            player_record_easy = player_record
        elif record_type == 'средне':
            player_record_medium = player_record
        elif record_type == 'сложно':
            player_record_hard = player_record
        else:
            player_record_super_hard = player_record
        list = root.pack_slaves()
        for i in list:
            i.destroy()
        del list
        GAME(record_type)

    def MAIN00():
        nonlocal num_now
        nonlocal matrix_size
        if (num_now != matrix_size**2) if num_poradok == 1 else (num_now != 1):
            MAIN()
        else:
            MAIN0()
    def MAIN0():
        list = root.pack_slaves()
        for i in list:
            i.destroy()
        del list
        MAIN()

    out_widget = Button(text="Выход", bg='grey', font='Arial 24', command=MAIN00)
    out_widget.pack()
    num_now_widget = Label(text=str(num_now), font=("Arial", 20))
    num_now_widget.pack()
    c = Canvas(root, width=canvas_size+1, height=canvas_size+1, bg=player_tema_bg)
    c.pack()
    results_widget = Label(text='', font=("Arial", 20))
    play_again_widget = Button(text="Играть снова", bg='red', font='Arial 24', command=GAME0)


    def create_matrix():
        nonlocal numbers
        numbers = list(range(1, (matrix_size**2)+1))
        random.shuffle(numbers)

        kjj = 0
        for i in range(matrix_size):
            matrix.append([])
            for j in range(matrix_size):
                matrix[i].append(numbers[kjj])
                kjj += 1

        kjj = 0
        for i in range(matrix_size):
            for j in range(matrix_size):
                x1 = i*cell_size+2
                x2 = j*cell_size+2
                y1 = x1+cell_size
                y2 = x2+cell_size
                c.create_rectangle(x1, x2, y1, y2)
                c.create_text(x1+cell_size/2, x2+cell_size/2,
                              text=str(matrix[i][j]),
                              fill=player_tema_num,
                              font=('Arial', 16))
                kjj += 1
        del kjj


    def click(event):
        nonlocal num_now
        nonlocal errors
        nonlocal score
        nonlocal matrix
        nonlocal numbers
        nonlocal player_record
        nonlocal plus_coins
        global num_poradok
        global player_coins
        global player_record_super_easy
        global player_record_easy
        global player_record_medium
        global player_record_hard
        global player_record_super_hard
        x = event.x
        y = event.y
        i = x // cell_size
        j = y // cell_size
        mixer.music.load(resource_path('click.mp3'))
        mixer.music.play()
        if matrix[i][j] == num_now:
            if num_poradok == 1:
                num_now += 1
            else:
                num_now -= 1
            plus_coins += 2
            if (matrix[i][j] == matrix_size**2) if num_poradok == 1 else (matrix[i][j] == 1):
                game_time = datetime.now() - start
                list = root.pack_slaves()
                for i in list:
                    i.destroy()
                del list
                root.title('Результаты')
                score = str(game_time)
                if score < player_record:
                    player_record = score
                mixer.music.load(resource_path('win.mp3'))
                mixer.music.play()
                player_coins += plus_coins
                results_widget['text'] = 'Победа!' + '\n' + \
                                         'Ошибки: ' + str(errors) + '\n' + \
                                         'Итоговое время: ' + score + '\n' + \
                                         "Рекордное время (" + record_type + "): " + player_record + '\n' + \
                                         '+' + str(plus_coins) + " монет" + '\n'
                results_widget.pack()
                play_again_widget.pack()
                out_widget = Button(text="Выход", bg='grey', font='Arial 24', command=MAIN0)
                out_widget.pack()
                if record_type == 'очень легко':
                    player_record_super_easy = player_record
                elif record_type == 'легко':
                    player_record_easy = player_record
                elif record_type == 'средне':
                    player_record_medium = player_record
                elif record_type == 'сложно':
                    player_record_hard = player_record
                else:
                    player_record_super_hard = player_record
                save_param()
            else:
                num_now_widget['text'] = str(num_now)
        elif (matrix[i][j] < num_now) if num_poradok == 1 else (matrix[i][j] > num_now):
            print('')
        else:
            mixer.music.load(resource_path('err.wav'))
            mixer.music.play()
            errors += 1
            plus_coins -= 2
            if errors >= len(numbers):
                root.title('Результаты')
                list = root.pack_slaves()
                for i in list:
                    i.destroy()
                del list
                results_widget['text'] = "Проигрыш :("
                results_widget.pack()
                play_again_widget.pack()
                out_widget = Button(text="Выход", bg='grey', font='Arial 24', command=MAIN0)
                out_widget.pack()

    create_matrix()
    start = datetime.now()
    c.bind('<1>', click)


MAIN()
root.mainloop()
