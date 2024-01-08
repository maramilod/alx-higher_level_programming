#!/usr/bin/node

const x = parseInt(process.argv[2]);
let y = 'X';
if (x) {
  for (let i = 0; i < x; i++) {
    y = y + 'X';
  }
  for (let i = 0; i < x; i++) {
    console.log(y);
  }
} else {
  console.log('Missing number of occurrences');
}
