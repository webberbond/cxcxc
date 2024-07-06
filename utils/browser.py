import threading

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utils.driver_config import DriverConfig


class BrowserFactory:
    _local = threading.local()

    @staticmethod
    def get_driver(browser_name):
        if not hasattr(BrowserFactory._local, 'driver'):
            if browser_name.lower() == 'chrome':
                BrowserFactory._local.driver = BrowserFactory._get_chrome_driver()
            elif browser_name.lower() == 'firefox':
                BrowserFactory._local.driver = BrowserFactory._get_firefox_driver()
            elif browser_name.lower() == 'edge':
                BrowserFactory._local.driver = BrowserFactory._get_edge_driver()
            else:
                raise ValueError(f"Unsupported browser: {browser_name}")
        return BrowserFactory._local.driver

    @staticmethod
    def _get_chrome_driver():
        options = DriverConfig.get_options("chrome")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        return driver

    @staticmethod
    def _get_firefox_driver():
        options = DriverConfig.get_options("firefox")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        driver.maximize_window()
        return driver

    @staticmethod
    def _get_edge_driver():
        options = DriverConfig.get_options("edge")
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)
        driver.maximize_window()
        return driver
