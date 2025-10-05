# todo: Преобразуйте переменную age и foo в число
# age = "23"
# foo = "23abc"
int(age)
23
int(foo)
# Выводится ошибка ValueError: invalid literal for int() with base 10: '23abc'. Без ошибки:
int(foo[:2])
23
#
# Преобразуйте переменную age в Boolean
# age = "123abc"
bool(age)
True
#
# Преобразуйте переменную flag в Boolean
# flag = 1
bool(flag)
True
#
# Преобразуйте значение в Boolean
# str_one = "Privet"
# str_two = ""
bool(str_one)
True
bool(str_two)
False
#
# Преобразуйте значение 0 и 1 в Boolean
#
bool(0)
False
bool(1)
True
# Преобразуйте False в строку
str(False)
'False'
