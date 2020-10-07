"""Base page, parent page for other pages."""
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

"""URLs used when testing webapp functionality."""
BASE_URL = "https://www.booking.com/"

class BasePage:
    """Docstring for base page."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def find_element_by_css(self, by_css):
        """Method for finding element on the page.
        """
        return self.wait.until(EC.visibility_of_element_located(by_css))

    def click_on_element_by_css(self, by_css):
        """Method for clicking on the element."""
        self.wait.until(EC.element_to_be_clickable(by_css)).click()

    def go_to_page(self, page):
        """Method for going to the specific page.
        """
        self.driver.get(page)

    def fill_in_text_field_by_css(self, by_css, text):
        """Method for filling in the text in particular field."""
        self.wait.until(EC.visibility_of_element_located(by_css)
                        ).send_keys(text)

    def find_element_by_xpath(self, element_xpath):
        """Method for finding element on the page"""
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, element_xpath)))

    def click_on_element_by_xpath(self, by_xpath):
        """Method for clicking on the element"""
        self.wait.until(EC.element_to_be_clickable(by_xpath)).click()

    def click_on_element_by_link_text(self, text):
        """Method for clicking on the text element"""
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,text))).click()

    def find_element_by_link_text(self, text):
        """Method for finding element on the page by text"""
        return self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, text)))

