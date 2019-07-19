from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest
import time

def pytest_addoption(parser):
    parser.addoption('--browser',action='store',default='chrome')


@pytest.fixture(scope='function')
def Setup(request):
    try:
        browser=request.config.getoption('--browser')
        if browser=='chrome':
            driver=webdriver.Chrome(ChromeDriverManager().install())
        elif browser=='firefox':
            driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.maximize_window()
        request.cls.driver=driver
        yield
        driver.close()
        driver.quit()

    except:
        print('Error in Configuration')
