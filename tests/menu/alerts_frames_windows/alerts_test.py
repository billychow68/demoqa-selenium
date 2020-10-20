from pages.menu.alerts_frames_windows.alerts import ElementsAlertsArea
import pytest
import time


class TestAlertsArea:

    def test_page_load(self, driver):
        aa = ElementsAlertsArea(driver)
        aa.open_alerts_page()
        assert aa.validate_page_load()

    def test_alerts_button(self, driver):
        aa = ElementsAlertsArea(driver)
        aa.open_alerts_page()
        aa.select_alerts_button()
        assert aa.validate_alerts_button_text()
        aa.accept_alert()
        assert aa.validate_alerts_button_close()

    def test_timer_alerts_button(self, driver):
        aa = ElementsAlertsArea(driver)
        aa.open_alerts_page()
        aa.select_timer_alerts_button()
        assert aa.validate_timer_alerts_button_text()
        aa.accept_alert()
        assert aa.validate_alerts_button_close()

    def test_confirm_button_accept(self, driver):
        aa = ElementsAlertsArea(driver)
        aa.open_alerts_page()
        aa.select_confirm_button()
        assert aa.validate_confirm_button_text()
        aa.accept_alert()
        assert aa.validate_confirm_button_close_accept()

    def test_confirm_button_dismiss(self, driver):
        aa = ElementsAlertsArea(driver)
        aa.open_alerts_page()
        aa.select_confirm_button()
        assert aa.validate_confirm_button_text()
        aa.dismiss_alert()
        assert aa.validate_confirm_button_close_dismiss()

    def test_prompt_button_accept(self, driver):
        aa = ElementsAlertsArea(driver)
        aa.open_alerts_page()
        aa.select_prompt_button()
        assert aa.validate_prompt_button_text()
        aa.alert_send_keys("Billy")
        aa.accept_alert()
        assert aa.validate_prompt_button_close_accept()
