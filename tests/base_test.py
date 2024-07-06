import unittest

from pages.company_detail_page import CompanyDetailPage
from pages.company_setup_page import CompanySetupPage
from pages.login_page import LoginPage
from utils.browser import BrowserFactory
from utils.config import AppConfig


class BaseTest(unittest.TestCase):
    def initialize_driver(self):
        self.driver = BrowserFactory.get_driver("chrome")
        self.driver.get(AppConfig.BASE_URL)
        yield self.driver

    def setUp(self):
        self.driver = next(self.initialize_driver())

        self.login_page = LoginPage(self.driver)
        self.company_setup_page = CompanySetupPage(self.driver)
        self.company_detail_page = CompanyDetailPage(self.driver)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        del BrowserFactory._local.driver

