#!/usr/bin/node
const { argv: args } = require('process');

const iterations = parseInt(args[2], 10);
if (Number.isNaN(iterations)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < iterations; i++) {
    console.log('C is fun');
  }
}
