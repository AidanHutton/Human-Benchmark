from typing import *


RESULT_LOCATOR = '//h1[@class="css-0"]'
TARGET_LOCATOR = '//div[@class="css-z6vxiy e6yfngs3"][1]'


class AimTrainerPage:

    def __init__(self, page):
        self.page = page

    def click_on_target(self):
        while True:
            if self.page.locator(TARGET_LOCATOR).is_visible():
                self.page.locator(TARGET_LOCATOR).click(force=True)
            elif self.page.locator(RESULT_LOCATOR).is_visible():
                break
            else:
                pass

    def get_test_results(self) -> List[str]:
        results = [self.page.locator(RESULT_LOCATOR).inner_text()]
        return results
