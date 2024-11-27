from typing import *


RESULT_LOCATOR = '//h1[@class="css-0"]'


class TypingPage:

    def __init__(self, page):
        self.page = page

    def get_all_characters(self) -> List[Any]:
        characters = []

        starting_character = self.page.locator('//span[@class="incomplete current"]').inner_text()
        characters.append(starting_character)

        number_of_characters = len(self.page.query_selector_all('//span[@class="incomplete"]'))
        for i in range(number_of_characters):
            character = self.page.locator(f'//span[@class="incomplete"][{i + 1}]').inner_text()
            characters.append(character)

        return characters

    def type(self, characters: List[Any]) -> None:
        for character in characters:
            self.page.keyboard.press(character)

    def get_test_results(self) -> List[str]:
        results = [self.page.locator(RESULT_LOCATOR).inner_text()]
        return results
