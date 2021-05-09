import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: chrome or firefox"
    )


@pytest.fixture(scope="class")
def browserSetup(request):
        browser_name = request.config.getoption("--browser_name")

        if browser_name == "chrome":
                driver = webdriver.Chrome(executable_path="../drivers/chromedriver")
        elif browser_name == "firefox":
                driver = webdriver.Firefox(executable_path="../drivers/geckodriver")

        #driver.implicitly_wait(5)
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
        request.cls.driver = driver
        yield
        driver.quit()