# Ссылка на приложение
from helpers import HelpEmail, HelpPassword

DRIVER = 'https://stellarburgers.nomoreparties.site/'

# Зарегистрированный пользователь:
NAME = "Наталья"
EMAIL = "nata_ponomareva_09_111@ya.ru"
PASSWORD = "555555"

# Валидные данные для регистрации пользователя:
NAME_INPUT = "Ната"
EMAIL_INPUT = (HelpEmail.generate_email())
PASSWORD_INPUT = (HelpPassword.generate_password())

# Невалидные данные для регистрации пользователя:
PASSWORD_ERROR = "123"