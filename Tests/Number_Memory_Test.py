from Page_Object_Models.Dashboard_Page import *
from Page_Object_Models.Number_Memory_Page import *
from Utilities.Initialize_Test import *
import pytest


def execute_number_memory(page):
    dashboard_page = DashboardPage(page=page)
    number_memory_page = NumberMemoryPage(page=page)

    dashboard_page.goto_number_memory_page()

    number_memory_page.start_test()
    number_memory_page.remember_numbers()
    results = number_memory_page.get_test_results()

    return results


test_result = initialize_test(test=execute_number_memory)


@pytest.mark.parametrize("result", test_result)
def test_number_memory(result):
    assert type(result) == str
