from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import MainPageLocators


class TestConstructor:
    def test_go_to_buns(self, driver):  # переход к разделу "Булки"

        # По умолчанию при загрузке приложения выбран раздел "Булки", поэтому:
        # Находим раздел "Соусы" и кликаем по нему
        driver.find_element(*MainPageLocators.SAUCES).click()

        # Находим  раздел "Булки"
        driver.find_element(*MainPageLocators.BUNS).click()

        # Проверяем, что заголовок "Булки" присутствует на странице
        buns_h2 = WebDriverWait(driver, 3).until(ec.visibility_of_element_located(MainPageLocators.BUNS_H2))
        assert buns_h2.is_displayed()

    def test_go_to_sauces(self, driver):  # переход к разделу "Соусы"

        # Находим раздел "Соусы" и кликаем по нему
        driver.find_element(*MainPageLocators.SAUCES).click()

        # Проверяем, что заголовок "Соусы" присутствует на странице
        sauces_h2 = WebDriverWait(driver, 3).until(ec.visibility_of_element_located(MainPageLocators.SAUCES_H2))
        assert sauces_h2 .is_displayed()

    def test_go_to_fillings(self, driver):  # переход к разделу "Начинки"

        # Находим раздел "Начинки" и кликаем по нему
        driver.find_element(*MainPageLocators.FILLINGS).click()

        # Проверяем, что заголовок "Начинки" присутствует на странице
        fillings_h2 = WebDriverWait(driver, 3).until(ec.visibility_of_element_located(MainPageLocators.FILLINGS_H2))
        assert fillings_h2.is_displayed()
