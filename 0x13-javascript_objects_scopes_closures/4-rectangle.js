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
