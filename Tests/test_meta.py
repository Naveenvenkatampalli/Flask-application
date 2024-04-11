from Tests.test_base import BaseTest
import pytest

@pytest.mark.run(order=2)#4
@pytest.mark.usefixtures("drivers")
class Test_SetMeta(BaseTest):
    def test_set_meta(self, drivers, sanity_mode):
        driver1,driver2,driver3,driver4=drivers
        print("running metadata successfully")
