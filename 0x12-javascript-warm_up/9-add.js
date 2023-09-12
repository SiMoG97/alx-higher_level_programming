#!/usr/bin/node
const { argv: args } = require('process');

const [num1, num2] = [parseInt(args[2], 10), parseInt(args[3], 10)];

function add (a, b) {
  return a + b;
}
console.log(add(num1, num2));
