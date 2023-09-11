#!/usr/bin/node
const { argv: args } = require('process');

const number = parseInt(args[2], 10);
if (Number.isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
