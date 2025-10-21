#todo: Вы пишете скрипт для очистки временных файлов. Создайте список полных путей к временным файлам (с расширениями .tmp, .bak),
# добавив к каждому путь "/tmp/".
files = [
    "document.pdf",
    "temp_backup.tmp",
    "image.jpg",
    "cache.tmp",
    "report.docx",
    "old_data.bak"
]

# результат:
#['/tmp/temp_backup.tmp', '/tmp/cache.tmp', '/tmp/old_data.bak']

abs_path = ['/tmp/'+file for file in files if file.endswith(('.bak','.tmp'))]
print(abs_path)