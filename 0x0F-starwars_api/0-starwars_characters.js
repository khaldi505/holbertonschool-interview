#!/usr/bin/node

const request = require('request');
const link = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
let counter = 0;

request(link, function (error, response, bd) {
  if (error) {
    return console.log(error);
  }
  const url = JSON.parse(bd).characters;
  for (counter = 0; counter < url.length; counter++) {
    request(url[counter], function (err, rep, body) {
      if (err) {
        return console.log(err);
      }
      const character = JSON.parse(body).name;
      console.log(character);
    });
  }
});