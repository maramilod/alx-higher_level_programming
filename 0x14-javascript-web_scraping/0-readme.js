#!/usr/bin/node

const first = require('fs');
const second = process.argv;

try {
  console.log(first.readFileSync(second[2], 'utf8'));
} catch (err) {
  console.log(err);
}
