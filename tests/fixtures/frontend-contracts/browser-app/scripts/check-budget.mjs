import { gzipSync } from "node:zlib";
import { readdir, readFile } from "node:fs/promises";
import { resolve } from "node:path";

const root = resolve(import.meta.dirname, "..");
const budget = JSON.parse(await readFile(resolve(root, "performance-budget.json"), "utf8"));

async function assets(directory) {
  const rows = [];
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const path = resolve(directory, entry.name);
    if (entry.isDirectory()) rows.push(...(await assets(path)));
    else if (/\.(?:css|js)$/.test(entry.name)) rows.push(path);
  }
  return rows;
}

const files = await assets(resolve(root, "dist"));
const measurements = [];
for (const file of files) {
  const bytes = gzipSync(await readFile(file)).byteLength;
  measurements.push({ file: file.slice(root.length + 1), gzip_bytes: bytes });
}
const total = measurements.reduce((sum, row) => sum + row.gzip_bytes, 0);
console.log(JSON.stringify({ measurements, total_gzip_bytes: total, budget_bytes: budget.maximum_compressed_asset_bytes }, null, 2));
if (total > budget.maximum_compressed_asset_bytes) process.exitCode = 1;
