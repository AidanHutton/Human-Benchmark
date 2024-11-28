from Page_Object_Models.Dashboard_Page import *
from Page_Object_Models.Visual_Memory_Page import *
from Utilities.Initialize_Test import *
import pytest


def execute_visual_memory(page):
    dashboard_page = DashboardPage(page=page)
    visual_memory_page = VisualMemoryPage(page=page)

    dashboard_page.goto_visual_memory_page()

    visual_memory_page.start_test()
    lives_remaining = 3
    while lives_remaining > 0:
        squares = visual_memory_page.detect_active_squares()
        if len(squares) > 100:
            visual_memory_page.break_out_of_test()
            lives_remaining -= 1
        visual_memory_page.click_active_squares(squares=squares)

    results = visual_memory_page.get_test_results()

    return results


test_result = initialize_test(test=execute_visual_memory)


@pytest.mark.parametrize("result", test_result)
def test_visual_memory(result):
    assert type(result) == str
