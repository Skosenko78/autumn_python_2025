#todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.
#
# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!
string_ = '8 5 12 12 15 , 0 23 15 18 12 4 !'

cnt :int = 0
alpha_dict :dict = {0 : ' '}
result: list = []

for i in range(ord('a'),ord('z')):
    cnt += 1
    alpha_dict[cnt] = chr(i)

for char_ in string_.split():
    if char_ != ' ':
        result.append(alpha_dict[int(char_)]) if char_.isdigit() else result.append(char_)

print(''.join(result))
