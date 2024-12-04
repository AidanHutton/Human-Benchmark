from Page_Object_Models.Dashboard_Page import *
from Page_Object_Models.Chimp_Test_Page import *
from Utilities.Initialize_Test import *
import pytest


def execute_chimp_test(page):
    dashboard_page = DashboardPage(page=page)
    chimp_page = ChimpTestPage(page=page)

    dashboard_page.goto_chimp_test_page()
    chimp_page.start_test()
    results = chimp_page.click_active_squares_in_order()

    return results


test_result = initialize_test(test=execute_chimp_test)


@pytest.mark.parametrize("result", test_result)
def test_chimp_test(result):
    assert type(result) == str
