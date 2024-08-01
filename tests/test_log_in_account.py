from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import data
from locators import MainPageLocators, AuthFormElements, RegistrationPageLocators, Authorization


class TestLogIn:
    def test_login_via_login_button_on_homepage(self, driver):   # вход по кнопке «Войти в аккаунт» на главной странице
        # Найти кнопку "Войти в аккаунт" и кликнуть по ней
        driver.find_element(*MainPageLocators.LOG_IN_ACCOUNT_BUTTON).click()

        # Выполни авторизацию
        driver.find_element(*Authorization.EMAIL).send_keys(data.EMAIL)
        driver.find_element(*Authorization.PASSWORD).send_keys(data.PASSWORD)
        driver.find_element(*Authorization.BUTTON).click()

        # Проверка загрузки cтраницы конструктора
        constructor_page = driver.find_element(*MainPageLocators.CONSTRUCTOR_PAGE)
        assert constructor_page.is_displayed()

    def test_login_via_personal_account_button(self, driver):  # вход через кнопку «Личный кабинет»

        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()  # Найти "Личный кабинет" и кликнуть

        # Выполни авторизацию
        driver.find_element(*Authorization.EMAIL).send_keys(data.EMAIL)
        driver.find_element(*Authorization.PASSWORD).send_keys(data.PASSWORD)
        driver.find_element(*Authorization.BUTTON).click()

        # Проверка загрузки cтраницы конструктора
        constructor_page = driver.find_element(*MainPageLocators.CONSTRUCTOR_PAGE)
        assert constructor_page.is_displayed()

    def test_login_via_registration_form(self, driver):  # вход через кнопку в форме регистрации
        # Найти "Личный кабинет" и кликнуть
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Найти ссылку "Зарегистрироваться" и кликнуть по ней
        driver.find_element(*AuthFormElements.REGISTER_LINK).click()

        # В строке с текстом "Уже зарегистрированы?" найти ссылку "Войти" и кликнуть по ней
        driver.find_element(*RegistrationPageLocators.AUTH_LINK).click()

        # Выполни авторизацию
        driver.find_element(*Authorization.EMAIL).send_keys(data.EMAIL)
        driver.find_element(*Authorization.PASSWORD).send_keys(data.PASSWORD)
        driver.find_element(*Authorization.BUTTON).click()

        # Проверка загрузки cтраницы конструктора
        constructor_page = driver.find_element(*MainPageLocators.CONSTRUCTOR_PAGE)
        assert constructor_page.is_displayed()

    def test_login_via_password_recovery_form(self, driver):  # вход через кнопку в форме восстановления пароля
        # Найти "Личный кабинет" и кликнуть
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Найти ссылку "Восстановить пароль" и кликнуть по ней
        driver.find_element(*AuthFormElements.RECOVER_PASSWORD_LINK).click()

        # дождаться загрузки формы "Восстановление пароля"
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(AuthFormElements.RECOVER_FORM))

        # В строке с текстом "Вспомнили пароль?" найти ссылку "Войти" и кликнуть по ней
        driver.find_element(*AuthFormElements.RECOVER_LINK).click()

        # Выполни авторизацию
        driver.find_element(*Authorization.EMAIL).send_keys(data.EMAIL)
        driver.find_element(*Authorization.PASSWORD).send_keys(data.PASSWORD)
        driver.find_element(*Authorization.BUTTON).click()

        # Проверка загрузки cтраницы конструктора
        constructor_page = driver.find_element(*MainPageLocators.CONSTRUCTOR_PAGE)
        assert constructor_page.is_displayed()
