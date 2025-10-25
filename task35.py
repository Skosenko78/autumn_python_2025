# Инкапсуляция и property
# todo: Класс "Температура"
# Создайте класс Temperature, который хранит температуру в градусах Цельсия.
# Добавьте свойство для получения и установки температуры в Фаренгейтах и Кельвинах.
# Внутренне температура должна храниться только в Цельсиях.

# celsius (get, set) - работа с Цельсиями.
# fahrenheit (get, set) - при установке конвертирует значение в Цельсии.
# kelvin (get, set) - при установке конвертирует значение в Цельсии.

# Пример использования
# t = Temperature(25)
# print(f"{t.celsius}C, {t.fahrenheit}F, {t.kelvin}K")
# t.fahrenheit = 32
# print(f"После установки 32F: {t.celsius}C")

class Temperature:

    def __init__(self, celsius):
        self.celsius = float(celsius)

    def __setattr__(self, key, value):
        match key:
            case 'fahrenheit':
                value = (value - 32) / 1.8
            case 'kelvin':
                value -= 273.15
        self.__dict__['celsius'] = value

    def __getattr__(self, item):
        match item:
            case 'fahrenheit':
                return self.celsius*1.8 + 32
            case 'kelvin':
                return self.celsius + 273.15

t = Temperature(25)
print(t.celsius, t.fahrenheit, t.kelvin)
t.fahrenheit = 32
print(f"После установки 32F: {t.celsius}C")
t.kelvin = 373.15
print(f"После установки 373.15K: {t.celsius}C")