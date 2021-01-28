from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests import config


class ElementsLinksArea(BasePage):

    title = "ToolsQA"
    links_path = "/links"
    home_loc = (By.CSS_SELECTOR, '#simpleLink')
    homenouoh_loc = (By.ID, "dynamicLink")
    created_loc = (By.CSS_SELECTOR, '#created')
    link_response_loc = (By.CSS_SELECTOR, '#linkResponse')

    def __init__(self, driver):
        super(ElementsLinksArea, self).__init__(driver)

    def validate_page_load(self):
        assert self.is_displayed(self.home_loc, timeout=15) and \
           self.is_displayed(self.homenouoh_loc, timeout=15) and \
           self.is_displayed(self.created_loc, timeout=15)

    def open_links_page(self):
        self.open_url(self.links_path)

    def select_home_link(self):
        if self.is_displayed(self.home_loc, timeout=15):
            self.find_element(self.home_loc).click()
            # Firefox webdriver bug: webdriver fails to consistently return 2 windows handles
            # Workaround: use explicit wait on windows handles to be 2
            self.number_of_windows_to_be(handles=2, timeout=15)
            index = self.get_number_of_handles()
            self.switch_to_window_handle(index-1)

    def validate_select_home_link(self):
        self.url_to_be(config.baseurl, timeout=15)
        actual_url = self.get_url()
        expected_url = config.baseurl + "/"
        assert actual_url == expected_url

    def select_homenouoh_link(self):
        if self.is_displayed(self.homenouoh_loc, timeout=15):
            self.find_element(self.homenouoh_loc).click()
            # Firefox webdriver bug: webdriver fails to consistently return 2 windows handles
            # Workaround: use explicit wait on windows handles to be 2
            self.number_of_windows_to_be(handles=2, timeout=15)
            index = self.get_number_of_handles()
            self.switch_to_window_handle(index-1)

    def select_created_link(self):
        if self.is_displayed(self.created_loc, timeout=15):
            self.find_element(self.created_loc).click()

    def validate_select_created_link(self):
        assert self.is_text_displayed(self.link_response_loc, "Link has responded with staus", timeout=15)


