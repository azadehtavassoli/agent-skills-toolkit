import { test, expect } from '@playwright/test';

test.describe('Critical admin page', () => {
  test.use({ storageState: 'tests/auth/storage-state/admin.json' });

  test('loads and performs primary action', async ({ page }) => {
    const consoleErrors: string[] = [];

    page.on('console', msg => {
      if (msg.type() === 'error') {
        consoleErrors.push(msg.text());
      }
    });

    await page.goto('/settings/quotas');

    await expect(page.getByRole('heading', { name: /quotas/i })).toBeVisible();

    await page.getByRole('combobox', { name: /user class/i }).selectOption('vip');
    await page.getByRole('combobox', { name: /feature class/i }).selectOption('qa_synthesis');
    await page.getByRole('spinbutton', { name: /limit/i }).fill('500');
    await page.getByRole('spinbutton', { name: /window/i }).fill('86400');
    await page.getByRole('button', { name: /save/i }).click();

    await expect(page.getByText(/saved successfully/i)).toBeVisible();

    expect(consoleErrors).toEqual([]);
  });
});