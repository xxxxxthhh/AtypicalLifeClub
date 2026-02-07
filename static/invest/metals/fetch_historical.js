#!/usr/bin/env node
/**
 * Fetch historical metals & ETF data from Yahoo Finance.
 * Builds the initial historical.json for the Metals module.
 */

const https = require('https');
const fs = require('fs');
const path = require('path');

const METALS = {
  "GC=F":  { name: "Gold",      unit: "USD/oz" },
  "SI=F":  { name: "Silver",    unit: "USD/oz" },
  "PL=F":  { name: "Platinum",  unit: "USD/oz" },
  "PA=F":  { name: "Palladium", unit: "USD/oz" },
  "HG=F":  { name: "Copper",    unit: "USD/lb" },
};

const ETFS = {
  "COPX": { name: "Global X Copper Miners ETF",        category: "copper" },
  "GLD":  { name: "SPDR Gold Shares",                  category: "gold" },
  "SLV":  { name: "iShares Silver Trust",              category: "silver" },
  "CPER": { name: "US Copper Index Fund",              category: "copper" },
  "DBB":  { name: "Invesco DB Base Metals Fund",       category: "base_metals" },
  "REMX": { name: "VanEck Rare Earth/Strategic Metals", category: "rare_earth" },
  "LIT":  { name: "Global X Lithium & Battery Tech",   category: "lithium" },
  "PPLT": { name: "abrdn Physical Platinum Shares",    category: "platinum" },
  "PALL": { name: "abrdn Physical Palladium Shares",   category: "palladium" },
};

function fetchJSON(url) {
  return new Promise((resolve, reject) => {
    https.get(url, { headers: { 'User-Agent': 'Mozilla/5.0' } }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try { resolve(JSON.parse(data)); }
        catch (e) { reject(new Error(`Parse error: ${e.message}`)); }
      });
    }).on('error', reject);
  });
}

async function fetchHistory(symbol, days = 730) {
  const now = Math.floor(Date.now() / 1000);
  const start = now - days * 86400;
  const url = `https://query1.finance.yahoo.com/v8/finance/chart/${encodeURIComponent(symbol)}?period1=${start}&period2=${now}&interval=1d`;

  try {
    const json = await fetchJSON(url);
    const result = json.chart?.result?.[0];
    if (!result || !result.timestamp) {
      console.log(`  ⚠ No data for ${symbol}`);
      return [];
    }
    const timestamps = result.timestamp;
    const closes = result.indicators?.quote?.[0]?.close || [];
    const volumes = result.indicators?.quote?.[0]?.volume || [];

    const records = [];
    for (let i = 0; i < timestamps.length; i++) {
      if (closes[i] == null) continue;
      const d = new Date(timestamps[i] * 1000);
      records.push({
        date: d.toISOString().split('T')[0],
        close: Math.round(closes[i] * 10000) / 10000,
        volume: volumes[i] || 0,
      });
    }
    console.log(`  ✓ ${symbol}: ${records.length} days`);
    return records;
  } catch (e) {
    console.log(`  ✗ ${symbol}: ${e.message}`);
    return [];
  }
}

function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function main() {
  const outPath = process.argv[2] || path.join(__dirname, 'data', 'historical.json');
  console.log(`Building historical data → ${outPath}\n`);

  console.log('=== Fetching Metals Spot Data ===');
  const metalsData = {};
  for (const [symbol, info] of Object.entries(METALS)) {
    metalsData[symbol] = await fetchHistory(symbol);
    await sleep(500);
  }

  console.log('\n=== Fetching ETF Data ===');
  const etfsData = {};
  for (const [symbol, info] of Object.entries(ETFS)) {
    etfsData[symbol] = await fetchHistory(symbol);
    await sleep(500);
  }

  // Build current prices
  const current = {};
  const allData = { ...metalsData, ...etfsData };
  for (const [symbol, history] of Object.entries(allData)) {
    if (history.length >= 2) {
      const latest = history[history.length - 1];
      const prev = history[history.length - 2];
      const change = latest.close - prev.close;
      const pct = prev.close ? (change / prev.close * 100) : 0;
      current[symbol] = {
        price: latest.close,
        change: Math.round(change * 10000) / 10000,
        changePct: Math.round(pct * 100) / 100,
        date: latest.date,
      };
    }
  }

  const result = {
    metadata: {
      metals: METALS,
      etfs: ETFS,
      lookback_days: 730,
      last_updated: new Date().toISOString(),
      total_metals: Object.keys(METALS).length,
      total_etfs: Object.keys(ETFS).length,
    },
    current,
    metals: metalsData,
    etfs: etfsData,
  };

  fs.mkdirSync(path.dirname(outPath), { recursive: true });
  fs.writeFileSync(outPath, JSON.stringify(result, null, 2), 'utf-8');

  let total = 0;
  for (const v of Object.values(metalsData)) total += v.length;
  for (const v of Object.values(etfsData)) total += v.length;
  console.log(`\n✅ Done! Saved to ${outPath}`);
  console.log(`   Total data points: ${total}`);
}

main().catch(e => { console.error(e); process.exit(1); });
