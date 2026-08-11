import AxeBuilder from "@axe-core/playwright";
import { expect, test } from "@playwright/test";

test("representative view has no detected automated accessibility violations", async ({ page }) => {
  await page.goto("/");
  const results = await new AxeBuilder({ page }).analyze();
  expect(results.violations).toEqual([]);
});

test("representative flow is keyboard operable", async ({ browserName, page }) => {
  await page.goto("/");
  const forwardKey = browserName === "webkit" && process.platform === "darwin" ? "Alt+Tab" : "Tab";
  await page.keyboard.press(forwardKey);
  await expect(page.getByRole("button", { name: "Open details" })).toBeFocused();
  await page.keyboard.press("Enter");
  await expect(page.getByRole("heading", { name: "Details ready" })).toBeFocused();
});
