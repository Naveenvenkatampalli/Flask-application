from Tests.test_base import BaseTest
from Pages.loginpage import LoginPage
import pytest

@pytest.mark.run(order=1)
@pytest.mark.usefixtures("drivers")
class Test_Login(BaseTest):
    def test_login(self, drivers, sanity_mode):
        driver1, driver2, driver3, driver4 = drivers
        
        login_page1 = LoginPage(driver1)
        login_page2 = LoginPage(driver2)
        login_page3 = LoginPage(driver3)
        login_page4 = LoginPage(driver4)
        
        if not sanity_mode:
            # Login in the first window
            login_page1.login_github()
            
        else:
            # Login in the first window
            login_page3.login_github()

        
