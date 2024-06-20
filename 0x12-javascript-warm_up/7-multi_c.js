#!/usr/bin/node
const process = require('process');

const args = process.argv.slice(2).join(' ');

if (args.length === 0 || isNaN(parseInt(args))) {
  console.log('Missing number of occurrences');
} else {
  const word = 'C is fun';
  let count = 0;
  const argssplit = args.split(' ');

  while (argssplit[count] !== undefined) {
    const number = parseInt(argssplit[count]);
    for (let i = 0; i < number; i++) {
      console.log(word);
    }
    count++;
  }
}
