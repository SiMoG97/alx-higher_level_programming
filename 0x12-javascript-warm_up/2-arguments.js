#!/usr/bin/node
const process = require('process');

const args = process.argv;
const argsLen = args.length;
if (argsLen === 2) {
  console.log('No argument');
} else if (argsLen === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
