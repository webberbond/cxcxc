from selenium.webdriver.common.by import By


class CompanySetupPageLocators:
    COMPANY_SETUP_TEXT = (By.XPATH, "//h3[normalize-space()='Company Setup']")

    INACTIVE_DROPDOWN_BUTTON = (By.XPATH, "//span[@title='Inactive']")
    ACTIVE_DROPDOWN_OPTION = (By.XPATH, "//div[@title='Active']")

    COMPANY_NAVIGATE_BUTTON = (By.XPATH, "(//span[contains(text(),'Navigate')])[1]")
