from pages.menu.alerts_frames_windows.modal_dialogs import ElementsModalDialogsArea
import pytest
import time


class TestModalDialogsArea:

    def test_page_load(self, driver):
        modal = ElementsModalDialogsArea(driver)
        modal.open_modals_page()
        assert modal.validate_page_load()

    def test_small_modal_with_close(self, driver):
        modal = ElementsModalDialogsArea(driver)
        modal.open_modals_page()
        modal.select_small_modal()
        assert modal.validate_small_modal()
        modal.close_small_modal_dialog()

    def test_small_modal_with_close_x(self, driver):
        modal = ElementsModalDialogsArea(driver)
        modal.open_modals_page()
        modal.select_small_modal()
        assert modal.validate_small_modal()
        modal.close_x_small_modal_dialog()

    def test_large_modal_with_close(self, driver):
        modal = ElementsModalDialogsArea(driver)
        modal.open_modals_page()
        modal.select_large_modal()
        assert modal.validate_large_modal()
        modal.close_large_modal_dialog()

    def test_large_modal_with_close_x(self, driver):
        modal = ElementsModalDialogsArea(driver)
        modal.open_modals_page()
        modal.select_large_modal()
        assert modal.validate_large_modal()
        modal.close_x_large_modal_dialog()