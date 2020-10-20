from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ElementsBrowserWindowsArea(BasePage):

    brw_wdw_url = "https://demoqa.com/browser-windows"
    tab_btn_loc = (By.CSS_SELECTOR, "#tabButton")
    wdw_btn_loc = (By.CSS_SELECTOR, "#windowButton")
    msg_wdw_btn_loc = (By.CSS_SELECTOR, "#messageWindowButton")
    confirm_msg = "Knowledge increases by sharing but not by saving. Please share this website with your friends and in your organization."

    def __init__(self, driver):
        super(ElementsBrowserWindowsArea, self).__init__(driver)

    def open_browser_window_page(self):
        self.driver.get(self.brw_wdw_url)

    def validate_page_load(self):
        return (self.is_displayed(self.tab_btn_loc, 15)) and \
               (self.is_displayed(self.wdw_btn_loc, 15)) and \
               (self.is_displayed(self.msg_wdw_btn_loc, 15))

    def select_tab_button(self):
        self.click(self.tab_btn_loc)
        index = self.get_number_of_handles()
        self.switch_to_window_handle(index-1)

    def validate_tab_button(self):
        return ("https://demoqa.com/sample" == self.get_url()) and \
               ("This is a sample page" in self.driver.page_source)

    def select_new_window_button(self):
        self.click(self.wdw_btn_loc)
        index = self.get_number_of_handles()
        self.switch_to_window_handle(index-1)

    def select_new_window_message(self):
        index = self.get_number_of_handles()
        self.click(self.msg_wdw_btn_loc)
        self.switch_to_window_handle(index-1)

    def validate_new_window_message(self):
        """
        todo:
        Note: Possible bug in Selenium. Can't get URL or page source after switching to new handle.
        """
        # page = self.driver.page_source
        # x = self.confirm_msg
        # if x in page:
        # # if (self.confirm_msg in self.driver.page_source):
        #     return True
        # return False
