import data
from locators import MainPageLocators, AuthFormElements
from locators import RegistrationPageLocators


class TestRegistration:
    # Тест на успешную регистрацию
    def test_successful_registration(self, driver):
        # Найти кнопку "Личный кабинет" и кликнуть по ней
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Найти ссылку "Зарегистрироваться" и кликнуть по ней
        driver.find_element(*AuthFormElements.REGISTER_LINK).click()

        # Заполнение формы для успешной регистрации
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(data.NAME_INPUT)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(data.EMAIL_INPUT)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(data.PASSWORD_INPUT)  # допустимый пароль
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        # Ожидание загрузки страницы с вводом данных зарегистрированного пользователя (для входа в личный кабинет)
        auth_page = driver.find_element(*AuthFormElements.AUTH_PAGE)
        assert auth_page.is_displayed()

    # Тест на проверку ошибки при регистрации
    def test_registration_error(self, driver):

        # Найти кнопку "Личный кабинет" и кликнуть по ней
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Найти ссылку "Зарегистрироваться" и кликнуть по ней
        driver.find_element(*AuthFormElements.REGISTER_LINK).click()

        # Заполнение формы с некорректным паролем
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(data.NAME_INPUT)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(data.EMAIL_INPUT)
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(data.PASSWORD_ERROR)  # короткий пароль
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()

        # Проверка на наличие сообщения об ошибке
        error_message = driver.find_element(*RegistrationPageLocators.ERROR_MESSAGE)
        assert error_message.is_displayed()
