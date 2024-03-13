#!/usr/bin/node
const Square_ = require('./5-square');

class Square extends Square_ {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.height; j++) {
          row += 'C';
        }
        console.log(row);
      }
    } else {
      super.print();
    }
  }
}
module.exports = Square;
