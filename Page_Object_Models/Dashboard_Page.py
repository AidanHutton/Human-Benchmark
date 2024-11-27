REACTION_TIME_PAGE_LOCATOR = '//a[@class="css-uaat4j e19owgy72"]//h3[text()="Reaction Time"]'
SEQUENCE_MEMORY_PAGE_LOCATOR = '//a[@class="css-uaat4j e19owgy72"]//h3[text()="Sequence Memory"]'
AIM_TRAINER_PAGE_LOCATOR = '//a[@class="css-uaat4j e19owgy72"]//h3[text()="Aim Trainer"]'
NUMBER_MEMORY_PAGE_LOCATOR = '//a[@class="css-uaat4j e19owgy72"]//h3[text()="Number Memory"]'
VERBAL_MEMORY_PAGE_LOCATOR = '//a[@class="css-uaat4j e19owgy72"]//h3[text()="Verbal Memory"]'
CHIMP_TEST_PAGE_LOCATOR = '//a[@class="css-uaat4j e19owgy72"]//h3[text()="Chimp Test"]'
VISUAL_MEMORY_PAGE_LOCATOR = '//a[@class="css-uaat4j e19owgy72"]//h3[text()="Visual Memory"]'
TYPING_PAGE_LOCATOR = '//a[@class="css-uaat4j e19owgy72"]//h3[text()="Typing"]'
ALL_TESTS_LOCATOR = '//a[@class="css-de05nr e19owgy711"][text()="Get Started"]'


class DashboardPage:

    def __init__(self, page):
        self.page = page

    def goto_all_tests(self):
        self.page.locator(ALL_TESTS_LOCATOR).click()

    def goto_reaction_time_page(self):
        self.page.locator(REACTION_TIME_PAGE_LOCATOR).click()

    def goto_sequence_memory_page(self):
        self.page.locator(SEQUENCE_MEMORY_PAGE_LOCATOR).click()

    def goto_aim_trainer_page(self):
        self.page.locator(AIM_TRAINER_PAGE_LOCATOR).click()

    def goto_number_memory_page(self):
        self.page.locator(NUMBER_MEMORY_PAGE_LOCATOR).click()

    def goto_verbal_memory_page(self):
        self.page.locator(VERBAL_MEMORY_PAGE_LOCATOR).click()

    def goto_chimp_test_page(self):
        self.page.locator(CHIMP_TEST_PAGE_LOCATOR).click()

    def goto_visual_memory_page(self):
        self.page.locator(VISUAL_MEMORY_PAGE_LOCATOR).click()

    def goto_typing_page(self):
        self.page.locator(TYPING_PAGE_LOCATOR).click()
