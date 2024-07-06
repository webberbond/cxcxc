import time

from selenium.webdriver.common.by import By

from locators.company_setup_page_locators import CompanySetupPageLocators
from pages.base_page import BasePage


class CompanySetupPage(BasePage):
    company_setup_page_locators = CompanySetupPageLocators

    def get_unique_locator(self):
        return By.XPATH, "//h3[normalize-space()='Company Setup']"

    def click_dropdown_button(self):
        return self.click(self.company_setup_page_locators.INACTIVE_DROPDOWN_BUTTON)

    def click_active_option_button(self):
        return self.click(self.company_setup_page_locators.ACTIVE_DROPDOWN_OPTION)

    def click_navigate_button(self):
        time.sleep(2)
        return self.click(self.company_setup_page_locators.COMPANY_NAVIGATE_BUTTON)
