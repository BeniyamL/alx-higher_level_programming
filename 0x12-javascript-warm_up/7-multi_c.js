#!/usr/bin/node
const myVar = 'C is fun';
let i;
const len = parseInt(process.argv[2]);
if (isNaN(len)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < len; i++) {
    console.log(myVar);
  }
}
