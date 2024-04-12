#!/usr/bin/node

class Rectangle {
  width;
  height;

  constructor(w, h) {
    if ((!Number.isInteger(w) || w <= 0) || (!Number.isInteger(h) || h <= 0)) {
      /* console.log("Rectangle {}") */
      this.width = undefined;
      this.height = undefined;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  // Print method
  print() {
    const x = 'X';
    let output = '';
    for (let i = 0; i < parseInt(this.height); i++) {
      for (let j = 0; j < parseInt(this.width); j++) {
        output += x;
      }
      console.log(output);
      output = '';
    }
  }

  rotate() {
    const clone = this.width;
    this.width = this.height;
    this.height = clone;
  }

  double() {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
