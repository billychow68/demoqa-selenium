"""This module tests the home page"""
import pytest
from pages.home_page import HomePage


class TestHomePage:

    def test_page_load(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.validate_page_load()

    def test_select_elements(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.select_elements_option()
        home_page.validate_elements_page()

    def test_select_forms(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.select_forms_option()
        home_page.validate_forms_page()

    def test_select_alerts_frames_windows(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.select_alert_frames_windows_option()
        # todo: assert

    def test_select_widgets(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.select_widgets_option()
        # todo: assert

    def test_interactions_option(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.select_interactions_option()
        # todo: assert
