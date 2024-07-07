#!/usr/bin/node

const process = require('process');

const args = process.argv.slice(2)[0]; // Get the first argument

if (isNaN(args)) {
  console.log('Not a number');
} else {
  const number = parseInt(args);
  console.log(`My number: ${number}`);
}
