from pages.menu.nav_bar import MenuNavBar
from pages.menu.forms.practice_form import FormsPracticeFormArea
import pytest
import time


class TestPracticeFormArea:

    def test_page_load(self, homepage):
        homepage.open_home_page()
        homepage.select_forms_option()
        menu_nav_bar = MenuNavBar(homepage.get_driver())
        menu_nav_bar.select_forms_practice_form_menu_item()
        forms_practice_area = FormsPracticeFormArea(homepage.get_driver())
        assert forms_practice_area.validate_page_load()
