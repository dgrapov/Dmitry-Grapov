#!/usr/bin/env node
// Pulls the `sections = [...]` array out of the .dc.html source and prints it as JSON.
// Usage: node extract-sections.js "Dmitry Grapov Forest.dc.html" > sections.json
'use strict';
const fs = require('fs');
const file = process.argv[2];
if (!file) { console.error('Usage: extract-sections.js <file.dc.html>'); process.exit(1); }
const src = fs.readFileSync(file, 'utf8');

const marker = 'sections = [';
const start = src.indexOf(marker);
if (start === -1) throw new Error(`"${marker}" not found in ${file}`);
const arrStart = src.indexOf('[', start);
let depth = 0, i = arrStart;
for (; i < src.length; i++) {
  if (src[i] === '[') depth++;
  else if (src[i] === ']') { depth--; if (depth === 0) break; }
}
if (depth !== 0) throw new Error('Unbalanced brackets while scanning sections array');
const arrText = src.slice(arrStart, i + 1);

// The array is plain JS-object-literal syntax (single quotes, unquoted keys),
// not JSON, so it needs eval rather than JSON.parse.
// eslint-disable-next-line no-eval
const sections = eval(arrText);

process.stdout.write(JSON.stringify(sections, null, 2) + '\n');
