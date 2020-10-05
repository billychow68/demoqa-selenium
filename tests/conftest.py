import pytest
from selenium import webdriver
from pages.home_page import HomePage
import time

@pytest.fixture(scope="function")
def homepage(request):
    driver = webdriver.Chrome()
    # self.driver.implicitly_wait(10)
    #driver.maximize_window()
    #driver.get("http://demoqa.com")

    def close():
        driver.delete_all_cookies()
        driver.quit()

    request.addfinalizer(close)
    return HomePage(driver)

# @pytest.fixture(scope="function")
# def delay():
#     yield
#     time.sleep(5)