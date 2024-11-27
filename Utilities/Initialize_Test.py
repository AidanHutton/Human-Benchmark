from playwright.sync_api import sync_playwright


def initialize_test(test):
    with sync_playwright() as playwright_function:
        chrome = playwright_function.chromium
        browser = chrome.launch(headless=False)
        browser_context = browser.new_context(no_viewport=True)
        page = browser_context.new_page()

        page.goto("https://humanbenchmark.com/")

        results = test(page)

        return results
