#!/usr/bin/node

const request = require('request');
const urlFilm = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(urlFilm, function (_err, response, body) {
  if (_err) {
    console.log(_err);
  } else {
    const characters = JSON.parse(body).characters;

    printName(characters, 0);
  }
});

function printName (characters, i) {
  const urlPeople = characters[i];
  request(urlPeople, function (err, res, bdy) {
    if (err) {
      console.log(err);
    } else {
      bdy = JSON.parse(bdy).name;
      console.log(bdy);
      if (i + 1 < characters.length) {
        printName(characters, i + 1);
      }
    }
  });
}
