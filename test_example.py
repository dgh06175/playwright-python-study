import re

from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))


def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()


def test_example(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    expect(page.get_by_role("heading")).to_contain_text("todos")
    expect(page.get_by_role("textbox", name="What needs to be done?")).to_be_visible()
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("pytest")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("checkbox", name="Toggle Todo").check()
    expect(page.get_by_role("button", name="Clear completed")).to_be_visible()
    expect(page.locator("body")).to_contain_text("0 items")
