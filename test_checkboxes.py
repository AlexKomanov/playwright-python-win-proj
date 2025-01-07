import allure
from playwright.sync_api import Page, expect


@allure.feature("QA Practice")
@allure.story("Checkboxes")
def test_checkboxes(page: Page) -> None:
    page.goto("https://www.qa-practice.com/elements/checkbox/mult_checkbox")
    page.get_by_label("One").check()
    page.get_by_label("Two").check()
    page.get_by_label("Three").check()
    page.get_by_label("Three").uncheck()
    page.get_by_label("Three").check()
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Selected checkboxes:")).to_be_visible()
    expect(page.locator("#result-text")).to_contain_text("one, two, three")
    expect(page.locator(".site_header")).to_be_visible()
