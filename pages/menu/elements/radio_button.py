from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class ElementsRadioButtonArea(BasePage):

    def __init__(self, driver):
        super(ElementsRadioButtonArea, self).__init__(driver)

    radiobutton_path = "/radio-button"
    question_loc = (By.CLASS_NAME, "mb-3")
    yes_label_loc = (By.XPATH, '//*/div[@class="col-12 mt-4 col-md-6"]/div[1]/div[2]/label')
    yes_loc = (By.XPATH, '//*/input[@id="yesRadio"]')
    impressive_label_loc = (By.XPATH, '//*/div[@class="col-12 mt-4 col-md-6"]/div[1]/div[3]/label')
    impressive_loc = (By.CSS_SELECTOR, '#impressiveRadio')
    no_label_loc = (By.XPATH, '//*/div[@class="col-12 mt-4 col-md-6"]/div[1]/div[4]/label')
    no_loc = (By.ID, 'noRadio')
    confirmation_text = 'You have selected '

    def open_radiobutton_page(self):
        self.open_url(self.radiobutton_path)

    def validate_page_load(self):
        # todo: investigate why yes_loc, impressive_loc and no_loc aren't locatable
        # if self.is_displayed(self.yes_loc, timeout=15):
        assert self.is_displayed(self.question_loc, timeout=15) and \
           self.is_displayed(self.yes_label_loc, timeout=15) and \
           self.is_displayed(self.impressive_label_loc, timeout=15) and \
           self.is_displayed(self.no_label_loc, timeout=15)

    def select_yes(self):
        if self.is_displayed(self.yes_label_loc, timeout=15):
            self.click(self.yes_label_loc)

    def select_impressive(self):
        if self.is_displayed(self.impressive_label_loc, timeout=15):
            self.click(self.impressive_label_loc)

    def validate_select_yes_success(self):
        assert self.confirmation_text in self.driver.page_source and \
           "Yes" in self.driver.page_source and \
           self.is_selected(self.yes_loc)

    def validate_select_impressive_success(self):
        assert self.confirmation_text in self.driver.page_source and \
           "Impressive" in self.driver.page_source and \
           self.is_selected(self.impressive_loc)

    def validate_no_is_disabled(self):
        assert not self.is_enabled(self.no_loc)
