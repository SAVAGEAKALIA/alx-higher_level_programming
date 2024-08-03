#!/usr/bin/node
const process = require('process');
const request = require('request');
const movieapi = process.argv[2];

if (!movieapi) {
  console.error('Usage: node 0-fetch-character.js <character_id>');
  process.exit(1);
}
const characterId = 18;

request.get(movieapi, (err, response, body) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  if (response.statusCode !== 200) {
    console.error(`Request failed with status code ${response.statusCode}`);
    process.exit(1);
  }

  const films = JSON.parse(body).results;
  let count = 0;
  for (const film of films) {
    const characters = film.characters;
    for (const character of characters) {
      if (character.includes(characterId)) {
        count++;
        break;
      }
    }
  }
  console.log(count);
});
