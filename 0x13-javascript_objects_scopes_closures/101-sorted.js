#!/usr/bin/node
const { dict } = require('./101-data');

const dictEntries = Object.entries(dict);
const newDict = [...new Set(Object.values(dict))].reduce((acc, curr) => {
  const occurences = [];
  for (let i = 0; i < dictEntries.length; i++) {
    if (dictEntries[i][1] === curr) {
      occurences.push(dictEntries[i][0]);
    }
  }
  acc[curr] = occurences;
  return acc;
}, {});

console.log(newDict);
