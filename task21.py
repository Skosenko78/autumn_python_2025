#todo: Задан шаблон config_default.txt, где каждому в текстовом файле параметру
# нужно сопоставить данные для подстановки.

# Содержимое файла config_default.txt
# # Конфигурация приложения.
# app_name    = ?
# version     = ?
# debug       = ?
#
# # Настройки базы данных
# db_host     = ?
# db_port     = ?
# db_name     = ?
# db_user     = ?
# db_password = ?
#
# # Настройки API
# api_key     = ?
# api_secret  = ?
# base_url    = ?
#
# # Пути
# log_file    = ?
# data_dir    = ?
# temp_dir    = ?


# Данные для подстановки
config_values = {
    'app_name': 'NextGen',
    'version': '1.0.0',
    'debug':  True,
    'db_host': 'localhost',
    'db_port': 5432,
    'db_name': 'my_database',
    'db_user': 'admin',
    'db_password': 'secret123',
    'api_key': 'ak_123456789',
    'api_secret': 'sk_987654321',
    'base_url': 'https://api.example.com',
    'log_file': '/var/log/app.log',
    'data_dir': '/opt/app/data',
    'temp_dir': '/tmp/app',
    'max_workers': 10,
    'timeout': 30,
    'retry_attempts': 3
}

# В итоге вместо "?" должны подставиться значения и получиться файл config.txt:

# # Конфигурация приложения
# app_name    =  "NextGen"
# version     =  '1.0.0'
# debug       =  True
#
# # Настройки базы данных
# db_host     =  5432
# .....

f_default = open("config_default.txt","tr")
f_out = open("config.txt", "tw")

for line in f_default:
    new_line = None
    for key in config_values:
        if key in line:
            new_line = line.replace('?',str(config_values[key]))
            f_out.write(new_line)
    if new_line == None:
        f_out.write(line)

f_default.close()
f_out.close()
