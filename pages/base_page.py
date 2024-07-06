import os
from abc import abstractmethod

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.logger import test_logger


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        test_logger.info(f"Element {locator} was found!")
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_elements(self, locator):
        test_logger.info(f"Element {locator} was found!")
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator):
        test_logger.info(f"Click element {locator} was done!")
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        test_logger.info(f"Text was entered to field {locator}!")
        self.find_element(locator).send_keys(text)

    def clear_text(self, locator):
        test_logger.info(f"Textfield {locator} was cleared!")
        self.find_element(locator).clear()

    def get_text(self, element):
        test_logger.info(f"Getting text from element: {element}!")
        return self.find_element(element).text

    def is_visible(self, locator):
        test_logger.info(f"Checking if element {locator} is visible!")
        return self.find_element(locator).is_displayed()

    def get_alert_text(self):
        test_logger.info(f"Getting text from alert!")
        return self.driver.switch_to.alert.text

    @abstractmethod
    def get_unique_locator(self):
        pass

    def is_page_opened(self):
        test_logger.info("Checking if page is opened!")
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.get_unique_locator()))
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def take_screen_shot(self, file_name):
        screenshot_path = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(screenshot_path, exist_ok=True)
        screenshot_file = os.path.join(screenshot_path, f"{file_name}.png")
        self.driver.save_screenshot(screenshot_file)
        test_logger.info("Screenshot was taken %s", file_name)
