#!/usr/bin/node

const process = require('process');

const args = process.argv.slice(2).join(' ');

if (!args) {
  console.log('No argument');
} else {
  console.log(args);
}
