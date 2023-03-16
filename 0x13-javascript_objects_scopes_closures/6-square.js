#!/usr/bin/node
const square1 = require('./5-square');

class Square extends square1 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    const row = c.repeat(this.size);
    for (let i = 0; i < this.size; i++) {
      console.log(row);
    }
  }
}

module.exports = Square;
