from tests.base_test import BaseTest
from utils.config import AppConfig


class LoginTest(BaseTest):
    def test_successful_login(self):
        self.login_page.enter_email(AppConfig.DASHBOARD_EMAIL)
        self.login_page.enter_password(AppConfig.DASHBOARD_PASSWORD)
        self.login_page.click_login_button()

        self.assertTrue(self.company_setup_page.is_page_opened(), "Company setup page was not opened")

    def test_error_email_login(self):
        self.login_page.enter_email(AppConfig.DASHBOARD_ERROR_EMAIL)
        self.login_page.enter_password(AppConfig.DASHBOARD_PASSWORD)
        self.login_page.click_login_button()

        self.assertEqual(self.login_page.get_notification_text(), "Invalid username", "Error text is incorrect")

    def test_error_password_login(self):
        self.login_page.enter_email(AppConfig.DASHBOARD_EMAIL)
        self.login_page.enter_password(AppConfig.DASHBOARD_ERROR_PASSWORD)
        self.login_page.click_login_button()

        self.assertEqual(self.login_page.get_notification_text(), "Invalid password", "Error text is incorrect")

    def test_forgot_password(self):
        pass
