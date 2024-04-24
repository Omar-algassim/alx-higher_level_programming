#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
let count = 0;
const result = {};

request(url, function (error, response, body) {
  if (!error) {
    const data = JSON.parse(body);
    while (count < data.length) {
      const element = data[count];
      if (element.completed === true) {
        if (result[element.userId] === undefined) {
          result[element.userId] = 1;
        } else {
          result[element.userId] += 1;
        }
      }
      count += 1;
    }
    console.log(result);
  }
});
