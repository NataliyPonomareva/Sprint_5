from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import data
from locators import MainPageLocators, Authorization


class TestTransfer:
    # Переход из личного кабинета в конструктор
    def test_transfer_from_personal_account_to_constructor(self, driver):

        # Найти "Личный кабинет" и кликнуть по нему
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Выполнить авторизацию:
        driver.find_element(*Authorization.EMAIL).send_keys(data.EMAIL)
        driver.find_element(*Authorization.PASSWORD).send_keys(data.PASSWORD)
        driver.find_element(*Authorization.BUTTON).click()

        # Найти раздел "Конструктор" и кликнуть по нему
        driver.find_element(*MainPageLocators.CONSTRUCTOR).click()  # Найти раздел "Конструктор" и кликнуть по нему

        # Проверка перехода в конструктор
        constructor_page = WebDriverWait(driver, 3).until(ec.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_PAGE))
        assert constructor_page.is_displayed()
