from Page_Object_Models.Dashboard_Page import *
from Page_Object_Models.Typing_Page import *
from Utilities.Initialize_Test import *
import pytest


def execute_typing(page):
    dashboard_page = DashboardPage(page=page)
    typing_page = TypingPage(page=page)

    dashboard_page.goto_typing_page()
    characters = typing_page.get_all_characters()
    typing_page.type(characters=characters)

    results = typing_page.get_test_results()
    return results


test_result = initialize_test(test=execute_typing)


@pytest.mark.parametrize("result", test_result)
def test_typing_results(result):
    assert type(result) == str
