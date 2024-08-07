#!/usr/bin/node
const fs = require('fs');
const process = require('process');
const args = process.argv.slice(2)[0];
const input = process.argv.slice(2)[1];

if (args === undefined) {
  console.error('Usage: file not given');
  process.exit(1);
}
fs.writeFile(args, input, (err) => {
  if (err) {
    console.log(err);
    process.exit(1);
  }
});
