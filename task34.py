# todo: Перепишите игру "Поле чудес" на классах.
import random
import uuid
import datetime
#from os.path import split

from db import DICT_DEFENITION_WORD

class Yakubovich:
    def __init__(self):
        self.name = input('Введите имя: ')
        self.session_uuid = uuid.uuid4()

    def print_menu(self):
        print("""
                    1. Начать игру
                    2. Сохранить игру
                    3. Загрузить игру
                    4. Выход
                """)
        num = int(input('Пункт меню: '))
        match num:
            case 1:
                self.key = self._generate_key()
                self.mask = (['#'] * len(self.key))
                self.start_game()
            case 2:
                self.save_game()
            case 3:
                self.load_game()
            case 4:
                self.end_game()
            case 5:
                pass

    def start_game(self):
        self.list_word = list(self.key)
        print(DICT_DEFENITION_WORD[self.key])
        print(self.mask)
        while '#' in self.mask:
            alfa = input("Введите букву (0 - основное меню): ")
            if alfa == '0':
                self.print_menu()
            count = 0
            for i in self.list_word:
                if alfa == i:
                    self.mask[count] = alfa
                    count += 1
                    continue
                count += 1
            print(self.mask)

    def save_game(self):
        dt = datetime.datetime.now()
        try:
            mask = ''.join(self.mask)
            str = f'{dt}|{self.session_uuid}|{self.name}|{self.key}|{mask}\n'
        except Exception:
            print("Нечего сохранять. Начните новую игру или загрузите предыдущую")
            self.print_menu()
        f = open('save_game.csv', 'at')
        f.write(str)
        f.close()
        print('Сохранил игру!')

    def end_game(self):
        print(f'Спасибо {self.name} за игру! Заходи ещё!')
        exit(0)

    def load_game(self):
        try:
            f = open('save_game.csv', 'rt')
        except (Exception, FileNotFoundError) as error:
            print (f"Нет файла save_game.csv для загрузки")
            self.print_menu()
        indx = 0
        list_str = f.readlines()
        for csv_str in list_str:
            if self.name in csv_str:
                print(indx, ') ', csv_str)
            indx += 1
        indx_load = int(input('Введите номер: '))
        sg = list_str[indx_load].split('|')
        self.key = sg[3]
        self.mask = list(sg[4].strip())
        self.session_uuid = sg[1]
        self.start_game()

    def _generate_key(self) -> str:
        keys = list(DICT_DEFENITION_WORD.keys())
        random.shuffle(keys)
        return keys.pop()


game = Yakubovich()
game.print_menu()