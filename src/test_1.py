import pytest
from playwright.async_api import async_playwright


@pytest.mark.asyncio
async def test_add_a_row():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://localhost:8501/")
        await page.get_by_label("ID").click()
        await page.get_by_label("ID").fill("11")
        await page.get_by_test_id("stTabs").get_by_label("Name").click()
        await page.get_by_test_id("stTabs").get_by_label("Name").fill("11")
        await page.get_by_test_id("stTabs").get_by_label("Type").click()
        await page.get_by_test_id("stTabs").get_by_label("Type").fill("11")
        await page.get_by_label("Size 1").click()
        await page.get_by_label("Size 1").fill("11")
        await page.get_by_label("Size 2").click()
        await page.get_by_label("Size 2").fill("11")
        await page.get_by_label("Size 3").click()
        await page.get_by_label("Size 3").fill("11")
        await page.get_by_role("button", name="Add data").click()
        await browser.close()


@pytest.mark.asyncio
async def test_change_tabs():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://localhost:8501/")
        await page.get_by_role("tab", name="Edit & Calculate").click()
        await page.get_by_role("tab", name="Check Metrics").click()
        await page.get_by_role("tab", name="Edit & Calculate").click()
        await page.get_by_role("tab", name="Add Data").click()
        await browser.close()
