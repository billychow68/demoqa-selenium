from pages.menu.alerts_frames_windows.browser_windows import ElementsBrowserWindowsArea
import pytest
import time


class TestBrowserWindowWindowsArea:

    def test_page_load(self, driver):
        bw = ElementsBrowserWindowsArea(driver)
        bw.open_browser_window_page()
        bw.validate_page_load()

    def test_new_tab(self, driver):
        bw = ElementsBrowserWindowsArea(driver)
        bw.open_browser_window_page()
        bw.select_tab_button()
        bw.validate_tab_button()
        bw.close()

    @pytest.mark.xfail(reason="Sauce Labs bug: Contents of new window is incorrect.")
    def test_new_window(self, driver):
        bw = ElementsBrowserWindowsArea(driver)
        bw.open_browser_window_page()
        bw.select_new_window_button()
        # note: same validation as tab button
        bw.validate_tab_button()
        bw.close()

    @pytest.mark.xfail(reason="Selenium hangs on validation (possible bug).")
    def test_new_window_message(self, driver):
        bw = ElementsBrowserWindowsArea(driver)
        bw.open_browser_window_page()
        bw.select_new_window_message()
        assert False
        # assert bw.validate_new_window_message()
        bw.close()

