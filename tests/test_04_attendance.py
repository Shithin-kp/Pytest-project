import time

import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.attendance_page import AttendancePage
from conftest import username, password


@pytest.mark.priority1
def test_attendance_page_elements(driver):
    """
    Test description: Verify the presence of key elements on the Attendance page after login.
    """
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    attendance_page = AttendancePage(driver)
    # Pause to let you solve the CAPTCHA manually
    login_page.pauseForCaptcha()
    login_page.logIn(username, password)
    time.sleep(1)
    assert "home" in driver.current_url, "Failed to redirect to the home page after login"
    home_page.clickAttendance()

