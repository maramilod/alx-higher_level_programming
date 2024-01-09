#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    let i;
    let j;
    let x;
    if (c === undefined) {
      c = 'X';
    }
    for (i = 0; i < this.height; i++) {
      x = '';
      for (j = 0; j < this.width; j++) {
        x += c;
      }
      console.log(x);
    }
  }
}

module.exports = Square;
