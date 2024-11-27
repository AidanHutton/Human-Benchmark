from typing import *


MAIN_TEST_WIDGET_LOCATOR = '(//div[@class="css-1qvtbrk e19owgy78"])[3]'
READY_TO_CLICK_LOCATOR = '(//div[@class="view-go e18o0sx0 css-saet2v e19owgy77"])'
VIEW_RESULTS_LOCATOR = '(//div[@class="view-result e18o0sx0 css-saet2v e19owgy77"])'
RESULT_LOCATOR = '//h1[@class="css-0"]'


class ReactionTimePage:
    def __init__(self, page):
        self.page = page

    def start_test(self):
        self.page.locator(MAIN_TEST_WIDGET_LOCATOR).click()

    def click_screen_when_ready(self):
        while True:
            if self.page.locator(READY_TO_CLICK_LOCATOR).is_visible():
                self.page.locator(READY_TO_CLICK_LOCATOR).click()
            elif self.page.locator(VIEW_RESULTS_LOCATOR).is_visible():
                self.page.locator(VIEW_RESULTS_LOCATOR).click()
            elif self.page.locator(RESULT_LOCATOR).is_visible():
                break
            else:
                pass

    def get_test_results(self) -> List[str]:
        results = [self.page.locator(RESULT_LOCATOR).inner_text()]
        return results
