import os
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager



# Fixture to set up browser
@pytest.fixture()
def setup(browser):
    global driver
    if browser == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        print("Launching Chrome browser...")
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        print("Launching Firefox browser...")
    elif browser == 'edge':
        driver = webdriver.Edge(service=EdgeService(EdgeDriverManager().install()))
        print("Launching Edge browser...")

    yield driver
    driver.quit()


# Command-line option to specify the browser
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")


# Fixture to access the browser option
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# Customize the HTML report title
def pytest_html_report_title(report):
    report.title = "SauceDemo E-Commerce Automation Report"


# Add custom environment information in the HTML report
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([f"Project Name: SauceDemo E-Commerce Automation",
                   f"Module Name: Login, Product Search, Cart",
                   f"Tester: srinivas"])


# Take screenshots for failed or skipped tests
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    pytest_html = item.config.pluginmanager.getplugin('html')

    if report.when == "call" or report.when == "setup":
        if report.failed:
            try:
                file_name = datetime.now().strftime('%Y%m%d_%H%M%S') + ".png"
                screenshot_path = os.path.join(os.getcwd(), "Screenshots", file_name)
                driver = item.funcargs['setup']
                driver.get_screenshot_as_file(screenshot_path)
                extra = pytest_html.extras.image(screenshot_path)
                report.extra = getattr(report, 'extra', []) + [extra]
            except NoSuchWindowException:
                print("Window is closed or web view not found. Cannot capture screenshot.")
