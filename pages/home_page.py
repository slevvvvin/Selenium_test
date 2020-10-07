from selenium.common.exceptions import TimeoutException
from pages import base_page
from pages.base_page import BasePage
from helpers import locators as hpl


"""Class for the Home page with methods which using for testing"""

class HomePage(BasePage):
    """Docstring for Home page."""

    def click_on_guest_menu(self):
        """Method for clicking on guest menu section."""
        self.click_on_element_by_css(hpl.SELECTING_GUEST_MENU)

    def increase_number_of_children(self):
        """Method for increasing amount of guesting children."""
        self.click_on_element_by_css(hpl.INCREASE_CHILD_GUEST)
        self.click_on_element_by_css(hpl.INCREASE_CHILD_GUEST)

    def age_input_is_present(self):
        """Method for verification of age input menu presence."""
        try:
            self.find_element_by_css(hpl.AGE_SPECIFYING_MENU)
            self.find_element_by_css(hpl.SECOND_AGE_SPECIFYING_MENU)
            return True
        except TimeoutException:
            return False

    def is_the_list_of_hotels_opened(self):

        """Method for verification page with listed hotels"""
        try:
            self.find_element_by_link_text('Наши рекомендации')
            return True
        except TimeoutException:
            return False


    def calendar_is_present(self):
        """Method for verification of calendar."""
        try:
            self.find_element_by_xpath(hpl.CALENDARX)
            return True
        except TimeoutException:
            return False

    def go_to_home_page(self):
        """Methods for opening home page."""
        self.driver.get(base_page.BASE_URL)

    def choose_a_city(self):
        """Methods for opening city page."""
        self.click_on_element_by_css(hpl.CITY_PAGE2)


    def enter_search_query(self):
        """Method for entering a search request into
        "where are you going?" field"""
        self.fill_in_text_field_by_css(hpl.WHERE_ARE_YOU_GOING_FIELD, 'Cagliari')

    def submit_search_form(self):

        """Method for submitting search form"""
        self.element = self.find_element_by_xpath(hpl.DATE2)
        self.driver.execute_script("arguments[0].click();", self.element)
        self.click_on_element_by_css(hpl.SEARCH_BTN)

    def is_result_has_price_and_free_places(self):

        """Method for verification price and free places of hotels"""
        try:

            self.find_element_by_link_text('Выбрать номер')
            self.find_element_by_link_text('UAH')
            return True
        except TimeoutException:
            return False

