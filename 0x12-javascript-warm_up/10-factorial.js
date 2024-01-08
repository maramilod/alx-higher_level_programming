#!/usr/bin/node

const arg = parseInt(process.argv[2]);
if (arg) {
  console.log(fac (arg));
} else {
  console.log(1);
}
function fac (num) {
  if (num === 1) {
    return (1);
  }
  return (num * fac (num - 1));
}
