import pytest
from selenium import webdriver
import os
import base64  # Import base64 for encoding
from pytest_html import extras # Import extras for direct image embedding

def pytest_html_report_title(report):
    report.title = "KefiLynks Automation Report"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook for taking a screenshot on test failure and embedding it.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        if "driver" in item.fixturenames:
            driver = item.funcargs["driver"]
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_name = f"{item.name}_failure.png"
            screenshot_path = os.path.join(screenshot_dir, screenshot_name)
            try:
                driver.save_screenshot(screenshot_path)
                print(f"\nScreenshot saved: {screenshot_path}")

                # --- NEW PART: Base64 encoding and embedding ---
                with open(screenshot_path, "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read()).decode()

                # Use pytest_html.extras.png to embed the base64 encoded image
                # This ensures the image is truly self-contained in the report
                rep.extra.append(extras.png(encoded_string))
                # --- END NEW PART ---

            except Exception as e:
                print(f"Failed to take screenshot: {e}")