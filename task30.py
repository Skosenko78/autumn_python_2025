# todo: Вы работаете с данными цен товаров, которые приходят в разном формате.
# Создайте список числовых значений цен,  игнорируя некорректные записи.
# Все цены переведите в рубли. Задачу следует решить с использованием списковых включений.

def convert(price):
    result = price
    if 'USD' in price:
        price = f'${price[0:-4]}'
    match price[0]:
        case '€':
            result = f'₽{float(price[1:]) * 93.18:.2f}'
        case '$':
            result = f'₽{float(price[1:]) * 80.80:.2f}'
        case '¥':
            result = f'₽{float(price[1:]) * 0.52:.2f}'
    return result


def valid(item):
    if item.startswith(('₽','€','$','¥')) or 'USD' in item:
        return True
    return False


prices = ["₽1500", "20.50 USD", "invalid", "€25.00", "$15.99",  "18.99", "N/A", "¥5000"]
rub_prices = [convert(item) for item in prices if valid(item)]
print(rub_prices)