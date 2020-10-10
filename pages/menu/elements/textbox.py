from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class ElementsTextboxArea(BasePage):

    def __init__(self, driver):
        super(ElementsTextboxArea, self).__init__(driver)

    textbox_url = "https://demoqa.com/text-box"
    full_name_label_loc = (By.ID, "userName-label")
    full_name_loc = (By.ID, "userName")
    email_label_loc = (By.ID, "userEmail-label")
    email_loc = (By.ID, "userEmail")
    current_address_label_loc = (By.ID, "currentAddress-label")
    current_address_loc = (By.ID, "currentAddress")
    permanent_address_label_loc = (By.ID, "permanentAddress-label")
    elememts_permanentaddress_loc = (By.ID, "permanentAddress")
    submit_button_loc = (By.ID, "submit")

    def open_textbox_page(self):
        self.open_url(self.textbox_url)

    def validate_page_load(self):
        if self.is_displayed(self.full_name_loc, 30) and \
           self.is_displayed(self.full_name_label_loc, 10) and \
           self.is_displayed(self.email_loc, 30) and \
           self.is_displayed(self.email_label_loc, 30) and \
           self.is_displayed(self.current_address_loc, 30) and \
           self.is_displayed(self.current_address_label_loc, 30) and \
           self.is_displayed(self.elememts_permanentaddress_loc, 30) and \
           self.is_displayed(self.permanent_address_label_loc, 30) and \
           self.is_displayed(self.submit_button_loc, 30):
            return True
        else:
            return False

    def textbox_submit_form(self, name, email, cur_addr, perm_addr):
        if self.is_displayed(self.full_name_loc, 30):
            self.send_keys(self.full_name_loc, name)
        if self.is_displayed(self.email_loc, 30):
            self.send_keys(self.email_loc, email)
        if self.is_displayed(self.current_address_loc):
            self.send_keys(self.current_address_loc, cur_addr)
        if self.is_displayed(self.elememts_permanentaddress_loc):
            self.send_keys(self.elememts_permanentaddress_loc, perm_addr)
        if self.is_displayed(self.submit_button_loc, 30):
            self.click(self.submit_button_loc)

    def validate_form_submitted_data(self):
        pass
