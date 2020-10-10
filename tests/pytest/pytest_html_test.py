"""This module contains miscellaneious pytest related tests."""
from pages.menu.forms.practice_form import FormsPracticeFormArea
import pytest


class TestPytestHTML:

    @pytest.mark.xfail(reason="xfail test")
    def test_pytest_runtest_makereport_hook_on_xfail(self, homepage):
        homepage.open_home_page()
        assert False

    @pytest.mark.xfail(reason="xpass test")
    def test_pytest_runtest_makereport_hook_on_xpass(self, homepage):
        homepage.open_home_page()

    def test_pytest_runtest_makereport_hook_on_fail(self, homepage):
        """This method tests the screenshot feature"""
        forms_practice_area = FormsPracticeFormArea(homepage.get_driver())
        forms_practice_area.open_practice_form_url()
        assert False
