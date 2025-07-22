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
    time.sleep(1)
    assert attendance_page.attendancePageEntryTabElements() is True, "Entry tab is not displayed on the Attendance page"
    assert attendance_page.attendancePageExitTabElements() is True, "Exit tab is not displayed on the Attendance page"

@pytest.mark.priority2
def test_mark_exit_button(driver):
    """
    Test description: Verify the functionality of the Mark Exit button on the Attendance page.
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
    time.sleep(1)
    attendance_page.clickMarkExit()
    time.sleep(1)

