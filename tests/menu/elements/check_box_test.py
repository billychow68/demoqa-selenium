from pages.menu.nav_bar import MenuNavBar
from pages.menu.elements.check_box import ElementsCheckBoxArea
import pytest
import time


class TestElementCheckBoxArea:

    def test_page_load(self, homepage):
        check_box_area = ElementsCheckBoxArea(homepage.get_driver())
        check_box_area.open_checkbox_page()
        assert check_box_area.validate_page_load()

    def test_select_all_checkboxes(self, homepage):
        check_box_area = ElementsCheckBoxArea(homepage.get_driver())
        check_box_area.open_checkbox_page()
        check_box_area.select_home_checkbox()
        check_box_area.toggle_home_arrow()
        assert check_box_area.validate_select_all_checkboxes()

    def test_expand_collapse_checkbox_tree(self, homepage):
        check_box_area = ElementsCheckBoxArea(homepage.get_driver())
        check_box_area.open_checkbox_page()
        check_box_area.toggle_plus()
        check_box_area.toggle_minus()
        # todo: assert
