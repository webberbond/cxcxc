import json

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class DriverConfig:
    with open('resources/browser_options.json') as f:
        browser_options_json = json.load(f)

    @staticmethod
    def get_options(browser_name):
        options = None
        if browser_name == "chrome":
            options = ChromeOptions()
        elif browser_name == "firefox":
            options = FirefoxOptions()
        elif browser_name == "edge":
            options = EdgeOptions()

        browser_options = DriverConfig.browser_options_json.get(browser_name, {})
        for argument in browser_options.get("arguments", []):
            options.add_argument(argument)

        experimental_options = browser_options.get("experimental_options", {})
        for key, value in experimental_options.items():
            options.add_experimental_option(key, value)

        return options
