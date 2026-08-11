import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { expect, test } from "@playwright/test";

test("representative navigation has explicit focus", async ({ page }) => {
  await page.goto("/");
  await page.getByRole("button", { name: "Open details" }).click();
  await expect(page.getByRole("heading", { name: "Details ready" })).toBeFocused();
});

test("content reflows without horizontal document overflow", async ({ page }) => {
  await page.setViewportSize({ width: 320, height: 720 });
  await page.goto("/");
  const sizes = await page.evaluate(() => ({ scroll: document.documentElement.scrollWidth, client: document.documentElement.clientWidth }));
  expect(sizes.scroll).toBeLessThanOrEqual(sizes.client);
  await expect(page.locator(".card-shell")).toHaveCSS("border-left-color", "rgb(49, 89, 184)");
});

test("predeclared navigation budget is measured repeatedly", async ({ page }, testInfo) => {
  const budget = JSON.parse(await readFile(resolve(process.cwd(), "performance-budget.json"), "utf8")) as {
    repetitions: number;
    maximum_navigation_ms: number;
  };
  const results: number[] = [];
  for (let run = 0; run < budget.repetitions; run += 1) {
    const started = performance.now();
    await page.goto(`/?run=${run}`);
    await page.getByRole("heading", { name: "Browser behavior with explicit boundaries" }).waitFor();
    results.push(performance.now() - started);
  }
  await testInfo.attach("navigation-measurements.json", {
    body: Buffer.from(JSON.stringify({ budget, results }, null, 2)),
    contentType: "application/json",
  });
  expect(results.every((value) => value <= budget.maximum_navigation_ms)).toBe(true);
});
