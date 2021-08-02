#!/usr/bin/node
const len = process.argv.length;
let i;
if (len <= 3) {
  console.log(0);
} else {
  let largest, s;
  if (process.argv[2] > process.argv[3]) {
    largest = process.argv[2];
    s = process.argv[3];
  } else {
    largest = process.argv[3];
    s = process.argv[2];
  }
  for (i = 4; i < len; i++) {
    if (process.argv[i] > largest) {
      s = largest;
      largest = process.argv[i];
    } else if (process.argv[i] > s) {
      s = process.argv[i];
    }
  }
  console.log(s);
}
