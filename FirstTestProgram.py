from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.facebook.com/")
    page.get_by_test_id("royal_email").click()
    page.get_by_test_id("royal_email").fill("vikash.kunj@gmail.com")
    page.get_by_test_id("royal_pass").click()
    page.get_by_test_id("royal_pass").fill("Aircel@test")
    page.get_by_test_id("royal_login_button").click()
    page.get_by_text("Wrong credentials").is_enabled()
    page.get_by_text("Invalid username or password").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
