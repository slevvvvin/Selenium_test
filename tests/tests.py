"""Test case for checking if a number of age input
menus is equal to a number of children guests."""

import unittest
from selenium import webdriver
from pages import home_page as hp


class NumberOfAgeInputs(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.home_page = hp.HomePage(self.driver)
        self.home_page.go_to_home_page()

    def tearDown(self):
        self.driver.close()


    def test_number_of_age_inputs_increases(self):

        """Test to check if a number of age input
        menu is equal to number of children guests."""
        self.home_page.click_on_guest_menu()
        self.home_page.increase_number_of_children()
        self.assertTrue(self.home_page.age_input_is_present)


    def test_on_choosing_any_city(self):

        """Test to check if a calendar and page with listed hotels is opened"""
        self.home_page.choose_a_city()
        self.assertTrue(self.home_page.calendar_is_present(),'Calendar isn"t present')
        self.assertTrue(self.home_page.is_the_list_of_hotels_opened(), 'no list with hotels')


    def test_search_form(self):

        """Test to check if each result entry has booking price or banner saying no free places"""
        self.home_page.choose_a_city()
        self.home_page.submit_search_form()
        self.assertTrue(self.home_page.is_result_has_price_and_free_places(),
                        'no elements on page')



if __name__ == "main":
    unittest.main(verbosity=2)