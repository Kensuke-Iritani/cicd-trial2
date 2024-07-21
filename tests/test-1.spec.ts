import { test, expect } from '@playwright/test';

test('add a row', async ({ page }) => {
  await page.goto('http://localhost:8501/');
  await page.getByLabel('ID').click();
  await page.getByLabel('ID').fill('11');
  await page.getByTestId('stTabs').getByLabel('Name').click();
  await page.getByTestId('stTabs').getByLabel('Name').fill('11');
  await page.getByTestId('stTabs').getByLabel('Type').click();
  await page.getByTestId('stTabs').getByLabel('Type').fill('11');
  await page.getByLabel('Size 1').click();
  await page.getByLabel('Size 1').fill('11');
  await page.getByLabel('Size 2').click();
  await page.getByLabel('Size 2').fill('11');
  await page.getByLabel('Size 3').click();
  await page.getByLabel('Size 3').fill('11');
  await page.getByRole('button', { name: 'Add data' }).click();
});


test('change tabs', async ({ page }) => {
  await page.goto('http://localhost:8501/');
  await page.getByRole('tab', { name: 'Edit & Calculate' }).click();
  await page.getByRole('tab', { name: 'Check Metrics' }).click();
  await page.getByRole('tab', { name: 'Edit & Calculate' }).click();
  await page.getByRole('tab', { name: 'Add Data' }).click();
});