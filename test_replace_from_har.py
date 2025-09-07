# playwright open --save-har=example.har --save-har-glob="**/api/users/2" https://reqres.in
from playwright.sync_api import expect


def test_replace_from_har(page):
    page.goto("https://reqres.in/")
    page.route_from_har("example.har")
    users_single = page.locator('li[data-id="users-single"]')
    users_single.click()
    response = page.locator('[data-key="output-response"]')
    expect(response).to_contain_text("Open Solutions")
