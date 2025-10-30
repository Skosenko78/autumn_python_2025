# Композиция и вычисляемые свойства
# todo: Класс "Заказ"
# Создайте класс Order (Заказ). Внутри он хранит список экземпляров Product (из предыдущей задачи 37).
# Реализуйте свойство total_price, которое вычисляет общую стоимость заказа на основе цен всех товаров
# в списке. Реализуйте методы add_product(product) и remove_product(product) для управления списком.

# Пример использования
#book = Product("Book", 10)
#pen = Product("Pen", 2)
#order = Order()
#order.add_product(book)
#order.add_product(pen)
#print(f"Общая стоимость: {order.total_price}")  # 12

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __setattr__(self, key, value):
        if key == 'price' and value < 0:
            value = 0
        self.__dict__[key] = value

class Order:

    def __init__(self):
        self.busket = []

    def add_product(self, item):
        self.busket.append(item)

    def remove_product(self, item):
        if item in self.busket:
            self.busket.remove(item)

    def __getattr__(self, attr):
        if attr == 'total_price':
            total = sum(i.price for i in self.busket)
            return total
        else:
            raise Exception(f"Unknown attribute {attr}")


book = Product("Book", 10)
pen = Product("Pen", 2)
order = Order()
order.add_product(book)
order.add_product(pen)
print(f"Общая стоимость: {order.total_price}")  # 12