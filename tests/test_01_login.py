import time

import pytest
from pages.login_page import LoginPage
from conftest import username, password

@pytest.mark.priority1
def test_valid_login(driver):
    """
    Test description: Verify valid login redirects to Lynks dashboard.
    """
    login_page = LoginPage(driver)
    login_page.enterUserName(username)
    login_page.enterPassword(password)
    # Pause to let you solve the CAPTCHA manually
    login_page.pauseForCaptcha()
    login_page.clickLogin()
    time.sleep(2)
    assert "home" in driver.current_url, "Failed to redirect to Lynks dashboard after valid login"

@pytest.mark.priority2
def test_invalid_login(driver):
    """
           Test description: Verify invalid login
    """
    login_page = LoginPage(driver)
    login_page.enterUserName("invalid_user")
    login_page.enterPassword("invalid_password")
    # Pause to let you solve the CAPTCHA manually
    login_page.pauseForCaptcha()
    login_page.clickLogin()
    assert "Incorrect Credentials" in login_page.loginError()