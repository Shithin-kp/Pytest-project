import time

import pytest
from pages.login_page import LoginPage

@pytest.mark.priority1
def test_valid_login(driver):
    """
       Test description: Verify valid login redirects to Lynks dashboard.
    """
    login_page = LoginPage(driver)
    login_page.load()
    login_page.enterUserName("shithin.kokkarni@kefitech.com")
    login_page.enterPassword("DUlKKyKV")
    time.sleep(8)
    login_page.clickLogin()
    assert "home" in driver.current_url, "Failed to redirect to Lynks dashboard after valid login"

@pytest.mark.priority2
def test_invalid_login(driver):
    """
           Test description: Verify invalid login
    """
    login_page = LoginPage(driver)
    login_page.load()
    login_page.enterUserName("invalid_user")
    login_page.enterPassword("invalid_password")
    time.sleep(8)
    login_page.clickLogin()
    assert "Incorrect Credentials" in login_page.loginError()