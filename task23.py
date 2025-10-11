# todo: Исправить ошибку в коде игры  ../code/ya_kube.py
# Ошибку исправил: перенёс строку 'list_word = list(key)' в функцию start_game
#from lesson_5.code import ya_kube

import random
import uuid
import datetime
from db import DICT_DEFENITION_WORD

name = input("Введите имя:")

def print_menu():
    print("""   
       1. Начать игру
       2. Сохранить игру
       3. Загрузить игру
       4. Выход из игры
       5. Настройки 
    """)

print_menu()
num = int(input("Пункт меню:"))


def generate_key() -> str:
    keys = list(DICT_DEFENITION_WORD.keys())
    random.shuffle(keys)
    return keys.pop()


def save_game(id_session, word, mask):
    # dt, id_session, name, word, mask
    f = open("save_game.csv", "at")
    dt = datetime.datetime.now()
    mask = "".join(mask)
    str = f"{dt}|{id_session}|{name}|{word}|{mask}"
    f.write(str)
    f.close()
    print("Сохранил игру!")


def load_game():
    f = open("save_game.csv", "tr")
    indx = 0
    list_str= f.readlines()
    for csv_str in list_str:
       if name in csv_str:
         print(indx, ") ", csv_str)
       indx += 1
    indx_load = int(input("Введите номер:"))
    sg = list_str[indx_load].split("|")
    key = sg[3]
    mask = sg[4]
    session_uuid = sg[1]
    # print(session_uuid,key, list(mask))
    start_game(session_uuid,key.strip(), list(mask))


def start_game(session_uuid, key, mask ):
    list_word = list(key)
    print(DICT_DEFENITION_WORD[key])
    print(mask)
    while '#' in mask:
        alfa = input("Введите букву:")
        if alfa == "2":
            print("Сохранение игры!")
            save_game(session_uuid, key, mask)
        cnt = 0
        for i in list_word:
            if alfa == i:
                mask[cnt] = alfa
                cnt += 1
                continue
            cnt += 1
        else:
            print(mask)

match num:
    case 1:
        key = generate_key()
        mask = ['#'] * len(key)
        session_uuid = uuid.uuid4()
        start_game(session_uuid,key,mask)
        # print('The UUID is: ' + str(session_uuid))
    case 2:
        pass
    case 3:
        load_game()
    case 4:
        print(f"Спасибо {name} за игру! Заходи еще! ")
        pass



