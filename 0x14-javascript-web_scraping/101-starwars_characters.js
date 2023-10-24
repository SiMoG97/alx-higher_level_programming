#!/usr/bin/node
const { argv } = process;
const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: node 101-starwars_characters.js <Movie-ID>');
  process.exit(1);
}

function fetchCharacters (url) {
  return new Promise(
    (resolve, reject) => {
      request(url, (err, res, body) => {
        if (err) {
          console.error(err);
          reject(err);
        }
        const character = JSON.parse(body).name;
        resolve(character);
      });
    }
  );
}

const movieID = argv[2];
request(`https://swapi-api.alx-tools.com/api/films/${movieID}`, function (err, res, data) {
  if (err) {
    console.error(err);
    return;
  }
  try {
    const characters = JSON.parse(data).characters;
    const promises = characters.map(url => fetchCharacters(url));
    Promise.all(promises).then((res) => {
      res.forEach((name) => {
        console.log(name);
      });
    }).catch(e => {
      console.log(e);
    });
  } catch (e) {
    console.error(e);
  }
});
