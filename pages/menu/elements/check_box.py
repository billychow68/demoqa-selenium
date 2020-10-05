from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import pytest
import time


class ElementsCheckBoxArea(BasePage):
    def __init__(self, driver):
        super(ElementsCheckBoxArea, self).__init__(driver)

    checkbox_url = "https://demoqa.com/checkbox"
    plus_toggle_loc = (By.XPATH, '//*/div[@class="check-box-tree-wrapper"]/div/div/button[1]')
    minus_toggle_loc = (By.XPATH, '//*/div[@class="check-box-tree-wrapper"]/div/div/button[2]')
    home_toggle_loc = (By.XPATH, '//*/div[@class="check-box-tree-wrapper"]/div/ol/li/span/button')
    home_checkbox_loc = (By.XPATH, '//*/div[@class="check-box-tree-wrapper"]/div/ol/li/span/label/span')
    selected_text_success = "You have selected"
    home_text_success = "home"
    desktop_text_success = "desktop"
    notes_text_success = "notes"
    commands_text_success = "commands"
    documents_text_success = "documents"
    workspace_text_success = "workspace"
    react_text_success = "react"
    angular_text_success = "angular"
    veu_text_success = "veu"
    office_text_success = "office"
    public_text_success = "public"
    private_text_success = "private"
    classified_text_success = "classified"
    general_text_success = "general"
    downloads_text_success = "downloads"
    wordfile_text_success = "wordFile"
    excelfile_text_success = "excelFile"

    def open_checkbox_page(self):
        self.open_url(self.checkbox_url)

    def validate_page_load(self):
        if self.is_displayed(self.home_toggle_loc, 2) and \
           self.is_displayed(self.home_checkbox_loc, 2):
            return True
        else:
            return False

    def toggle_plus(self):
        self.click(self.plus_toggle_loc)

    def toggle_minus(self):
        self.click(self.minus_toggle_loc)

    def toggle_home_arrow(self):
        self.click(self.home_toggle_loc)

    def select_home_checkbox(self):
        self.click(self.home_checkbox_loc)

    def validate_select_all_checkboxes(self):
        if self.validate_select_all_desktop_checkboxes() and \
           self.validate_select_all_documents_checkboxes() and \
           self.validate_select_all_documents_checkboxes():
            return True
        else:
            return False

    def validate_select_all_desktop_checkboxes(self):
        if self.desktop_text_success in self.driver.page_source and \
           self.notes_text_success in self.driver.page_source and \
           self.commands_text_success in self.driver.page_source:
            return True
        else:
            return False

    def validate_select_all_documents_checkboxes(self):
        if self.validate_select_all_workspace_checkboxes() and \
           self.validate_select_all_office_checkboxes():
            return True
        else:
            return False

    def validate_select_all_workspace_checkboxes(self):
        if self.react_text_success in self.driver.page_source and \
           self.angular_text_success in self.driver.page_source and \
           self.veu_text_success in self.driver.page_source:
            return True
        else:
            return False

    def validate_select_all_office_checkboxes(self):
        if self.public_text_success in self.driver.page_source and \
           self.private_text_success in self.driver.page_source and \
           self.classified_text_success in self.driver.page_source and \
           self.general_text_success in self.driver.page_source:
            return True
        else:
            return False

    def validate_select_all_downloads_checkboxes(self):
        if self.downloads_text_success in self.driver.page_source and \
           self.wordfile_text_success in self.driver.page_source and \
           self.excelfile_text_success in self.driver.page_source:
            return True
        else:
            return False
