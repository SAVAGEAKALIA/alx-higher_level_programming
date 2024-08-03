#!/usr/bin/node
const request = require('request');
const process = require('process');
const movieId = process.argv.slice(2)[0];
if (movieId === undefined) {
  console.error('Usage: node script.js <movie_id>');
  process.exit(1);
}

const api = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request.get(api, (err, response, body) => {
  if (err) {
    console.log(err);
    process.exit(1);
  }
  if (!response && response.statusCode === 200) {
    console.error(`Error: ${response.statusCode}`);
    process.exit(1);
  }
  const movie = JSON.parse(body);
  console.log(`${movie.title}`);
});
