from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from abc import abstractmethod


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_driver(self):
        return self.driver

    def get_title(self):
        return self.get_title()

    def get_url(self):
        return self.get_url()

    def open_url(self, url):
        self.driver.get(url)

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

    def is_enabled(self, locator):
        if self.find_element(locator).is_enabled():
            return True
        else:
            return False

    def is_selected(self, locator):
        if self.find_element(locator).is_selected():
            return True
        else:
            return False

    def scroll_to_bottom_of_page(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    @abstractmethod
    def validate_page_load(self):
        pass


class InvalidPageException(Exception):
    """ Throw this exception when you don't find the correct page """
    pass
