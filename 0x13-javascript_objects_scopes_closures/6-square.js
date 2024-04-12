#!/usr/bin/node
const Sq = require('./5-square');

class Square extends Sq {
  size;

  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c = 'X') {
    let output = '';
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        output += c;
      }
      console.log(output);
      output = '';
    }
  }
}

module.exports = Square;
