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
}

module.exports = Rectangle;
