from selenium.webdriver.common.by import By

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    login_locators = LoginPageLocators

    def get_unique_locator(self):
        return By.XPATH, "//h1[normalize-space()='Service Entrance']"

    def enter_email(self, email):
        return self.enter_text(self.login_locators.EMAIL_INPUT_FIELD, email)

    def enter_password(self, password):
        return self.enter_text(self.login_locators.PASSWORD_INPUT_FIELD, password)

    def click_login_button(self):
        return self.click(self.login_locators.LOGIN_BUTTON)

    def get_notification_text(self):
        return self.get_text(self.login_locators.ERROR_NOTIFICATION)
