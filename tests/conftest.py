from selenium import webdriver
from pages.home_page import HomePage
import pytest
from datetime import datetime
import sys
import os
import rootpath
import shutil
import json


@pytest.fixture(scope="function")
def driver(request):
    """Fixture to create and destroy the webdriver"""
    driver = webdriver.Chrome()
    # self.driver.implicitly_wait(10)
    driver.maximize_window()

    def close():
        # driver.delete_all_cookies()
        driver.quit()

    request.addfinalizer(close)
    return driver

def pytest_sessionstart(session):
    path = os.path.join(rootpath.detect(), "reports")
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

def pytest_sessionfinish(session, exitstatus):
    pass

@pytest.fixture
def json_loader():
    """Loads data from JSON file"""
    def _loader(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        return data
    return _loader

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """This hook will create a HTML report"""
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            driver = item.funcargs['request'].getfixturevalue('driver')
            timestamp = datetime.now().strftime('%H-%M-%S.%f')[:-3]
            path = os.path.join(rootpath.detect(), "reports", "screenshot_" + timestamp + ".png")
            driver.save_screenshot(path)
            extra.append(pytest_html.extras.image(path))
        report.extra = extra
    pass