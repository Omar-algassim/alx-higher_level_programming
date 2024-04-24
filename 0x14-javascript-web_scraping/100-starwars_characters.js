#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const base_url = 'https://swapi-api.alx-tools.com/api/films/' + id

request(base_url, function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body);
    const url_array = results.characters;
    for (const count in url_array) {
        const url = url_array[count]
        request(url, function (error, response, body) {
            if (!error) {
            const info = JSON.parse(body)
            console.log(info.name)
            }
        })
    }

  }
});
