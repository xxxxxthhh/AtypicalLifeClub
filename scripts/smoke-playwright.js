let chromium;
try {
    ({ chromium } = require("playwright"));
} catch (error) {
    console.error("Missing dependency: playwright. Run `npm install --no-save playwright` and `npx playwright install chromium` first.");
    process.exit(1);
}

const baseUrl = process.env.SMOKE_BASE_URL || "http://127.0.0.1:1313";

function assert(condition, message) {
    if (!condition) {
        throw new Error(message);
    }
}

async function testResearch(page) {
    await page.goto(`${baseUrl}/research/`, { waitUntil: "networkidle" });
    await page.waitForSelector(".report-card");

    const cardCount = await page.locator(".report-card").count();
    assert(cardCount > 0, "research page should have report cards");

    await page.getByRole("button", { name: "能源" }).click();
    await page.waitForSelector("#reportsGrid");
    const emptyState = await page.locator("#reportsGrid").innerText();
    assert(emptyState.includes("暂无研报"), "energy filter should show empty state");

    await page.getByRole("button", { name: "全部" }).click();
    await page.waitForSelector(".report-card");

    const firstHref = await page.locator(".report-card .read-more").first().getAttribute("href");
    assert(firstHref && firstHref.includes("/research/reports/view.html?id="), "report link should point to unified report template");

    await page.goto(`${baseUrl}${firstHref}`, { waitUntil: "networkidle" });
    await page.waitForSelector("#markdownContent h2, #markdownContent h1");

    const tocItems = await page.locator("#tableOfContents li").count();
    assert(tocItems > 0, "report detail should generate TOC");
}

async function testCurrency(page) {
    await page.goto(`${baseUrl}/currency/`, { waitUntil: "networkidle" });
    await page.waitForSelector(".stat-card");

    await page.selectOption("#base-currency-select", "USD");
    await page.selectOption("#currency-select", "JPY");
    await page.selectOption("#timerange-select", "30");

    await page.waitForTimeout(500);

    const statsText = await page.locator("#statistics").innerText();
    assert(statsText.includes("USD/JPY"), "statistics panel should update selected pair");

    const cardCount = await page.locator(".stat-card").count();
    assert(cardCount === 4, "currency dashboard should show four stat cards");

    const hasChart = await page.evaluate(() => {
        return typeof window.Chart !== "undefined" && !!document.getElementById("mainChart");
    });
    assert(hasChart, "currency dashboard should initialize chart canvas");
}

async function main() {
    const browser = await chromium.launch({ headless: true });
    const context = await browser.newContext();
    const page = await context.newPage();

    try {
        await testResearch(page);
        await testCurrency(page);
        console.log("Smoke tests passed.");
    } finally {
        await browser.close();
    }
}

main().catch((error) => {
    console.error("Smoke tests failed:", error.message);
    process.exit(1);
});
