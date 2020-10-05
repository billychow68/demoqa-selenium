from demoqa.pages.menu.nav_bar import MenuNavBar
from demoqa.pages.menu.elements.buttons import ElementsButtonsArea
import pytest
import time


class TestElementsButtonsArea:

    def test_page_load(self, homepage):
        buttons_area = ElementsButtonsArea(homepage.get_driver())
        buttons_area.open_buttons_page()
        assert buttons_area.validate_page_load()

    def test_doubleclick(self, homepage):
        buttons_area = ElementsButtonsArea(homepage.get_driver())
        buttons_area.open_buttons_page()
        buttons_area.select_doubleclick_button()
        assert buttons_area.validate_doubleclick()

    def test_rightclick(self, homepage):
        buttons_area = ElementsButtonsArea(homepage.get_driver())
        buttons_area.open_buttons_page()
        buttons_area.select_rightclick_button()
        assert buttons_area.validate_rightclick()

    def test_dynamicclick(self, homepage):
        pass
