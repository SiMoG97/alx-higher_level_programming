#!/usr/bin/node
let argsPrintedCount = 0;
exports.logMe = function (item) {
  console.log(`${argsPrintedCount}: ${item}`);
  argsPrintedCount++;
};
