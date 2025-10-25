# Инкапсуляция и property
# todo: Класс "Товар" (Защита от отрицательной цены)
# Создайте класс Product. У него есть свойства name (простая строка) и price.
# При установке цены проверяйте, что она не отрицательная.
# Если пытаются установить отрицательную цену, устанавливайте 0.


# Пример использования
# product = Product("Book", 10)
# print(product.price)  # 10
# product.price = -5
# print(product.price)  # 0

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __setattr__(self, key, value):
        if key == 'price' and value < 0:
            value = 0
        self.__dict__[key] = value

product = Product("Book", 10)
print(product.price)
product.price = -15
print(product.price)