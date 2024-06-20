#!/usr/bin/node

const process = require('process');

const args = process.argv.slice(2).join(' ');
let ar

if (!args) {
  console.log('No argument');
} else {
  ar = args.split(' ');
  console.log(ar[0]);
}
