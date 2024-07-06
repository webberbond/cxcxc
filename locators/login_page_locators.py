from selenium.webdriver.common.by import By


class LoginPageLocators:
    SERVICE_ENTRANCE_TEXT = (By.XPATH, "//h1[normalize-space()='Service Entrance']")

    EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, "input[placeholder='Enter username']")
    PASSWORD_INPUT_FIELD = (By.CSS_SELECTOR, "input[placeholder='Enter password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    ERROR_NOTIFICATION = (By.XPATH, "//div[contains(@class, 'ant-notification-notice-error')]")
