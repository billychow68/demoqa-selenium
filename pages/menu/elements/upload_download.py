from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import os
import rootpath
import time


class ElementsUploadDownloadArea(BasePage):

    upload_download_path = "/upload-download"
    download_button_loc = (By.CSS_SELECTOR, '#downloadButton')
    upload_button_loc = (By.ID, 'uploadFile')
    upload_file_path_loc = (By.ID, 'uploadedFilePath')

    def __init__(self, driver):
        super(ElementsUploadDownloadArea, self).__init__(driver)

    def _delete_sample_file(self, json_loader):
        path = os.path.join(rootpath.detect(), "tests", "menu", "elements", "config.json")
        config = json_loader(path)
        full_path = os.path.join(config["path"], config["file"])
        if os.path.exists(full_path):
            os.remove(full_path)

    def open_upload_download_page(self):
        self.open_url(self.upload_download_path)

    def validate_page_load(self):
        assert self.is_displayed(self.download_button_loc, timeout=15) and \
            self.is_displayed(self.upload_button_loc, timeout=15)

    def select_download(self, json_loader):
        self._delete_sample_file(json_loader)
        if self.is_displayed(self.download_button_loc, timeout=15):
            self.find_element(self.download_button_loc).click()

    def validate_download(self, json_loader):
        path = os.path.join(rootpath.detect(), "tests", "menu", "elements", "config.json")
        config = json_loader(path)
        full_path = os.path.join(config["path"], config["file"])
        assert self.is_file_exists(full_path, timeout=15)
        self._delete_sample_file(json_loader)

    def select_upload(self):
        full_path = os.path.join(rootpath.detect(), "tests", "menu", "elements", "sampleFile.jpeg")
        self.find_element(self.upload_button_loc).send_keys(full_path)

    def validate_upload(self):
        assert self.is_text_displayed(self.upload_file_path_loc, "C:\\fakepath\sampleFile.jpeg", timeout=15)





