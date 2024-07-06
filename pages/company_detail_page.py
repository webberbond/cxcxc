from selenium.webdriver.common.by import By

from locators.company_detail_page_locators import CompanyDetailPageLocators
from pages.base_page import BasePage


class CompanyDetailPage(BasePage):
    company_detail_page_locators = CompanyDetailPageLocators

    def get_unique_locator(self):
        return By.XPATH, "//h1[normalize-space()='CTE-LOG']"
