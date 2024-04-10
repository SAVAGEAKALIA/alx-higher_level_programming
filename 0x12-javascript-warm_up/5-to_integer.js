#!/usr/bin/node

const process = require('process');

const args = process.argv.slice(2).join(' ');

if (args.length === 0) {
  console.log('Not a Number');
} else {
  let i = 0;
  const argssplit = args.split(' ');
  while (argssplit[i]) {
    const a = parseInt(argssplit[i]);
    if (isNaN(a)) {
      console.log('Not a Number');
    } else {
      console.log('My Number: ' + a);
    }
    i++;
  }
}
