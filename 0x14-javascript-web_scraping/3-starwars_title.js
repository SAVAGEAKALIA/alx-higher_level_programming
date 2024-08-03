#!/usr/bin/node
const request = require('request')
const process = require('process');
movie_id = process.argv.slice(2)[0];
if (movie_id === undefined) {
    console.error('Usage: node script.js <movie_id>');
    process.exit(1);
}

const api = `https://swapi-api.alx-tools.com/api/films/${movie_id}`
console.log(api);
request.get(api, (err, response, body) => {
    if (err) {
        console.log(err);
        process.exit(1)
    }
    if (!response && response.statusCode === 200) {
        console.error(`Error: ${response.statusCode}`);
        process.exit(1)
    }
    const movie = JSON.parse(body)
    console.log(`Title: ${movie.title}`);
});