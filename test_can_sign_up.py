import pytest
from playwright.sync_api import Page, expect
from faker import Faker
fake = Faker()
import allure


@allure.feature("Canvu Apps")
@allure.story("Signup")
@pytest.skip()
def test_example(page: Page) -> None:
    random_name = fake.name()
    random_email = fake.email()
    random_password = fake.password()
    random_company = fake.company()
    page.set_viewport_size({"width": 1600, "height": 1200})
    page.goto("https://canvusapps.com/signup")
    page.locator("#user_name").fill(random_name)
    page.locator("#user_email").fill(random_email)
    page.locator("#user_password").fill(random_password)
    page.locator("#user_password_confirmation").fill(random_password)
    page.get_by_label("Company Name").fill(random_company)
    page.get_by_role("button", name="Sign up").click()
    expect(page.get_by_role("heading", name="Congratulations!")).to_be_visible()
    expect(page.get_by_role("heading", name="Congratulations!")).to_have_text("Congratulations!")
