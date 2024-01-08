#!/usr/bin/node

const len = process.argv.length;
if (len > 3) {
  let big = parseInt(process.argv[2]);
  for (let i = 2; i <= len; i++) {
    if (parseInt(process.argv[i]) > big) {
      big = parseInt(process.argv[i]);
    }
  }
  let secB = parseInt(process.argv[2]) === big ? parseInt(process.argv[3]) : parseInt(process.argv[2]);
  for (let i = 2; i <= len; i++) {
    if (process.argv[i] >= secB && parseInt(process.argv[i]) < big) {
      secB = parseInt(process.argv[i]);
    }
  }
  console.log(secB);
} else {
  console.log(0);
}
