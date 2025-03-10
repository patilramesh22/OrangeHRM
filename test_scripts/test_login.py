from generic.base_test import BaseTest
from generic.utility import Excel
from pages.homepage import HomePage
from pages.loginpage import LoginPage



class TestLogin(BaseTest):
    def test_valid_login(self):
        un=Excel.get_cell_value("../data/input.xlsx","ValidLogin",2,1)
        pw=Excel.get_cell_value("../data/input.xlsx","ValidLogin",2,2)
        lp = LoginPage(self.driver)
        lp.set_username(un)
        lp.set_password(pw)
        lp.click_on_login()
        hp = HomePage(self.driver)
        result = hp.verify_homepage_is_displayed(self.wait)
        assert result

    def test_invalid_login(self):
        un = Excel.get_cell_value("D:/book1.xlsx", "Sheet2", 2, 1)
        pw = Excel.get_cell_value("D:/book1.xlsx", "Sheet2", 2, 2)
        lp = LoginPage(self.driver)
        lp.set_username(un)
        lp.set_password(pw)
        lp.click_on_login()
        result = lp.verify_error_msg(self.wait)
        assert result
