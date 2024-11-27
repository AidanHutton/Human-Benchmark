from Page_Object_Models.Dashboard_Page import *
from Page_Object_Models.Verbal_Memory_Page import *
from Utilities.Initialize_Test import *
import pytest


def execute_aim(page):
    dashboard_page = DashboardPage(page=page)
    verbal_memory_page = VerbalMemoryPage(page=page)

    dashboard_page.goto_verbal_memory_page()

    verbal_memory_page.start_test()
    verbal_memory_page.detect_seen_words()
    results = verbal_memory_page.get_test_results()

    return results


test_result = initialize_test(test=execute_aim)


@pytest.mark.parametrize("result", test_result)
def test_aim(result):
    assert type(result) == str
