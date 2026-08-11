import { readdir } from "node:fs/promises";
import { resolve } from "node:path";
import { expect, test } from "@playwright/test";

async function emittedFiles(directory: string): Promise<string[]> {
  const rows: string[] = [];
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const path = resolve(directory, entry.name);
    if (entry.isDirectory()) rows.push(...(await emittedFiles(path)));
    else rows.push(path);
  }
  return rows;
}

test("built page excludes inline executable script and emitted source maps", async ({ page, request }) => {
  const response = await request.get("/");
  const html = await response.text();
  expect(html).not.toMatch(/<script(?![^>]*\bsrc=)[^>]*>/i);
  await page.goto("/");
  const scripts = await page.locator("script[src]").evaluateAll((nodes) => nodes.map((node) => (node as HTMLScriptElement).src));
  expect(scripts.length).toBeGreaterThan(0);
  const files = await emittedFiles(resolve(process.cwd(), "dist"));
  expect(files.some((file) => file.endsWith(".map"))).toBe(false);
});

test("unsafe schemes are not rendered as navigable links", async ({ page }) => {
  await page.goto("/");
  const hrefs = await page.locator("a").evaluateAll((nodes) => nodes.map((node) => (node as HTMLAnchorElement).href));
  expect(hrefs.every((href) => href.startsWith("http://") || href.startsWith("https://"))).toBe(true);
});
