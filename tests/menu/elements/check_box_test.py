from pages.menu.nav_bar import MenuNavBar
from pages.menu.elements.check_box import ElementsCheckBoxArea
import pytest
import time


class TestElementCheckBoxArea:

    def test_page_load(self, driver):
        check_box_area = ElementsCheckBoxArea(driver)
        check_box_area.open_checkbox_page()
        check_box_area.validate_page_load()

    def test_select_all_checkboxes(self, driver):
        check_box_area = ElementsCheckBoxArea(driver)
        check_box_area.open_checkbox_page()
        check_box_area.select_home_checkbox()
        check_box_area.toggle_home_arrow()
        check_box_area.validate_select_all_checkboxes()

    def test_expand_collapse_checkbox_tree(self, driver):
        check_box_area = ElementsCheckBoxArea(driver)
        check_box_area.open_checkbox_page()
        check_box_area.toggle_plus()
        check_box_area.toggle_minus()
        # todo: assert
