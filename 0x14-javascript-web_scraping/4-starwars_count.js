#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let cnt = 0;

request(url, function (_err, response, body) {
  if (_err) {
    console.log(_err);
  } else {
    body = JSON.parse(body).results;

    for (let i = 0; i < body.length; i++) {
      const colChar = body[i].characters;
      for (let j = 0; j < colChar.length; j++) {
        const rowChar = colChar[j];
        const id = rowChar.split('/')[5];
        if (id === '18') {
          cnt += 1;
        }
      }
    }
  }
  console.log(cnt);
});
