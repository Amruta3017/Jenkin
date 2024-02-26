import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as CS
from selenium.webdriver.firefox.service import Service as FS
from selenium.webdriver.edge.service import Service as ES
from webdriver_manager.chrome import ChromeDriverManager as CDM
from webdriver_manager.firefox import GeckoDriverManager as GDM
from webdriver_manager.microsoft import EdgeChromiumDriverManager as ECDM
from pytest_metadata.plugin import metadata_key


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(service=CS(CDM().install()))
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FS(GDM().install()))
    elif browser == 'edge':
        driver = webdriver.Edge(service=ES(ECDM().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def admin_setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(service=CS(CDM().install()))
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FS(GDM().install()))
    elif browser == 'edge':
        driver = webdriver.Edge(service=ES(ECDM().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def pytest_addoption(parser):      # This will get the value from CLI /hooks
    parser.addoption("--browser", default="chrome")
    #parser.addoption("--browser", default="firefox")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    yield request.config.getoption("--browser")




################# PyTest HTML Report #################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'MNF'
    config.stash[metadata_key]['Module Name'] = 'Mynextfilm'
    config.stash[metadata_key]['Tester'] = 'Amruta'


# It is hook for delete/modify Environment info to HTML Report
@pytest.hookimpl(hookwrapper=True)
def pytest_sessionfinish(session, exitstatus):
    yield
    session.config.stash[metadata_key]["Python"] = "ReactJS"


