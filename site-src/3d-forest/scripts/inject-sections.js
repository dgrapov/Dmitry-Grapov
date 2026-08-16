#!/usr/bin/env node
// Splices a sections.json (see extract-sections.js) back into the .dc.html source,
// replacing the `sections = [...]` array in place. Preserves everything else in the file.
// Usage: node inject-sections.js "Dmitry Grapov Forest.dc.html" sections.json
'use strict';
const fs = require('fs');
const [, , file, jsonFile] = process.argv;
if (!file || !jsonFile) {
  console.error('Usage: inject-sections.js <file.dc.html> <sections.json>');
  process.exit(1);
}
const src = fs.readFileSync(file, 'utf8');
const sections = JSON.parse(fs.readFileSync(jsonFile, 'utf8'));

if (!Array.isArray(sections) || sections.length !== 5) {
  throw new Error(`Expected exactly 5 sections, got ${Array.isArray(sections) ? sections.length : typeof sections}`);
}
for (const key of ['kicker', 'title', 'body', 'chips', 'links']) {
  for (const s of sections) if (!(key in s)) throw new Error(`Section missing "${key}": ${JSON.stringify(s)}`);
}

// Single-quote by default; fall back to double quotes if the string contains a
// literal single quote (matches the original file's own convention), escaping
// any of that quote char and backslashes.
function jsString(str) {
  const q = str.includes("'") ? '"' : "'";
  const escaped = str.replace(/\\/g, '\\\\').replace(new RegExp(q, 'g'), '\\' + q);
  return q + escaped + q;
}
function jsArray(arr) { return '[' + arr.map(jsString).join(',') + ']'; }
function jsLinks(links) {
  return '[' + links.map(l => `{label: ${jsString(l.label)}, url: ${jsString(l.url)}}`).join(',') + ']';
}

const lines = sections.map(s =>
  `    { kicker:${jsString(s.kicker)}, title:${jsString(s.title)}, body:${jsString(s.body)}, chips:${jsArray(s.chips)}, links:${jsLinks(s.links)} },`
);
const newArrText = 'sections = [\n' + lines.join('\n') + '\n  ];';

const marker = 'sections = [';
const start = src.indexOf(marker);
if (start === -1) throw new Error(`"${marker}" not found in ${file}`);
const arrStart = src.indexOf('[', start);
let depth = 0, i = arrStart;
for (; i < src.length; i++) {
  if (src[i] === '[') depth++;
  else if (src[i] === ']') { depth--; if (depth === 0) break; }
}
// consume the trailing ';' too
let end = i + 1;
while (src[end] === ' ' || src[end] === '\t') end++;
if (src[end] === ';') end++;

const out = src.slice(0, start) + newArrText + src.slice(end);
fs.writeFileSync(file, out);
console.log(`Updated ${file} (${sections.length} sections).`);
