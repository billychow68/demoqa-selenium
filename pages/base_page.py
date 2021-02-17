import os
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from abc import abstractmethod
from tests import config

class BasePage:
    """Base class for page object model"""

    _handles = None

    def __init__(self, driver_):
        self.driver = driver_

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def open_url(self, path):
        """Open URL using baseurl and path"""
        self.driver.get(config.baseurl + path)
        self._update_window_handles()

    def open_url_in_new_window(self, url):
        """Open the URL in a new tab."""
        js = f'window.open({url})'
        self.driver.execute_script(js)
        self._update_window_handles()

    def open_file(self, path):
        """Open URL using file:// and path"""
        self.driver.get("file://" + path)

    def close(self):
        """Close tab"""
        self.driver.close()
        self._update_window_handles()

    def get_number_of_handles(self):
        # todo: may want to refactor this to return self._update_window_handles().size() instead
        self._update_window_handles()
        return len(self._handles)

    def _update_window_handles(self):
        """
        Update the private _handles class variable with all window (tabs) handles.
        """
        self._handles = self.driver.window_handles

    def switch_to_window_handle(self, index):
        """
        Method for switching to a any window handle (zero-based).

        Example of switching to the newest window handle:
            index = self.get_number_of_handles()
            self.switch_to_window_handle(index-1)
        """
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
        """Explicit wait on element to be visible and enabled."""
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
        """Explicit wait on element's text to be present."""
        if timeout >= 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(ec.text_to_be_present_in_element(locator, text))
            except TimeoutException:
                return False
            else:
                return True
        else:
            return False

    def is_file_exists(self, path, timeout=0):
        """Poor man's wait on file to exist."""
        for t in range(0, timeout):
            # todo: exists or isfile?
            if os.path.exists(path):
                return True
            else:
                time.sleep(1)
        return False

    def is_alert_present(self, timeout=0):
        """Explicit wait on an alert."""
        if timeout >= 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(ec.alert_is_present())
            except TimeoutException:
                return False
            else:
                return True
        else:
            return False

    def title_is(self, title, timeout=0):
        """Explicit wait on the exact title to be present."""
        if timeout >= 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(ec.title_is(title=title))
            except TimeoutException:
                return False
            else:
                return True
        else:
            return False

    def url_to_be(self, url, timeout=0):
        """Explicit wait on the exact URL to be present."""
        if timeout >= 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(ec.url_to_be(url=url))
            except TimeoutException:
                return False
            else:
                return True
        else:
            return False

    def number_of_windows_to_be(self, *, handles: int, timeout=0):
        """Explicit wait on the number of window handles to be a certain value."""
        if timeout >= 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(ec.number_of_windows_to_be(handles))
            except TimeoutException:
                return False
            else:
                return True
        else:
            return False


    def is_enabled(self, locator):
        return self.find_element(locator).is_enabled()

    def is_selected(self, locator):
        return self.find_element(locator).is_selected()

    def scroll_to_bottom_of_page(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    def get_alert_text(self):
        return self.driver.switch_to.alert.text

    def alert_send_keys(self, text):
        self.driver.switch_to.alert.send_keys(text)

    def close_modal_dialog(self, locator):
        """This method will click on the Close or X button on the modal dialog"""
        if self.is_displayed(locator):
            self.click(locator)

    def get_modal_dialog_text(self, locator):
        if self.is_displayed(locator):
            return self.find_element(locator).text
        return None

    @abstractmethod
    def validate_page_load(self):
        pass


class InvalidPageException(Exception):
    """ Throw this exception when you don't find the correct page """
    pass
