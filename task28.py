#todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.
# Ответ: сдвиг на 20 символов, зашифрованная фраза: although that way may not be obvious at first unless you're dutch.'

phrase_encr :str = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.'"
letters_ascii :list = []
shift :int = 1

for i in range(ord('a'),ord('z') + 1):
    letters_ascii.append(i)

letters_len = len(letters_ascii)

while shift <= letters_len:
    phrase = ''
    for char_ in phrase_encr:
        char_ascii = ord(char_)
        if char_ascii in letters_ascii:
            curr_index = letters_ascii.index(char_ascii)
            new_index = curr_index + shift
            if new_index > letters_len - 1:
                new_index = new_index - len(letters_ascii)
            phrase += chr(letters_ascii[new_index])
        else:
            phrase += char_
    print(f"Shift +{str(shift)}: {phrase}")
    shift += 1