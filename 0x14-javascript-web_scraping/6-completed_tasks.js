#!/usr/bin/node
const request = require('request');
const process = require('process');
const api = process.argv.slice(2)[0];

if (api === undefined) {
  console.log('Usage: node script.js <API URL>');
  process.exit(1);
}

request(api, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }
  if (response.statusCode !== 200) {
    console.error(`Request Failed with status code: ${response.statusCode}`);
    process.exit(1);
  }

  const completedtodo = {};
  const todo = JSON.parse(body);
  for (const user of todo) {
    if (user.completed === true) {
      if (!completedtodo[user.userId]) {
        completedtodo[user.userId] = 0;
      }
      completedtodo[user.id] = completedtodo[user.userId]++;
    }
  }
  console.log(completedtodo);
});
