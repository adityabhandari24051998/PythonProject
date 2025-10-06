import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",help="browser selection")


@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("--browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome()


    elif browser_name=="firefox":
        driver= webdriver.Firefox()


    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/loginpagePractise")


    yield driver

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to get report object
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        print(f"\n❌ Test Failed: {report.nodeid}")

        # Example: attach screenshot if using Selenium
        if "browserInstance" in item.fixturenames:
            driver = item.funcargs["browserInstance"]
            driver.save_screenshot(f"screenshots/{item.name}.png")
            print(f"Screenshot saved: screenshots/{item.name}.png")

    elif report.when == "call" and report.passed:
        print(f"\n✅ Test Passed: {report.nodeid}")