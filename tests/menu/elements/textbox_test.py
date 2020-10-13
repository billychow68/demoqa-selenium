from pages.menu.nav_bar import MenuNavBar
from pages.menu.elements.textbox import ElementsTextboxArea
import pytest
import time


class TestElementsTextboxArea:

    def test_page_load(self, driver):
        textbox_area = ElementsTextboxArea(driver)
        textbox_area.open_textbox_page()
        assert textbox_area.validate_page_load()
