"""This module tests the practice form page"""
from pages.menu.forms.practice_form import FormsPracticeFormArea


class TestPracticeFormArea:
    """This class contains the test cases for the practice form page"""

    def test_page_load(self, driver):
        """This method validates the practice page load"""
        forms_practice_area = FormsPracticeFormArea(driver)
        forms_practice_area.open_practice_form_url()
        # assert forms_practice_area.validate_page_load()
        assert False

