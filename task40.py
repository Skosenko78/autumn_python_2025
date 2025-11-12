# Система уведомлений (Полиморфизм)
# todo: Реализовать систему отправки уведомлений пользователям через разные каналы.
#
# Требования:
# Базовый класс NotificationSender с методом send(message, user)
# Дочерние классы:
# EmailSender: отправляет email с темой "Образовательная платформа"
# SMSSender: отправляет SMS (первые 50 символов сообщения)
# PushSender: отправляет push-уведомление с иконкой "🎓"
#
# Класс пользователя User:
# Свойства: name, preferred_notifications (список объектов NotificationSender)

class NotificationSender:

    def send(self, message, user):
        print(f"MAIL TO: {user.name}")
        print(f"TEXT: {message}")


class EmailSender(NotificationSender):

    def send(self, message, user):
        print(f"MAIL TO: {user.name}")
        print(f"SUBJECT: {self.subject}")
        print(f"TEXT: {message}")

    subject = "Образовательная платформа"


class SMSSender(NotificationSender):

    def send(self, message, user):
        print(f"SMS TO: {user.name}")
        print(f"TEXT: {message[:50]}")


class PushSender(NotificationSender):

    def send(self, message, user):
        message = "🎓"
        print(f"PUSH TO: {user.name}")
        print(f"PUSH: {message}")


class User:
    def __init__(self, name, preferred_notifications):
        self.name = name
        self.preferred_notifications = preferred_notifications

# Этот код должен работать после реализации:
def notify_user(user, message):
    for sender in user.preferred_notifications:
        sender.send(message, user)

user = User("Мария", [EmailSender(), PushSender(), SMSSender()])
notify_user(user, "Блок аналитики начинается с 27 октября!")