#!/usr/bin/node
const { argv } = process;
const request = require('request');
const fs = require('fs');

if (process.argv.length < 4) {
  console.error('Usage: node 5-request_store.js <URL> <file path>');
  process.exit(1);
}

request(argv[2], function (err, res, data) {
  if (err) {
    console.error(err);
    return;
  }
  const { body } = res;
  fs.writeFile(argv[3], body, err => {
    if (err) {
      console.error(err);
    }
  });
});
