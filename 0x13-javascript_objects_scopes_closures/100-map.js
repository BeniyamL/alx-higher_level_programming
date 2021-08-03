#!/usr/bin/node
const oldlist = require('./100-data').list;
let i = 0;
const newlist = oldlist.map(x => x * i++);
console.log(oldlist);
console.log(newlist);
