#!/usr/bin/node
const process = require('process');
const fs = require('fs');
const request = require('request');
const site = process.argv.slice(2)[0];
const filepath = process.argv.slice(2)[1];

if (!site || !filepath) {
  console.error('Usage: node fetch_and_save.js <site_url> <filepath>');
  process.exit(1);
}

request(site, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    process.exit(1);
  }
  if (response.statusCode !== 200) {
    console.error(`Error: Received HTTP status code ${response.statusCode}`);
    process.exit(1);
  }
  fs.writeFile(filepath, body, (err) => {
    if (err) {
      console.log(err);
      process.exit(1);
    }
  });
});
