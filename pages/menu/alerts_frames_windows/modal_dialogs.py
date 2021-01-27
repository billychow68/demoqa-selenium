from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests import config


class ElementsModalDialogsArea(BasePage):

    modals_path = "/modal-dialogs"
    small_modal_loc = (By.CSS_SELECTOR, '#showSmallModal')
    small_modal_close_loc = (By.CSS_SELECTOR, '#closeSmallModal')
    small_modal_x_close_loc = (By.CSS_SELECTOR, '.close')
    small_modal_body_loc = (By.CSS_SELECTOR, '.modal-body')
    large_modal_loc = (By.CSS_SELECTOR, '#showLargeModal')
    large_modal_close_loc = (By.CSS_SELECTOR, '#closeLargeModal')
    large_modal_close_x_loc = (By.CLASS_NAME, "close")
    large_modal_body_loc = (By.XPATH, "//*/div[@class='modal-dialog modal-lg']/div/div/p")
    large_modal_text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'

    def __init__(self, driver):
        super(ElementsModalDialogsArea, self).__init__(driver)

    def open_modals_page(self):
        self.driver.get(config.baseurl + self.modals_path)

    def validate_page_load(self):
        return (self.is_displayed(self.small_modal_loc, timeout=15)) and \
               (self.is_displayed(self.large_modal_loc, timeout=15))

    def select_small_modal(self):
        if self.is_displayed(self.small_modal_loc, timeout=15):
            self.click(self.small_modal_loc)

    def close_small_modal_dialog(self):
        self.close_modal_dialog(self.small_modal_close_loc)

    def close_x_small_modal_dialog(self):
        self.close_modal_dialog(self.small_modal_x_close_loc)

    def validate_small_modal(self):
        text = self.get_modal_dialog_text(self.small_modal_body_loc)
        if 'This is a small modal. It has very less content' == text:
            return True
        return False

    def select_large_modal(self):
        if self.is_displayed(self.large_modal_loc, timeout=15):
            self.click(self.large_modal_loc)

    def close_large_modal_dialog(self):
        self.close_modal_dialog(self.large_modal_close_loc)

    def close_x_large_modal_dialog(self):
        self.close_modal_dialog(self.large_modal_close_x_loc)

    def validate_large_modal(self):
        text = self.get_modal_dialog_text(self.large_modal_body_loc)
        if self.large_modal_text == text:
            return True
        return False

