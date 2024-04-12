#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      Object.create(null);
    }
  }

  // Print method
  print() {
    const x = 'x';
    let g = '';
    for (let i = 0; i < parseInt(this.height); i++) {
      for (let j = 0; j < parseInt(this.width); j++) {
        g += x;
      }
      console.log(g);
      g = '';
    }
  }
}

module.exports = Rectangle;
