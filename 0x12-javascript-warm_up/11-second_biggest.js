#!/usr/bin/node

const len = process.argv.length;
if (len > 3) {
  let big = process.argv[2];
  for (let i = 2; i <= len; i++) {
    if (process.argv[i] > big) {
      big = process.argv[i];
    }
  }
  let secB = process.argv[2] === big ? process.argv[3] : process.argv[2];
  for (let i = 2; i <= len; i++) {
    if (process.argv[i] >= secB && process.argv[i] < big) {
     secB = process.argv[i];
    }
  }
  console.log(secB);
} else {
  console.log(len);
}
