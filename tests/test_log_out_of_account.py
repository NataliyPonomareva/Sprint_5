from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import data
from locators import MainPageLocators, AuthFormElements, Authorization


class TestLogOut:
    # Выход по кнопке «Выйти» из личного кабинете
    def test_log_out_of_account(self, driver):
        # Найти "Личный кабинет" и кликнуть по нему:
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Выполнить авторизацию:
        driver.find_element(*Authorization.EMAIL).send_keys(data.EMAIL)
        driver.find_element(*Authorization.PASSWORD).send_keys(data.PASSWORD)
        driver.find_element(*Authorization.BUTTON).click()

        # Войти в личный кабинет:
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Выйти из личного кабинета (найти кнопку "Выход" и кликнуть по ней):
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable(Authorization.BUTTON_EXIT)).click()

        # Проверка выхода, должна загрузиться страница с формой авторизации:
        auth_form = WebDriverWait(driver, 3).until(ec.visibility_of_element_located(AuthFormElements.AUTH_FORM))
        assert auth_form.is_displayed()
