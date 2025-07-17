import pytest
from selenium import webdriver
import os
from datetime import datetime

# Create 'screenshots' folder if not exist
SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), '..', 'screenshots')
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def pytest_html_report_title(report):
    report.title = "KefiLynks Automation Report"

@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)

    # Attach the driver to the request node for access in hooks
    request.node.driver = driver

    yield driver
    driver.quit()

# Hook for adding screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    # Only take screenshot on test failure
    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)
        if driver:
            # Generate filename
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            filename = f"{item.name}_{timestamp}.png"
            filepath = os.path.join(SCREENSHOT_DIR, filename)

            # Take screenshot
            driver.save_screenshot(filepath)

            # Attach to report.html
            if filepath:
                extra = getattr(report, 'extra', [])
                html = f'<div><img src="../screenshots/{filename}" alt="screenshot" style="width:600px;height:auto;" ' \
                       f'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))
                report.extra = extra

# Required for `pytest_html.extras`
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin('html')