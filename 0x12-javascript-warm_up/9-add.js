#!/usr/bin/node

function add (a, b) {
  const num3 = a + b;
  if (num3) {
    console.log(num3);
  } else {
    console.log('NaN');
  }
}
const num = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);
add(num, num2);
