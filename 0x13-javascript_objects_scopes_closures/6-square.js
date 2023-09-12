#!/usr/bin/node
const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    // if (!c) {
    //   this.print();
    // } else {
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
    // }
  }
}

module.exports = Square;
