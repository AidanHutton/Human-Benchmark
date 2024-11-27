from Page_Object_Models.Dashboard_Page import *
from Page_Object_Models.Reaction_Time_Page import *
from Utilities.Initialize_Test import *
import pytest


def execute_reaction_time(page):
    dashboard_page = DashboardPage(page=page)
    reaction_time_page = ReactionTimePage(page=page)

    dashboard_page.goto_reaction_time_page()

    reaction_time_page.start_test()
    reaction_time_page.click_screen_when_ready()
    results = reaction_time_page.get_test_results()

    return results


test_result = initialize_test(test=execute_reaction_time)


@pytest.mark.parametrize("result", test_result)
def test_reaction_time(result):
    assert type(result) == str
