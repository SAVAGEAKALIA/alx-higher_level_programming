#!/usr/bin/node

const process = require('process');

const args = parseInt(process.argv.slice(2)[0]); // Get and convert first argument

function factorial(number) {
  if (isNaN(number)) {
    return 1; // Factorial of NaN is 1
  } else if (number === 0) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}

const result = factorial(args);
console.log(result);
