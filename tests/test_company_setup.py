from tests.base_test import BaseTest
from utils.config import AppConfig


class TestCompanySetup(BaseTest):
    def test_create_driver(self):
        self.login_page.enter_email(AppConfig.DASHBOARD_EMAIL)
        self.login_page.enter_password(AppConfig.DASHBOARD_PASSWORD)
        self.login_page.click_login_button()

        self.assertTrue(self.company_setup_page.is_page_opened(), "Company setup page was not opened")

        self.company_setup_page.click_dropdown_button()
        self.company_setup_page.click_active_option_button()
        self.company_setup_page.click_navigate_button()

        self.assertTrue(self.company_detail_page.is_page_opened(), "Company detail page was not opened")
