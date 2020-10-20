from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class ElementsButtonsArea(BasePage):

    buttons_url = "http://demoqa.com/buttons"
    doubleclick_loc = (By.ID, "doubleClickBtn")
    rightclick_loc = (By.ID, 'rightClickBtn')
    clickme_loc = (By.CSS_SELECTOR, '#Ij1FH')

    def __init__(self, driver):
        super(ElementsButtonsArea, self).__init__(driver)

    def open_buttons_page(self):
        self.driver.get(self.buttons_url)

    def validate_page_load(self):
        if self.is_displayed(self.doubleclick_loc, 15) and \
           self.is_displayed(self.rightclick_loc, 15):
            # if self.is_displayed(self.clickme_loc, 5):
            return True
        else:
            return False

    def select_doubleclick_button(self):
        self.double_click(self.doubleclick_loc)

    def select_rightclick_button(self):
        self.right_click(self.rightclick_loc)

    def validate_doubleclick(self):
        if "You have done a double click" in self.driver.page_source:
            return True
        else:
            return False

    def validate_rightclick(self):
        if "You have done a right click" in self.driver.page_source:
            return True
        else:
            return False

