"""This module contains miscellaneious pytest related tests."""
from pages.menu.forms.practice_form import FormsPracticeFormArea
from pages.home_page import HomePage
import pytest


class TestPytestHTML:

    @pytest.mark.xfail(reason="xfail test")
    def test_pytest_runtest_makereport_hook_on_xfail(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        assert False

    @pytest.mark.xfail(reason="xpass test")
    def test_pytest_runtest_makereport_hook_on_xpass(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()

    def test_pytest_runtest_makereport_hook_on_fail(self, driver):
        """This method tests the screenshot feature"""
        forms_practice_area = FormsPracticeFormArea(driver)
        forms_practice_area.open_practice_form_url()
        assert False
