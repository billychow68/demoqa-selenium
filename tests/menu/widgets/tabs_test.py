from pages.menu.widgets.tabs import ElementsTabsArea
import pytest
import time


class TestTabsArea:

    def test_page_load(self, driver):
        tabs = ElementsTabsArea(driver)
        tabs.open_tabs_page()
        assert tabs.validate_page_load()

    def test_what_tab(self, driver):
        tabs = ElementsTabsArea(driver)
        tabs.open_tabs_page()
        tabs.select_what_tab()
        assert tabs.validate_what_tab()

    def test_origin_tab(self, driver):
        tabs = ElementsTabsArea(driver)
        tabs.open_tabs_page()
        tabs.select_origin_tab()
        assert tabs.validate_origin_tab()

    def test_use_tab(self, driver):
        tabs = ElementsTabsArea(driver)
        tabs.open_tabs_page()
        tabs.select_use_tab()
        assert tabs.validate_use_tab()
