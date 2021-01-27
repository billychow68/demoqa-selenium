import os
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    homepage_path = "/"
    logo_loc = (By.XPATH, "//*/div[@id='app']/header/a")
    elements_loc = (By.XPATH, "//*/div[@class='card mt-4 top-card'][1]/div/div[@class='card-body']/h5")
    forms_loc = (By.XPATH, "//*/div[@class='card mt-4 top-card'][2]/div/div[@class='card-body']/h5")
    alerts_frames_windows_loc = (By.XPATH, "//*/div[@class='card mt-4 top-card'][3]/div/div[@class='card-body']/h5")
    widgets_loc = (By.XPATH, "//*/div[@class='card mt-4 top-card'][4]/div/div[@class='card-body']/h5")
    interactions_loc = (By.XPATH, "//*/div[@class='card mt-4 top-card'][5]/div/div[@class='card-body']/h5")

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def open_home_page(self):
        self.open_url(self.homepage_path)

    def select_elements_option(self):
        if self.is_displayed(self.elements_loc, timeout=15):
            self.find_element(self.elements_loc).click()

    def select_forms_option(self):
        if self.is_displayed(self.forms_loc, timeout=15):
            self.find_element(self.forms_loc).click()

    def select_alert_frames_windows_option(self):
        if self.is_displayed(self.alerts_frames_windows_loc, timeout=15):
            self.find_element(self.alerts_frames_windows_loc).click()

    def select_widgets_option(self):
        if self.is_displayed(self.widgets_loc, timeout=15):
            self.find_element(self.widgets_loc).click()

    def select_interactions_option(self):
        if self.is_displayed(self.interactions_loc, timeout=15):
            self.find_element(self.interactions_loc).click()

    def validate_page_load(self):
        if '<img class="banner-image" src="/images/WB.svg"' in self.driver.page_source:
            return True
        else:
            return False

    def validate_elements_page(self):
        if '<div class="main-header">Elements</div>' in self.driver.page_source:
            return True
        else:
            return False

    def validate_forms_page(self):
        if '<div class="main-header">Forms</div>' in self.driver.page_source:
            return True
        else:
            return False
