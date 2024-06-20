#!/usr/bin/env node

const process = require('process');

const args = process.argv.slice(2).join(' ');

if (!args) {
  console.log('No argument');
} else {
  let arg = args.split(' ');
  console.log(arg[0]);
}
