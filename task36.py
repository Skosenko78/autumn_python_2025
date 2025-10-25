# Инкапсуляция и property
# todo: Класс "Пользователь" (Валидация email)
# Создайте класс User. У него должны быть свойства email и password.
# При установке email проверяйте, что строка содержит символ @ (простая валидация).
# При установке пароля, храните не сам пароль, а его хеш (для простоты можно использовать hash()).
# Сделайте метод check_password(password), который проверяет, соответствует ли хеш переданного
# пароля сохраненному хешу.

# Пример использования
# user = User("test@example.com", "secret")
# print(user.email)  # test@example.com
# # print(user.password) # AttributeError
# print(user.check_password("secret"))  # True
# print(user.check_password("wrong"))   # False

class User:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __setattr__(self, attr, value):
        match attr:
            case 'password':
                value = hash(value)
            case 'email':
                if '@' not in value:
                    raise AttributeError(value + ' incorrect email format')
        self.__dict__[attr] = value


    def check_password(self, clean_pass) -> bool:
        if self.password == hash(clean_pass):
            return True
        return False


user = User("test@example.com", "secret")

print(user.email)
print(user.check_password("secret"))
print(user.check_password("wrong"))
