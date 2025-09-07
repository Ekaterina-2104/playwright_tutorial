import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {

        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }

@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)
