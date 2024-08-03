#!/usr/bin/node
const request = require('request');
const process = require('process');
const args = process.argv.slice(2)[0];

if (args === undefined) {
  console.log('Usage: node script.js <API URL>');
  process.exit(1);
}

request.get(args).on('response', (response) => {
  console.log('code: ' + response.statusCode);
});
