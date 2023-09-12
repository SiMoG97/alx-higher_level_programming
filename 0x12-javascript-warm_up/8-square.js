#!/usr/bin/node
const { argv: args } = require('process');

const size = parseInt(args[2], 10);
if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
