from pages.menu.elements.upload_download import ElementsUploadDownloadArea
import pytest
import time


class TestUploadDownloadArea:

    def test_page_load(self, driver):
        upload_download_area = ElementsUploadDownloadArea(driver)
        upload_download_area.open_upload_download_page()
        assert upload_download_area.validate_page_load()

    def test_download_button(self, driver, json_loader):
        upload_download_area = ElementsUploadDownloadArea(driver)
        upload_download_area.open_upload_download_page()
        upload_download_area.select_download(json_loader)
        assert upload_download_area.validate_download(json_loader)

    def test_upload_button(self, driver, json_loader):
        upload_download_area = ElementsUploadDownloadArea(driver)
        upload_download_area.open_upload_download_page()
        upload_download_area.select_upload()
        assert upload_download_area.validate_upload()
