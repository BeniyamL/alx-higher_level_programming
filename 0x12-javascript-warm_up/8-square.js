#!/usr/bin/node
let i, j;
const len = parseInt(process.argv[2]);
if (isNaN(len)) {
  console.log('Missing size');
} else {
  for (j = 0; j < len; j++) {
    let line = '';
    for (i = 0; i < len; i++) {
      line += 'X';
    }
    console.log(line);
  }
}
