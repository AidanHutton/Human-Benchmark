from typing import *


START_TEST_LOCATOR = '//button[@class="css-de05nr e19owgy710" and text()="Start Test"]'
ACTIVE_SQUARE_LOCATOR = '//div[@data-cellnumber]'
CONTINUE_TEST_LOCATOR = '//button[@class="css-de05nr e19owgy710" and text()="Continue"]'
TEST_IS_DONE_LOCATOR = '//div[@class="css-16iqw5x" and text()="Score"]'
RESULT_LOCATOR = '//h1[@class="css-0"]'


class ChimpTestPage:

    def __init__(self, page):
        self.page = page

    def start_test(self):
        self.page.locator(START_TEST_LOCATOR).click()

    def click_active_squares_in_order(self) -> List[Any]:
        while True:
            try:
                if self.page.locator(TEST_IS_DONE_LOCATOR).is_visible():
                    return [self.page.locator(RESULT_LOCATOR).inner_text()]
                elif self.page.locator(CONTINUE_TEST_LOCATOR).is_visible():
                    self.page.locator(CONTINUE_TEST_LOCATOR).click()

                active_squares = (self.page.query_selector_all(ACTIVE_SQUARE_LOCATOR))
                active_square_numbers = [int(active_square.get_attribute('data-cellnumber')) for active_square in active_squares]
                active_square_numbers.sort()

                for number in active_square_numbers:
                    self.page.locator(f'//div[@data-cellnumber="{number}"]').click(force=True)

            except Exception:
                pass
