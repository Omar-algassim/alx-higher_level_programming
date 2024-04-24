#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(baseUrl, function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body);
    const urlArray = results.characters;
    for (const count in urlArray) {
      const url = urlArray[count];
      request(url, function (error, response, body) {
        if (!error) {
          const info = JSON.parse(body);
          console.log(info.name);
        }
      });
    }
  }
});
