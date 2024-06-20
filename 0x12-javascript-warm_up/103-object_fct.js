#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12,
  incr () { // Define incr function within the object
    this.value++; // Use "this" to refer to the object itself
  }
};

console.log(myObject);

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
