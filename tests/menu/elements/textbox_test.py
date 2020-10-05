from demoqa.pages.menu.nav_bar import MenuNavBar
from demoqa.pages.menu.elements.textbox import ElementsTextboxArea
import pytest
import time


class TestElementsTextboxArea:

    def test_page_load(self, homepage):
        textbox_area = ElementsTextboxArea(homepage.get_driver())
        textbox_area.open_textbox_page()
        assert textbox_area.validate_page_load()
