#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(baseUrl, function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body);
    printCharachter(results.characters);
  }
});

function printCharachter (Array) {
  for (const count in Array) {
    const url = Array[count];
    request(url, function (error, response, body) {
      if (!error) {
        const info = JSON.parse(body);
        console.log(info.name);
      }
    });
  }
}
