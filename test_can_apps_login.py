from playwright.sync_api import Page, expect
from faker import Faker
import allure
fake = Faker()

@allure.feature("Canvu Apps")
@allure.feature("Login")
@allure.title("Login Test")
def test_example(page: Page):
    url = 'https://canvusapps.com/login'
    with allure.step(f"Navigating to {url}"):
        page.goto(url)

    with allure.step("Filling login form"):
        random_email = fake.email()
        page.locator('#email').fill(random_email)
        page.locator('[name="password"]').fill(fake.password(length=8, digits=True))
        page.get_by_role('checkbox', name='Remember me').check()
        page.get_by_role('button', name='Login').click()

    with allure.step("Validation of redirection"):
        expect(page).to_have_url('https://canvusapps.com/sessions')
        # assert page.locator('.alert-block').inner_text() == '1Invalid email or password1' # Assert without retry
        expect(page.locator('.alert-block')).to_have_text('Invalid email or password', timeout=8000) # Assert with timeout and retry
