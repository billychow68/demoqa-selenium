import pytest
import time

class TestHomePage:

    def teardown(self):
        time.sleep(2)

    def test_page_load(self, homepage):
        homepage.open_home_page()
        assert homepage.validate_page_load()

    def test_select_elements(self, homepage):
        homepage.open_home_page()
        homepage.select_elements_option()
        assert homepage.validate_elements_page()

    def test_select_forms(self, homepage):
        homepage.open_home_page()
        homepage.select_forms_option()
        assert homepage.validate_forms_page()

    def test_select_alerts_frames_windows(self, homepage):
        homepage.open_home_page()
        homepage.select_alert_frames_windows_option()
        # todo: assert

    def test_select_widgets(self, homepage):
        homepage.open_home_page()
        homepage.select_widgets_option()
        # todo: assert

    def test_interactions_option(self, homepage):
        homepage.open_home_page()
        homepage.select_interactions_option()
        # todo: assert