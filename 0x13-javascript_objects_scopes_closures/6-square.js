#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let letter = c;
    if (!letter) {
      letter = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(letter.repeat(this.width));
    }
  }
}

module.exports = Square;
