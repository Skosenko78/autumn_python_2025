#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.
# Одинаковых значение может быть два и более !
# Пример:
mass = [1,2,17,54,30,89,2,1,6,2]

# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.

mass_len = len(mass)
passed_items = []

for cnt in range(mass_len - 1):
    result = None
    min_ = mass_len
    if mass[cnt] not in passed_items:
        passed_items.append(mass[cnt])
        next_value = cnt + 1
        pointer = cnt
        while next_value < mass_len:
            if mass[pointer] == mass[next_value]:
                if  next_value - pointer < min_:
                    min_ = next_value - pointer
                    result = f'{pointer} и {next_value}'
                pointer = next_value
            next_value += 1
        if result == None:
            print(f"Для числа {mass[cnt]} нет минимального расстояния т.к элемент в массиве один.")
        else:
            print(f"Для числа {mass[cnt]} минимальное расстояние в массиве по индексам: {result}")