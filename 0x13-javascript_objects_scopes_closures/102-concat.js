#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process');

fs.readFile(argv[2], (e, data) => {
  if (e) throw e;
  fs.appendFile(argv[4], data, (err) => {
    if (err) throw err;
  });
});

fs.readFile(argv[3], (e, data) => {
  if (e) throw e;
  fs.appendFile(argv[4], data, (err) => {
    if (err) throw err;
  });
});
