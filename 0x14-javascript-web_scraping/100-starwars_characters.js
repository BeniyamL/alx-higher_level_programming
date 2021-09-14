#!/usr/bin/node

const request = require('request');
const urlFilm = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(urlFilm, function (_err, response, body) {
  if (_err) {
    console.log(_err);
  } else {
    body = JSON.parse(body).characters;

    for (let i = 0; i < body.length; i++) {
      const urlPeople = body[i];
      request(urlPeople, function (err, res, bdy) {
        if (err) {
          console.log(err);
        } else {
          bdy = JSON.parse(bdy).name;
          console.log(bdy);
        }
      });
    }
  }
});
