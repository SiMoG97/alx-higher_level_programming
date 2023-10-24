#!/usr/bin/node
const { argv } = process;
const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: node 100-starwars_characters.js <Movie-ID>');
  process.exit(1);
}

const movieID = argv[2];
request(`https://swapi-api.alx-tools.com/api/films/${movieID}`, function (err, res, data) {
  if (err) {
    console.error(err);
    return;
  }
  try {
    const characters = JSON.parse(data).characters;
    for (const chara of characters) {
      request(chara, function (error, response, body) {
        if (error) {
          console.error(error);
          return;
        }
        try {
          const characName = JSON.parse(body).name;
          console.log(characName);
        } catch (e) {
          console.error(e);
        }
      });
    }
  } catch (e) {
    console.error(e);
  }
});
