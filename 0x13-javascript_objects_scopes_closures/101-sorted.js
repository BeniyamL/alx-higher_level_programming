#!/usr/bin/node
const olddict = require('./101-data').dict;
const newdict = {};
for (const key in olddict) {
  if (newdict[olddict[key]] === undefined) {
    newdict[olddict[key]] = [key];
  } else {
    newdict[olddict[key]].push(key);
  }
}
console.log(newdict);
