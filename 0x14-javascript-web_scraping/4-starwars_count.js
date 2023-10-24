#!/usr/bin/node
const { argv } = process;
const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: node 4-starwars_count.js <URL>');
  process.exit(1);
}

request(argv[2], function (err, res, data) {
  if (err) {
    console.error(err);
    return;
  }
  try {
    const characterID = 18;
    let count = 0;
    const results = JSON.parse(data).results;
    for (const film of results) {
      for (const char of film.characters) {
        if (char.includes(characterID)) {
          count++;
        }
      }
    }
    console.log(count);
  } catch (e) {
    console.error(e);
  }
});
