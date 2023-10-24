#!/usr/bin/node
const { argv } = process;
const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: node 3-starwars_title.js <movie-ID>');
  process.exit(1);
}

request(`https://swapi-api.alx-tools.com/api/films/${argv[2]}`, function (err, res, data) {
  if (err) {
    console.error(err);
    return;
  }

  console.log(JSON.parse(data).title);
});
