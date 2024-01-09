#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w && h && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
  rotate () {
    const he = this.height;
    this.height = this.width;
    this.width = he;
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
