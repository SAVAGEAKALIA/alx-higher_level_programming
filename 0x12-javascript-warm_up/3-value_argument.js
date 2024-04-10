#!/usr/bin/env node

const process = require('process');

const args = process.argv.slice(2).join(' ');

if (!args) {
  console.log('No argument');
} else if (args.includes(' ')) {
  const argssplit = args.split(' ');
  let i = 0;
  while (argssplit[i] !== undefined) {
    console.log(argssplit[i]);
    i++;
  }
} else {
  console.log(args);
}
