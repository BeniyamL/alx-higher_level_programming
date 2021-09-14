#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (_err, response, body) {
  if (_err) {
    console.log(_err);
  } else {
    body = JSON.parse(body);
    console.log(body.title);
  }
});
