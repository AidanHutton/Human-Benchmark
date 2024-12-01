from typing import *

START_TEST_LOCATOR = '//button[@class="css-de05nr e19owgy710" and text()="Start"]'
ACTIVE_SQUARE = '//div[@class="active css-lxtdud eut2yre1"]'
SQUARE_LOCATOR = '//div[@class="css-hvbk5q eut2yre0"]//div//div'
RESULT_LOCATOR = '//h1[@class="css-0"]'


class VisualMemoryPage:

    def __init__(self, page):
        self.page = page

    def start_test(self):
        self.page.locator(START_TEST_LOCATOR).click()

    def detect_active_squares(self):
        squares = []

        while True:
            try:
                active_locator = self.page.locator(ACTIVE_SQUARE)
                if active_locator.count() > 0:
                    all_squares = self.page.locator(SQUARE_LOCATOR)
                    number_of_squares = all_squares.count()
                    squares.clear()
                    for i in range(number_of_squares):
                        element_locator = all_squares.nth(i)
                        element_class = element_locator.get_attribute("class")
                        squares.append(element_class)
                    return squares
                else:
                    pass

            except Exception:
                pass

    def click_active_squares(self, squares):

        while True:
            try:
                active_locator = self.page.locator(ACTIVE_SQUARE)
                if active_locator.count() == 0:
                    for i in range(len(squares)):
                        if "active" in squares[i]:
                            self.page.locator(f'(//div[@class="css-hvbk5q eut2yre0"]//div//div)[{i + 1}]').click(force=True)
                    break
                else:
                    pass
            except Exception:
                pass

    def break_out_of_test(self, squares):

        while True:
            try:
                active_locator = self.page.locator(ACTIVE_SQUARE)
                if active_locator.count() == 0:
                    for i in range(len(squares)):
                        if "active" not in squares[i]:
                            try:
                                self.page.locator(f'(//div[@class="css-hvbk5q eut2yre0"]//div//div)[{i + 1}]').click(force=True)
                            except Exception:
                                pass
                    break
                else:
                    pass
            except Exception:
                pass

    def get_test_results(self) -> List[str]:
        while True:
            if self.page.locator(RESULT_LOCATOR).is_visible():
                results = [self.page.locator(RESULT_LOCATOR).inner_text()]
                return results
            else:
                pass
