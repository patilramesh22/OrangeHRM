from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    __dashboard = (By.XPATH, "//h6[.='Dashboard']")

    def __init__(self, driver):
        self.__driver = driver

    def verify_homepage_is_displayed(self,wait):
        try:
            wait.until(EC.visibility_of_element_located(self.__dashboard))
            print("Homepage is displayed")
            return True
        except:
            print("Homepage is not displayed")
            return False
