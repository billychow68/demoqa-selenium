from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests import config


class ElementsAlertsArea(BasePage):

    alerts_path = "/alerts"
    alert_button_loc = (By.ID, 'alertButton')
    timer_alert_button_loc = (By.ID, 'timerAlertButton')
    confirm_button_loc = (By.ID, 'confirmButton')
    prompt_button_loc = (By.ID, 'promtButton')

    def __init__(self, driver):
        super(ElementsAlertsArea, self).__init__(driver)

    def open_alerts_page(self):
        self.driver.get(config.baseurl + self.alerts_path)

    def validate_page_load(self):
        return (self.is_displayed(self.alert_button_loc, timeout=15)) and \
               (self.is_displayed(self.timer_alert_button_loc, timeout=15)) and \
               (self.is_displayed(self.confirm_button_loc, timeout=15)) and \
               (self.is_displayed(self.prompt_button_loc, timeout=15))

    def select_alerts_button(self):
        if self.is_displayed(self.alert_button_loc, timeout=15):
            self.click(self.alert_button_loc)

    def validate_alerts_button_text(self):
        if self.is_alert_present(15) and \
           'You clicked a button' == self.get_alert_text():
                return True
        return False

    def validate_alerts_button_close(self):
        if not self.is_alert_present(1):
            return True
        return False

    def select_timer_alerts_button(self):
        if self.is_displayed(self.timer_alert_button_loc, timeout=15):
            self.click(self.timer_alert_button_loc)

    def validate_timer_alerts_button_text(self):
        if self.is_alert_present(timeout=15) and \
           'This alert appeared after 5 seconds' == self.get_alert_text():
                return True
        return False
    
    def select_confirm_button(self):
        if self.is_displayed(self.confirm_button_loc, timeout=15):
            self.click(self.confirm_button_loc)

    def validate_confirm_button_text(self):
        if self.is_alert_present(timeout=15) and \
           'Do you confirm action?' == self.get_alert_text():
                return True
        return False

    def validate_confirm_button_close_accept(self):
        if (not self.is_alert_present(1)) and ('You selected Ok' in self.driver.page_source):
            return True
        return False

    def validate_confirm_button_close_dismiss(self):
        if (not self.is_alert_present(1)) and ('You selected Cancel' in self.driver.page_source):
            return True
        return False

    def select_prompt_button(self):
        if self.is_displayed(self.prompt_button_loc, timeout=15):
            self.click(self.prompt_button_loc)

    def validate_prompt_button_text(self):
        if self.is_alert_present(15) and \
           'Please enter your name' == self.get_alert_text():
                return True
        return False

    def validate_prompt_button_close_accept(self):
        if (not self.is_alert_present(1)) and ('You entered Billy' in self.driver.page_source):
            return True
        return False

