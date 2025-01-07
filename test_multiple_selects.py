from playwright.sync_api import Page, expect
import allure


@allure.feature("QA Practice")
@allure.story("Multi Select")
def test_multiple_selects(page: Page) -> None:
    page.goto("https://www.qa-practice.com/elements/select/mult_select")
    page.get_by_label("Choose the place you want to").select_option("4")
    print(page.get_by_label("Choose the place you want to").text_content())
    print(page.get_by_label("Choose the place you want to").inner_text())
    expect(page.get_by_label("Choose the place you want to")).to_have_value("4")
    page.get_by_label("Choose how you want to get").select_option("1")
    page.get_by_label("Choose when you want to go*").select_option("2")
    expect(page.get_by_role("button", name="Submit")).to_be_visible()
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("You selected")).to_be_visible()
    page.get_by_text("to go by car to the ocean").click()
    expect(page.locator("#result-text")).to_contain_text("to go by car to the ocean tomorrow")
