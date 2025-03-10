import pytest
from pyjavaproperties import Properties
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class BaseTest:
    @pytest.fixture(autouse=True)
    def pre_post_condition(self):
        pfile=Properties()
        pfile.load(open("../config.properties"))
        browser=pfile['browser']
        url=pfile['url']
        ITO=pfile['ITO']
        ETO=pfile['ETO']
        use_grid=pfile['use_grid']
        grid_url=pfile['grid_url']
        if use_grid=='no':
            if browser=='chrome':
                self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
                print("Launched chrome browser in local system")
            else:
                self.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
                print("Launched firefox browser in local system")
        else:
            if browser=='chrome':
                browser_option=webdriver.ChromeOptions()
                print("Launched chrome browser in remote system")
            else:
                browser_option=webdriver.FirefoxOptions()
                print("Launched firefox browser in remote system")
            self.driver=webdriver.Remote(grid_url,options=browser_option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(ITO)
        self.wait=WebDriverWait(self.driver,ETO)
        self.driver.get(url)
        yield
        self.driver.close()