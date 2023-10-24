#!/usr/bin/node
const { argv } = process;
const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: node 2-statuscode.js <url>');
  process.exit(1);
}

request(argv[2], function (err, res) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(`code: ${res.statusCode}`);
});
