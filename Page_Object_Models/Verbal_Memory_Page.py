from typing import *


RESULT_LOCATOR = '//h1[@class="css-0"]'
START_TEST_LOCATOR = '//button[@class="css-de05nr e19owgy710"]'
WORD_LOCATOR = '//div[@class="word"]'
SEEN_WORD_LOCATOR = '//button[@class="css-de05nr e19owgy710" and text()="SEEN"]'
NEW_WORD_LOCATOR = '//button[@class="css-de05nr e19owgy710" and text()="NEW"]'


class VerbalMemoryPage:

    def __init__(self, page):
        self.page = page

    def start_test(self):
        self.page.locator(START_TEST_LOCATOR).click()

    def detect_seen_words(self):
        words = []
        while True:
            if self.page.locator(WORD_LOCATOR).is_visible():
                word = self.page.locator(WORD_LOCATOR).inner_text()
                if len(words) > 1000:
                    self.page.locator(NEW_WORD_LOCATOR).click()
                elif word in words:
                    self.page.locator(SEEN_WORD_LOCATOR).click()
                else:
                    words.append(word)
                    self.page.locator(NEW_WORD_LOCATOR).click()
            elif self.page.locator(RESULT_LOCATOR).is_visible():
                break
            else:
                pass

    def get_test_results(self) -> List[str]:
        results = [self.page.locator(RESULT_LOCATOR).inner_text()]
        return results
