from selenium import webdriver
import pytest
from datetime import datetime
import os
import rootpath
import shutil
import json
import sys
from . import config

def pytest_addoption(parser):
    """Pytest function to get command-line arguments."""
    parser.addoption("--baseurl",
                     action="store",
                     default="https://demoqa.com",
                     help="the base URL for the application under test.",
                     )
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     help="the browser to use for testing.",
                     )
    parser.addoption("--browserversion",
                     action="store",
                     default="87.0",
                     help="the browser version to use for testing",
                     )
    parser.addoption("--host",
                     action="store",
                     default="saucelabs",
                     help="where to run your tests: localhost or saucelabs",
                     )
    parser.addoption("--platform",
                     action="store",
                     default="macOS 10.15",
                     help="the operating system to run your tests on (saucelabs only)",
                     )

@pytest.fixture(scope="function")
def driver(request):
    """Fixture to create and destroy the webdriver"""
    # Store command-line arguments or defaults in the global variables in memory (not config.py)
    config.baseurl = request.config.getoption("--baseurl").lower()
    config.browser = request.config.getoption("--browser").lower()
    config.browserversion = request.config.getoption("--browserversion").lower()
    config.host = request.config.getoption("--host").lower()
    config.platform = request.config.getoption("--platform").lower()

    if config.host == "saucelabs":
        dcaps = {}
        dcaps["browserName"] = config.browser
        dcaps["browserVersion"] = config.browserversion
        dcaps["platformName"] = config.platform
        # credentials = os.environ["SAUCE_USERNAME"] + ":" + os.environ["SAUCE_ACCESS_KEY"]
        # credentials = "billchow07" + ":" + "2de31427593c4cb1b4ea3f24e0867849"
        # url = "https://" + credentials + "@ondemand.saucelabs.com/wd/hub"
        url = "https://billchow07:2de31427593c4cb1b4ea3f24e0867849@ondemand.us-west-1.saucelabs.com:443/wd/hub"
        driver = webdriver.Remote(url, dcaps)
        pass
    elif config.host == "localhost":
        if config.browser == "chrome":
            executable_path = os.path.join(rootpath.detect(), "vendor", "chromedriver")
            driver = webdriver.Chrome(executable_path=executable_path,
                                      service_args=["--verbose", "--log-path=/Users/billy/chromedriver.log"])
        elif config.browser == "firefox":
            profile = webdriver.FirefoxProfile()
            # set download location and enable it
            profile.set_preference("browser.download.dir", "/Users/billy/Downloads")
            profile.set_preference("browser.download.folderList", 2)
            # disable system download window using MIME types
            profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "image/jpeg")
            profile.set_preference("browser.download.manager.showWhenStarting", False)
            profile.set_preference("pdfjs.disabled", True)
            # create webdriver instance
            executable_path = os.path.join(rootpath.detect(), "vendor", "geckodriver")
            driver = webdriver.Firefox(firefox_profile=profile,
                                       executable_path=executable_path)
        else:
            # Invalid --browser argument
            sys.exit(1)

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
    """This Pytest hook will create a HTML report"""
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