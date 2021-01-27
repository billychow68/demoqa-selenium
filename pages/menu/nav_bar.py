from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MenuNavBar(BasePage):

    def __init__(self, driver):
        super(MenuNavBar, self).__init__(driver)

    def validate_page_load(self):
        pass

    #
    # Elements menu
    #
    elements_menu_toggle_loc = (By.XPATH, '//*/div[@class="left-pannel"]/div//div[1]/div')
    elements_menu_textbox_loc = (By.XPATH, '//*/div[@class="left-pannel"]/div//div[1]/div/ul/li[1]')
    elements_menu_checkbox_loc = (By.XPATH, '//*/div[@class="left-pannel"]/div//div[1]/div/ul/li[2]')
    elements_menu_radiobutton_loc = (By.XPATH, '//*/div[@class="left-pannel"]/div//div[1]/div/ul/li[3]')
    elements_menu_web_tables_loc = (By.XPATH, '//*/div[@class="left-pannel"]/div//div[1]/div/ul/li[4]')
    elements_menu_buttons_loc = (By.XPATH, '//*/div[@class="left-pannel"]/div//div[1]/div/ul/li[5]')
    elements_menu_links_loc = (By.XPATH, '//*/div[@class="left-pannel"]/div//div[1]/div/ul/li[6]')
    elements_menu_broken_links_images_loc = (By.XPATH, '//*/div[@class="left-pannel"]/div//div[1]/div/ul/li[7]')
    elements_menu_upload_download_loc = (By.XPATH, '//*/div[@class="left-pannel"]/div//div[1]/div/ul/li[8]')
    elements_menu_dynamic_properties_loc = (By.XPATH, '//*/div[@class="left-pannel"]/div//div[1]/div/ul/li[9]')

    def toggle_elements_menu(self):
        if self.is_displayed(self.elements_menu_toggle_loc, timeout=15):
            self.click(self.elements_menu_toggle_loc)

    def select_elements_textbox_menu_item(self):
        if self.is_displayed(self.elements_menu_textbox_loc, timeout=15):
            self.click(self.elements_menu_textbox_loc)

    def select_elements_checkbox_menu_item(self):
        if self.is_displayed(self.elements_menu_checkbox_loc, timeout=15):
            self.click(self.elements_menu_checkbox_loc)

    def select_elements_radiobutton_menu_item(self):
        if self.is_displayed(self.elements_menu_radiobutton_loc, timeout=15):
            self.click(self.elements_menu_radiobutton_loc)

    def select_elements_webtables_menu_item(self):
        if self.is_displayed(self.elements_menu_web_tables_loc, timeout=15):
            self.click(self.elements_menu_web_tables_loc)

    def select_elements_buttons_menu_item(self):
        if self.is_displayed(self.elements_menu_buttons_loc, timeout=15):
            self.click(self.elements_menu_buttons_loc)

    def select_elements_links_menu_item(self):
        if self.is_displayed(self.elements_menu_links_loc, timeout=15):
            self.click(self.elements_menu_links_loc)

    def select_elements_broken_links_images_menu_item(self):
        if self.is_displayed(self.elements_menu_broken_links_images_loc, timeout=15):
            self.click(self.elements_menu_broken_links_images_loc)

    def select_elements_upload_download_menu_item(self):
        if self.is_displayed(self.elements_menu_upload_download_loc, timeout=15):
            self.click(self.elements_menu_upload_download_loc)

    def select_elements_dynamic_properties_menu_item(self):
        if self.is_displayed(self.elements_menu_dynamic_properties_loc, timeout=15):
            self.click(self.elements_menu_dynamic_properties_loc)

    #
    # Forms menu
    #
    forms_menu_toggle_loc = (By.XPATH, "//*/div[@class='left-pannel']/div/div[2]/div")
    forms_menu_practice_form_loc = (By.XPATH, "//*/div[@class='left-pannel']/div/div[2]/div/ul/li[1]")

    def toggle_forms_menu(self):
        if self.is_displayed(self.forms_menu_toggle_loc, timeout=15):
            self.click(self.forms_menu_toggle_loc)

    def select_forms_practice_form_menu_item(self):
        if self.is_displayed(self.forms_menu_practice_form_loc, timeout=15):
            self.click(self.forms_menu_practice_form_loc)

    # def validate_elements_page(self):
    #     if '<div class="main-header">Elements</div>' in self._driver.page_source:
    #         return True
    #     else:
    #         return False
    #
    # def validate_forms_page(self):
    #     if '<div class="main-header">Forms</div>' in self._driver.page_source:
    #         return True
    #     else:
    #         return False
