from selenium.webdriver.common.by import By


class MainPageLocators:  # Указатели главной страницы
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text() = 'Личный Кабинет']")  # "Личный кабинет"
    LOG_IN_ACCOUNT_BUTTON = (By.XPATH, "//button[text() = 'Войти в аккаунт']")   # кнопка "Войти в аккаунт"
    CONSTRUCTOR = (By.XPATH, "//p[text() = 'Конструктор']")  # "Конструктор"
    CONSTRUCTOR_PAGE = (By.XPATH, "//button[text()='Оформить заказ']")  # Страница конструктора
    CONSTRUCTOR_BUN = (By.XPATH, "//span[text() = 'Булки'")  # Раздел конструктора "Булки"
    BUNS = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]')  # Раздел конструктора "Булки"
    BUNS_H2 = (By.XPATH, "//h2[text()='Булки']")  # Заголовок "Булки" в ленте
    SAUCES = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]')  # Раздел конструктора "Соусы"
    SAUCES_H2 = (By.XPATH, "//h2[text()='Соусы']")  # Заголовок "Соусы" в ленте
    FILLINGS = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]')  # Раздел конструктора "Начинки"
    FILLINGS_H2 = (By.XPATH, "//h2[text()='Начинки']")  # Заголовок "Начинки" в ленте


class RegistrationPageLocators:  # Страница регистрации
    NAME_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')  # поле "Имя"
    EMAIL_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')  # поле "Email"
    PASSWORD_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input')  # поле "Пароль"
    REGISTER_BUTTON = (By.XPATH, "//button[text() = 'Зарегистрироваться']")  # кнопка "Зарегистрироваться"
    AUTH_LINK = (By.XPATH, "//a[text() = 'Войти']")  # ссылка "Войти"
    ERROR_MESSAGE = (By.XPATH, "//p[text() = 'Некорректный пароль']")  # сообщение об ошибке Некорректный пароль


class Authorization:  # Авторизация
    # поле "Email":
    EMAIL = (By.XPATH, "//input[(@class = 'text input__textfield text_type_main-default') and (@type = 'text')]")

    # поле "Пароль":
    PASSWORD = (By.XPATH, "//input[(@class = 'text input__textfield text_type_main-default') and (@type = 'password')]")

    # кнопка 'Войти':
    BUTTON = (By.XPATH, "//button[text() = 'Войти']")

    # кнопка 'Выход':
    BUTTON_EXIT = (By.XPATH, "//button[(@class = 'Account_button__14Yp3 text text_type_main-medium "
                             "text_color_inactive') and text() = 'Выход']")


class AuthFormElements:  # Форма аутентификации
    AUTH_FORM = (By.XPATH, "//h2[text() = 'Вход']")  # форма с заголовком "Вход"
    AUTH_PAGE = (By.XPATH, "//div[(@class = 'Auth_login__3hAey')]")  # страница входа для зарегистрированных
    # пользователей
    REGISTER_LINK = (By.XPATH, "//a[text() = 'Зарегистрироваться']")  # ссылка "Зарегистрироваться"
    RECOVER_PASSWORD_LINK = (By.XPATH, "//a[text() = 'Восстановить пароль']")  # ссылка "Восстановить пароль"
    RECOVER_FORM = (By.XPATH, "//h2[text() = 'Восстановление пароля']")  # форма "Восстановления пароля"
    RECOVER_LINK = (By.XPATH, "//a[text() = 'Войти']")  # ссылка "Войти"