from locators import MainPageLocators, AuthFormElements


class TestTransfer:
    # Открытие страницы входа для зарегистрированных пользователей по клику на «Личный кабинет»
    def test_transfer_personal_account(self, driver):

        # Найти "Личный кабинет" и кликнуть по нему
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        # Проверка загрузка формы аутентификации
        auth_page = driver.find_element(*AuthFormElements.AUTH_PAGE)
        assert auth_page.is_displayed()
