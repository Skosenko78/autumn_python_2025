# todo: База данных пользователя.
# Задан массив объектов пользователя

users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Andrey', 'age': 35, 'group': "master"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

#Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
#,первой букве логина, и заданной группе.

#Сперва вводится тип сортировки:
#1. По возрасту
#2. По первой букве
#3. По группе

#тип сортировки: 1

#Затем сообщение для ввода
#Ввидите критерии поиска: 16

#Результат:
#Пользователь: 'Piter' возраст 23 года , группа  "admin"
#Пользователь: 'Dasha' возраст 30 лет , группа  "master"

condition = 0

def get_login(dictionary):
    return dictionary['login']

def get_age(dictionary):
    return dictionary['age']

def get_group(dictionary):
    return dictionary['group']

print("""
1. По возрасту
2. По первой букве
3. По группе
""")

item = input ("Выберите тип сортировки: ")

match item:
    case '1':
        condition = int(input('Укажите критерии поиска: '))
        users.sort(key=get_age)
    case '2':
        users.sort(key=get_login)
    case '3':
        users.sort(key=get_group)
    case _:
        print('Такого варианта нет.')
        exit(0)

for person in users:
    if condition == 0 or person['age'] > condition:
        print(f"Пользователь: {person['login']} возраст {person['age']} года, группа {person['group']}")