from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    __username = (By.NAME, 'username')
    __password = (By.NAME, 'password')
    __login_btn = (By.XPATH, "//button[@type='submit']")
    __error_msg = (By.XPATH, "//p[.='Invalid credentials']")

    def __init__(self, driver):
        self.__driver = driver

    def set_username(self,un):
        self.__driver.find_element(*self.__username).send_keys(un)

    def set_password(self,pw):
        self.__driver.find_element(*self.__password).send_keys(pw)

    def click_on_login(self):
        self.__driver.find_element(*self.__login_btn).click()

    def verify_error_msg(self,wait):
        try:
            wait.until(EC.visibility_of_element_located(self.__error_msg))
            print("Error msg is displayed")
            print("Error msg text is:",self.__driver.find_element(*self.__error_msg).text)
            return True
        except:
            print("Error msg is not displayed")
            return False