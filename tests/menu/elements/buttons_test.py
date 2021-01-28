from pages.menu.nav_bar import MenuNavBar
from pages.menu.elements.buttons import ElementsButtonsArea
import pytest
import time


class TestElementsButtonsArea:

    def test_page_load(self, driver):
        buttons_area = ElementsButtonsArea(driver)
        buttons_area.open_buttons_page()
        buttons_area.validate_page_load()

    def test_doubleclick(self, driver):
        buttons_area = ElementsButtonsArea(driver)
        buttons_area.open_buttons_page()
        buttons_area.select_doubleclick_button()
        buttons_area.validate_doubleclick()

    def test_rightclick(self, driver):
        buttons_area = ElementsButtonsArea(driver)
        buttons_area.open_buttons_page()
        buttons_area.select_rightclick_button()
        buttons_area.validate_rightclick()

    def test_dynamicclick(self, driver):
        pass
