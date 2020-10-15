from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class ElementsLinksArea(BasePage):

    links_url = "https://demoqa.com/links"
    home_loc = (By.CSS_SELECTOR, '#simpleLink')
    homenouoh_loc = (By.ID, "dynamicLink")
    created_loc = (By.CSS_SELECTOR, '#created')
    link_response_loc = (By.CSS_SELECTOR, '#linkResponse')

    def __init__(self, driver):
        super(ElementsLinksArea, self).__init__(driver)

    def validate_page_load(self):
        if self.is_displayed(self.home_loc, 30) and \
           self.is_displayed(self.homenouoh_loc, 30) and \
           self.is_displayed(self.created_loc, 30):
            return True
        else:
            return False

    def open_links_page(self):
        self.open_url(self.links_url)

    def select_home_link(self):
        if self.is_displayed(self.home_loc, 30):
            self.find_element(self.home_loc).click()
            index = self.get_number_of_handles()
            self.switch_to_window_handle(index-1)

    def validate_select_home_link(self):
        url = self.get_url()
        if url == "https://demoqa.com/":
            return True
        else:
            return False

    def select_homenouoh_link(self):
        if self.is_displayed(self.homenouoh_loc, 30):
            self.find_element(self.homenouoh_loc).click()
            index = self.get_number_of_handles()
            self.switch_to_window_handle(index-1)

    def select_created_link(self):
        if self.is_displayed(self.created_loc, 30):
            self.find_element(self.created_loc).click()

    def validate_select_created_link(self):
        return self.is_text_displayed(self.link_response_loc, "Link has responded with staus", 30)


