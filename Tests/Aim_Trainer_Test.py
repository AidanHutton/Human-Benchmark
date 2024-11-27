from Page_Object_Models.Dashboard_Page import *
from Page_Object_Models.Aim_Trainer_Page import *
from Utilities.Initialize_Test import *
import pytest


def execute_aim(page):
    dashboard_page = DashboardPage(page=page)
    aim_trainer_page = AimTrainerPage(page=page)

    dashboard_page.goto_aim_trainer_page()

    aim_trainer_page.click_on_target()
    results = aim_trainer_page.get_test_results()

    return results


test_result = initialize_test(test=execute_aim)


@pytest.mark.parametrize("result", test_result)
def test_aim(result):
    assert type(result) == str
