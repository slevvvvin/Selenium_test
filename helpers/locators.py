"""Locators for home page."""
from selenium.webdriver.common.by import By


class HomePageLocators:
    """A class for home page locators.
    All home page locators should come here.
    """

SELECTING_GUEST_MENU = (By.CSS_SELECTOR, '.xp__guests__count')
INCREASE_CHILD_GUEST = (By.CSS_SELECTOR, 'div.sb-group__field:nth-child(2) > div:nth-child(1) > div:nth-child(2) > button:nth-child(4)')
SEARCH_BUTTON = (By.CSS_SELECTOR, '.sb-searchbox__button > span:nth-child(1)')
AGE_SPECIFYING_MENU = (By.CSS_SELECTOR, '.sb-group__children__field > select:nth-child(2)')
SECOND_AGE_SPECIFYING_MENU = (By.CSS_SELECTOR, '.sb-group__children__field > select:nth-child(3)')

CALENDARX = '//*[@id="frm"]/div[3]/div/div[2]/div/div/div[3]/div[1]/table'

CITY_PAGE2 = (By.CSS_SELECTOR, '#basiclayout > div.d-index__section.bui-spacer--large > div:nth-child(2) > div:nth-child(3) > div > div > div > div.unified-postcard__overlay')

SEARCH_BTN = (By.CSS_SELECTOR, '#frm > div.sb-searchbox__row.u-clearfix.-submit.sb-searchbox__footer.-last > div.sb-searchbox-submit-col.-submit-button > button')
CHOOSE_ROOM = '//*[@id="hotellist_inner"]/div[2]/div[2]/div[4]/div/div/div/div/div[2]/div[2]/div/div/div/a'
SEE_AVAILABILITY = '//*[@id="hotellist_inner"]/div[2]/div[2]/div[3]/div/div/div/div/div[2]/div[2]/div/div/div/a'

DATE2 = '//*[@id="frm"]/div[3]/div/div[2]/div/div/div[3]/div[1]/table/tbody/tr[2]/td[4]/span/span'

WHERE_ARE_YOU_GOING_FIELD = (By.CSS_SELECTOR, '#ss')
SELECT_CAGLIARI = (By.CSS_SELECTOR, 'li.sb-autocomplete__item-with_photo:nth-child(1)')
CHECK_IN_DATE = (By.CSS_SELECTOR, '.bui-calendar__date--selected > span:nth-child(1) > span:nth-child(1)')
CHECK_OUT_DATE = (By.CSS_SELECTOR, 'div.bui-calendar__wrapper:nth-child(1) > table:nth-child(2) > tbody:nth-child(2) > tr:nth-child(4) > td:nth-child(4) > span:nth-child(1) > span:nth-child(1)')
CALENDAR_MENU = (By.CSS_SELECTOR, '.xp__dates__checkout > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)')


