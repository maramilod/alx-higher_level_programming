#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w && h && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x = '';
    for (let i = 0; i < this.width; i++) {
      x = x + 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(x);
    }
  }
};
