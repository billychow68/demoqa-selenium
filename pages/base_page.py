from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from os import getcwd
from abc import abstractmethod
from pytest_html import extras


class BasePage:
    """Base class for page object model"""

    _handles = None

    def __init__(self, driver_):
        self.driver = driver_

    def get_driver(self):
        return self.driver

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def open_url(self, url):
        self.driver.get(url)
        self._update_window_handles()

    def open_url_in_new_window(self, url):
        """Open the URL in a new tab."""
        js = f'window.open({url})'
        self.driver.execute_script(js)
        self._update_window_handles()

    def close(self):
        """Close tab"""
        self.driver.close()
        self._update_window_handles()

    def get_number_of_handles(self):
        self._update_window_handles()
        return len(self._handles)

    def _update_window_handles(self):
        """Update the private _handles class variable with all the window (tabs) handles."""
        self._handles = self.driver.window_handles

    def switch_to_window_handle(self, index):
        self.driver.switch_to.window(self._handles[index])

    def find_element(self, locator):
        return self.driver.find_element(locator[0], locator[1])

    def click(self, locator):
        self.find_element(locator).click()

    def double_click(self, locator):
        elem = self.find_element(locator)
        action = ActionChains(self.driver)
        action.double_click(on_element=elem)
        action.perform()

    def right_click(self, locator):
        elem = self.find_element(locator)
        action = ActionChains(self.driver)
        action.context_click(on_element=elem)
        action.perform()

    def send_keys(self, locator, input_text):
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(input_text)

    def is_displayed(self, locator, timeout=0):
        if timeout > 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(ec.visibility_of_element_located((locator[0], locator[1])))
            except TimeoutException:
                return False
            else:
                return True
        else:
            try:
                return self.find_element(locator).is_displayed()
            except NoSuchElementException:
                return False

    def is_text_displayed(self, locator, text, timeout=0):
        if timeout >= 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(ec.text_to_be_present_in_element(locator, text))
            except TimeoutException:
                return False
            else:
                return True

    def is_enabled(self, locator):
        return self.find_element(locator).is_enabled()

    def is_selected(self, locator):
        return self.find_element(locator).is_selected()

    def scroll_to_bottom_of_page(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    @abstractmethod
    def validate_page_load(self):
        pass


class InvalidPageException(Exception):
    """ Throw this exception when you don't find the correct page """
    pass
