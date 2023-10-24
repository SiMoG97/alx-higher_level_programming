#!/usr/bin/node
const { argv } = process;
const fs = require('fs');

if (process.argv.length < 3) {
  console.error('Usage: node 0-readme.js <file-path>');
  process.exit(1);
}

fs.readFile(argv[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
