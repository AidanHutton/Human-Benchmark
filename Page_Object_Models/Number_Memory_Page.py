from typing import *


RESULT_LOCATOR = '//div[@class="level"]'
START_TEST_LOCATOR = '//button[@class="css-de05nr e19owgy710" and text()="Start"]'
NUMBER_LOCATOR = '//div[@class="big-number "]'
INPUT_NUMBER_LOCATOR = '//div[@class="css-1qvtbrk e19owgy78"]//input'
SUBMIT_NUMBER_LOCATOR = '//button[@class="css-de05nr e19owgy710" and text()="Submit"]'
NEXT_NUMBER_LOCATOR = '//button[@class="css-de05nr e19owgy710" and text()="NEXT"]'


class NumberMemoryPage:

    def __init__(self, page):
        self.page = page

    def start_test(self):
        self.page.locator(START_TEST_LOCATOR).click()

    def remember_numbers(self):

        while True:
            try:
                numbers = self.page.locator(NUMBER_LOCATOR).inner_text()
                if len(numbers) > 20:
                    self.page.locator(INPUT_NUMBER_LOCATOR).fill("1")
                    self.page.locator(SUBMIT_NUMBER_LOCATOR).click()
                    break
                self.page.locator(INPUT_NUMBER_LOCATOR).fill(numbers)
                self.page.locator(SUBMIT_NUMBER_LOCATOR).click()
                self.page.locator(NEXT_NUMBER_LOCATOR).click()
            except Exception:
                pass

    def get_test_results(self) -> List[str]:
        results = [self.page.locator(RESULT_LOCATOR).inner_text()]
        return results
