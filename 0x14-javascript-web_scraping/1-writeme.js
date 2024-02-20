#!/usr/bin/node

const first = require('fs');
const second = process.argv;

try {
  first.writeFileSync(second[2], second[3], 'utf8');
} catch (err) {
  console.log(err);
}
