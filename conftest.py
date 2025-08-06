# conftest.py - Configuration for pytest with Selenium WebDriver and HTML reporting
import pytest
from selenium import webdriver
import os
from datetime import datetime

# URL and credentials for the KefiLynks application
BaseUrl = "https://kefitechlynks.com/"
username = "shithin.kokkarni@kefitech.com"
password = "DUlKKyKV"

# Create 'screenshots' folder if not exist
SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), '..', 'screenshots')
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def pytest_html_report_title(report):
    report.title = "KefiLynks Automation Report"

@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BaseUrl)
    driver.implicitly_wait(3)

    # Attach the driver to the request node for access in hooks
    request.node.driver = driver

    yield driver
    driver.quit()

# For attaching html plugin instance
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin('html')

# Screenshot on failure + Docstring as Extra info
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        extra = getattr(report, 'extra', [])

        #  Attach docstring as test description
        docstring = item.function.__doc__
        if docstring:
            description = docstring.strip()
            extra.append(pytest_html.extras.text(description, name="Test Description"))

        #  Take screenshot on failure
        if report.failed:
            driver = getattr(item, "driver", None)
            if driver:
                timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                filename = f"{item.name}_{timestamp}.png"
                filepath = os.path.join(SCREENSHOT_DIR, filename)
                driver.save_screenshot(filepath)

                html = f'<div><img src="../screenshots/{filename}" alt="screenshot" style="width:600px;height:auto;" ' \
                       f'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))

        report.extra = extra
