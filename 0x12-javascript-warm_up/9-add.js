#!/usr/bin/node

const process = require('process');

const args = process.argv.slice(2).join(' ');

function add (a, b) {
  return a + b;
}

if (args.length === 0 || isNaN(parseInt(args))) {
  console.log('NaN');
} else if (args.length === 1) {
  console.log('NaN');
} else {
  const argssplit = args.split(' ');
  const a = parseInt(argssplit[0]);
  const b = parseInt(argssplit[1]);

  const result = add(a, b);
  console.log(result);
}
