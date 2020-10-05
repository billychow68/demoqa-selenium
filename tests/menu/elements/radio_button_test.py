from demoqa.pages.menu.nav_bar import MenuNavBar
from demoqa.pages.menu.elements.radio_button import ElementsRadioButtonArea
import pytest
import time


class TestElementsRadioButtonArea:

    def test_page_load(self, homepage):
        radio_button_area = ElementsRadioButtonArea(homepage.get_driver())
        radio_button_area.open_radiobutton_page()
        assert radio_button_area.validate_page_load()

    def test_select_yes(self, homepage):
        radio_button_area = ElementsRadioButtonArea(homepage.get_driver())
        radio_button_area.open_radiobutton_page()
        radio_button_area.select_yes()
        assert radio_button_area.validate_select_yes_success()

    def test_select_impressive(self, homepage):
        radio_button_area = ElementsRadioButtonArea(homepage.get_driver())
        radio_button_area.open_radiobutton_page()
        radio_button_area.select_impressive()
        assert radio_button_area.validate_select_impressive_success()

    def test_no_is_disabled(self, homepage):
        radio_button_area = ElementsRadioButtonArea(homepage.get_driver())
        radio_button_area.open_radiobutton_page()
        assert not radio_button_area.validate_no_is_disabled()
